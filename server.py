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

# URL pattern for Solien images.
ipfs_url = "https://ipfs.io/ipfs/"

# Queue for background tasks.
redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
conn = redis.from_url(redis_url)
q = Queue(connection=conn)

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
        error_message = "A server error has occurred."
        html = render_template(frontend_path + "error.html",
                               error_message=error_message)
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
        error_message = "A server error has occurred."
        html = render_template(frontend_path + "error.html",
                               error_message=error_message)
        return make_response(html)

#-----------------------------------------------------------------------

# Helper function to format the details of a background task in JSON.
def format_task_details(status, response):
    return jsonify({"status": status, "response": response})

# Returns the status of the job with the given ID.
@app.route("/status/<string:job_id>", methods=["GET"])
def job_status(job_id):
    try:
        job = q.fetch_job(job_id)
        if not job:
            return format_task_details("unknown", "")
        elif not job.result:
            return format_task_details(job.get_status(), "")
        return format_task_details(job.get_status(), job.result.json())

    except Exception as ex:
        print(ex, file=stderr)
        error_message = "A server error has occurred."
        html = render_template(frontend_path + "error.html",
                               error_message=error_message)
        return make_response(html)

#-----------------------------------------------------------------------

# Renders and returns the homepage.
@app.route("/loading/<string:job_id>", methods=["GET"])
def loading(job_id):
    try:
        job = q.fetch_job(job_id)
        html = render_template(frontend_path + "loading.html",
                               job_id=job.get_id())
        return make_response(html)

    except Exception as ex:
        print(ex, file=stderr)
        error_message = "A server error has occurred."
        html = render_template(frontend_path + "error.html",
                               error_message=error_message)
        return make_response(html)

#-----------------------------------------------------------------------

# Renders and returns the gallery builder page.
@app.route("/alpha_gallery/<string:id_strs>", methods=["GET"])
def alpha_gallery(id_strs):
    try:
        imgs = [ipfs_url + img_id for img_id in id_strs.split("=")]
        html = render_template(frontend_path + "alpha_gallery.html",
                               wallet="aaron", search_res=imgs)
        return make_response(html)

    except Exception as ex:
        print(ex, file=stderr)
        error_message = "A server error has occurred."
        html = render_template(frontend_path + "error.html",
                               error_message=error_message)
        return make_response(html)

#-----------------------------------------------------------------------

# Renders and returns the download page.
@app.route("/download/<string:id_strs>", methods=["GET"])
def download(id_strs):
    try:
        imgs = []
        for img_id in id_strs.split('='):
            img_url = ipfs_url + img_id
            nft_img = Image()
            nft_img.load(img_url)
            imgs.append(nft_img)

        background_url = "https://pbs.twimg.com/profile_banners/1427360637408120837/1633464733/1500x500"
        background_img = Image()
        background_img.load(background_url)
        gallery_request = GalleryRequest(imgs, background_img)

        response = generate_gallery(gallery_request)
        img_url  = response.get_gallery()
        html = render_template(frontend_path + "download.html",
                               url=img_url)
        return make_response(html)

    except Exception as ex:
        print(ex, file=stderr)
        error_message = "A server error has occurred."
        html = render_template(frontend_path + "error.html",
                               error_message=error_message)
        return make_response(html)
