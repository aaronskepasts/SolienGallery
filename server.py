from sys import stderr
from flask import Flask, request, make_response, render_template, jsonify

from backend.img_util import GalleryRequest, Image
from backend.img_generate import generate_gallery
from backend.solana_search import search
from backend.solana_util import SearchRequest, SearchResponse, SolanaNFT

#-----------------------------------------------------------------------

app = Flask(__name__, template_folder=".")
frontend_path = "frontend/pages/"

#-----------------------------------------------------------------------

# Renders and returns the homepage.
@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def index():
    html = render_template(frontend_path + "index.html")
    return make_response(html)

#-----------------------------------------------------------------------

# Renders and returns the download page.
@app.route("/download/<string:id>", methods=["GET"])
def download(id):
    # print(id)
    # print(type(id))
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

    url = generate_gallery(gallery_request)
    html = render_template(frontend_path + "download.html", url=url)
    return make_response(html)

#-----------------------------------------------------------------------

# Renders and returns the gallery builder page.
@app.route("/alpha_gallery/<wallet>", methods=["GET"])
def alpha_gallery(wallet):
    search_req = SearchRequest(wallet)
    search_res = search(search_req)
    if search_res[0] == "":
        html = render_template(frontend_path + "alpha_gallery.html",
                                wallet=wallet, search_res=search_res[1])
    else:
        html = render_template(frontend_path + "error.html",
                               error_message=search_res[0])
    return make_response(html)
