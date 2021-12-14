from rq import Queue
from sys import stderr
from flask import Flask, make_response, render_template, request
from flask import jsonify
import os
import redis

from backend.img_util import GalleryRequest, Image
from backend.img_generate import generate_gallery
from backend.solana_search import search
from backend.solana_util import SearchRequest, SearchResponse, SolanaNFT

#-----------------------------------------------------------------------

# Flask application.
app = Flask(__name__, template_folder=".")

# Path to front-end templates.
frontend_path = "templates/"

# Default error message.
default_err = "A server error has occurred."

# URL pattern for Solien images.
ipfs_url = "https://ipfs.io/ipfs/"

# Queue for background tasks.
redis_url = os.getenv("REDISTOGO_URL", "redis://localhost:6379")
conn = redis.from_url(redis_url)
q = Queue(connection=conn)

#-----------------------------------------------------------------------

# Map between error messages and their corresponding codes.
error_message_code_map = [
    ("Wallet contains no Solien NFTs.", "400"),
    ("The specified wallet number could not be found.", "404"),
    ("Cannot process call to blockchain.", "503"),
    ("A server error has occurred.", "500")
]

# Returns the error code corresponding to the exception.
def get_error_code(ex):
    ex_str = str(ex)
    for (err_message, err_code) in error_message_code_map:
        if err_message == ex_str:
            return err_code
    # Return last error code by default.
    return error_message_code_map[-1][1]

# Returns the error message corresponding to the code.
def get_error_message(code):
    for (err_message, err_code) in error_message_code_map:
        if err_code == code:
            return err_message
    # Return last error message by default.
    return error_message_code_map[-1][0]

#-----------------------------------------------------------------------

# Helper function to format the details of a background task in JSON.
def format_task_details(status, response):
    return jsonify({"status": status, "response": response})

#-----------------------------------------------------------------------

# Renders and returns the homepage.
@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    try:
        html = render_template(frontend_path + "index.html")
        return make_response(html)

    except Exception as ex:
        print(ex, file=stderr)
        html = render_template(frontend_path + "error.html",
                               error_message=default_err)
        return make_response(html)

#-----------------------------------------------------------------------

# Returns the exception encountered while executing the given job.
def get_exception(job):
    exc_keyword = "Exception: "
    exc_index = job.exc_info.rindex(exc_keyword)
    return job.exc_info[exc_index + len(exc_keyword):].strip()

# Returns the status of the job with the given ID.
@app.route("/status/<string:page>/<string:job_id>", methods=["GET"])
def job_status(page, job_id):
    try:
        job = q.fetch_job(job_id)
        if not job:
            return format_task_details("unknown", "")

        status = job.get_status()
        if status == "failed":
            ex_info  = get_exception(job)
            err_code = get_error_code(ex_info) 
            return format_task_details("failed", err_code)
        elif not job.result:
            return format_task_details(status, "")

        result = job.result.json() if page == "gallery" else job.result
        return format_task_details(status, result)

    except Exception as ex:
        print(ex, file=stderr)
        return format_task_details("failed", get_error_code(str(ex)))

#-----------------------------------------------------------------------

# Renders and returns the loading page.
@app.route("/loading/<string:page>/<string:job_id>", methods=["GET"])
def loading(page, job_id):
    try:
        job = q.fetch_job(job_id)
        html = render_template(frontend_path + "loading.html",
                               page=page, job_id=job.get_id())
        return make_response(html)

    except Exception as ex:
        print(ex, file=stderr)
        html = render_template(frontend_path + "error.html",
                               error_message=default_err)
        return make_response(html)

#-----------------------------------------------------------------------

# Returns the ID of the background task querying for the given wallet.
@app.route("/enqueue_search/<string:wallet>", methods=["GET"])
def enqueue_search(wallet):
    try:
        search_req = SearchRequest(wallet)
        job = q.enqueue(search, search_req)
        return job.get_id()

    except Exception as ex:
        print(ex, file=stderr)
        return -1

#-----------------------------------------------------------------------

# Renders and returns the gallery builder page.
@app.route("/gallery/<string:id_strs>", methods=["GET"])
def gallery(id_strs):
    try:
        imgs = [ipfs_url + img_id for img_id in id_strs.split("=")]
        html = render_template(frontend_path + "gallery.html",
                               wallet="aaron", search_res=imgs)
        response = make_response(html)
        return response

    except Exception as ex:
        print(ex, file=stderr)
        html = render_template(frontend_path + "error.html",
                               error_message=default_err)
        return make_response(html)

#-----------------------------------------------------------------------

# Creates a gallery from the specified image IDs and background.
def get_gallery(id_strs, color, bg_url, bg_type):
    imgs = []
    for img_id in id_strs.split("="):
        img_url = ipfs_url + img_id
        nft_img = Image()
        nft_img.loadURL(img_url)
        imgs.append(nft_img)

    background_img = Image()

    if (bg_type == "color"):
        background_img.loadColor(color)
    else:
        background_img.loadURL(bg_url)
    gallery_request = GalleryRequest(imgs, background_img)

    response = generate_gallery(gallery_request)
    img_url  = response.get_gallery()
    return img_url

# Returns the ID of the background task creating the given gallery.
@app.route("/enqueue_gallery/<string:id_strs>", methods=["GET"])
def enqueue_gallery(id_strs):
    try:
        color = request.cookies.get("color")
        bg_url = request.cookies.get("backgroundImage")
        bg_type = request.cookies.get("backgroundImageType")
        job = q.enqueue(get_gallery, id_strs, color, bg_url, bg_type)
        return job.get_id()

    except Exception as ex:
        print(ex, file=stderr)
        return -1

#-----------------------------------------------------------------------

# Renders and returns the download page.
@app.route("/download/<string:id_strs>", methods=["GET"])
def download(id_strs):
    try:
        img_ids = id_strs.split("=")
        img_url = ("http://res.cloudinary.com/dskvzlrpw/image/upload/" + 
                   img_ids[0] + "/" + img_ids[1])
        html = render_template(frontend_path + "download.html",
                               url=img_url)
        response = make_response(html)
        return response

    except Exception as ex:
        print(ex, file=stderr)
        html = render_template(frontend_path + "error.html",
                               error_message=default_err)
        return make_response(html)

#-----------------------------------------------------------------------

# Renders and returns the error page.
@app.route("/error", methods=["GET"])
def error():
    status_code = request.args.get("status_code")
    html = render_template(frontend_path + "error.html",
                           error_message=get_error_message(status_code))
    return make_response(html)