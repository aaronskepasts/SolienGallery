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
    print(id)
    print(type(id))
    urls = id.split('=')
    ims = list()
    for i in range(1, len(urls)):
        iUrl = "https://ipfs.io/ipfs/"+urls[i]
        print(iUrl)
        item = Image()
        item.load(iUrl)
        ims.append(item)
    
    gallery_request = GalleryRequest(ims)
    """



    
    nft_url = "https://ipfs.io/ipfs/QmT8TSe4k7qgwxpmvQPZkN7cefJz8RtUR4iDDADXRshu4X"
    nft_img1 = Image()
    nft_img1.load(nft_url)
    nft_img2 = Image()
    nft_img2.load(nft_url)
    nft_img3 = Image()
    nft_img3.load(nft_url)

    gallery_request = GalleryRequest([nft_img1, nft_img2, nft_img3])"""
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
