from sys import stderr
from flask import Flask, request, make_response, render_template, jsonify

from backend.img_util import GalleryRequest, Image
from backend.img_generate import generate_gallery
from backend.solana_search import search
from backend.solana_util import SearchRequest, SearchResponse, SolanaNFT

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder=".")
frontend_path = "templates/"

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

# Renders and returns the download page.
@app.route("/download/<string:id>", methods=["GET"])
def download(id):
    try:
        urls = id.split('=')
        imgs = []
        for i in range(1, len(urls)):
            url = "https://ipfs.io/ipfs/" + urls[i]
            print(url)
            nft_img = Image()
            nft_img.load(url)
            imgs.append(nft_img)
        
        background_url = "https://pbs.twimg.com/profile_banners/1427360637408120837/1633464733/1500x500"
        background_img = Image()
        background_img.load(background_url)
        gallery_request = GalleryRequest(imgs, background_img)

        response = generate_gallery(gallery_request)
        img_url  = response.get_gallery() 
        html = render_template(frontend_path + "download.html", url=img_url)
        return make_response(html)

    except Exception as ex:
        print(ex, file=stderr)
        error_message = "A server error has occurred."
        html = render_template(frontend_path + "error.html",
                               error_message=error_message)
        return make_response(html)

#-----------------------------------------------------------------------

# Renders and returns the gallery builder page.
@app.route("/alpha_gallery/<wallet>", methods=["GET"])
def alpha_gallery(wallet):
    try:
        search_req = SearchRequest(wallet)
        search_res = search(search_req)
        html = render_template(frontend_path + "alpha_gallery.html",
                               wallet=wallet, search_res=search_res)
        return make_response(html)
    
    except Exception as ex:
        print(ex, file=stderr)
        html = render_template(frontend_path + "error.html",
                               error_message=str(ex))
        return make_response(html)
