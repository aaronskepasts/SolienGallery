const express = require("express");
const path = require("path");

const sol = require("../backend/solana_search");
const sol_util = require("../backend/solana_util");

/*--------------------------------------------------------------------*/

const app = express();
app.set("view engine", "ejs");

app.get("/", function(req, res) {
	res.render("pages/index");
});

app.get("/alpha_gallery/:wallet", function(req, res) {
	wallet = req.params.wallet;
	searchReq = new sol_util.SearchRequest(wallet);
	searchRes = sol.search(searchReq);
	res.render("pages/alpha_gallery", { name: wallet, searchRes: searchRes });
});

app.get("/download", function(req, res) {
	res.render("pages/download");
});

const port = process.env.PORT || 8080;
app.listen(port);
console.log("Server started at http://localhost:" + port);
