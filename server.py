from sys import stderr
from flask import Flask, request, make_response, render_template

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
@app.route("/download", methods=["GET"])
def download():
    nft_url = "https://ipfs.io/ipfs/QmT8TSe4k7qgwxpmvQPZkN7cefJz8RtUR4iDDADXRshu4X"
    nft_img1 = Image()
    nft_img1.load(nft_url)
    nft_img2 = Image()
    nft_img2.load(nft_url)
    nft_img3 = Image()
    nft_img3.load(nft_url)

    gallery_request = GalleryRequest([nft_img1, nft_img2, nft_img3])
    url = generate_gallery(gallery_request)
    html = render_template(frontend_path + "download.html", url=url)
    return make_response(html)

#-----------------------------------------------------------------------

# Renders and returns the gallery builder page.
@app.route("/alpha_gallery/<wallet>", methods=["GET"])
def alpha_gallery(wallet):
    search_req = SearchRequest(wallet)
    search_res = search(search_req)
    html = render_template(frontend_path + "alpha_gallery.html",
                           wallet=wallet, search_res=search_res)
    return make_response(html)
