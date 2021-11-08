from sys import stderr
from flask import Flask, request, make_response, render_template

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
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

# Renders and returns the download page.
@app.route("/download", methods=["GET"])
def download():
    html = render_template(frontend_path + "download.html")
    response = make_response(html)
    return response

#-----------------------------------------------------------------------

# Renders and returns the gallery builder page.
@app.route("/alpha_gallery/<wallet>", methods=["GET"])
def alpha_gallery(wallet):
    search_req = SearchRequest(wallet)
    search_res = search(search_req)
    html = render_template(frontend_path + "alpha_gallery.html",
                           wallet=wallet, search_res=search_res)
    response = make_response(html)
    return response
