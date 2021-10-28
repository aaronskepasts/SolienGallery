const express = require("express");
const path = require("path");

const sol = require("./solana_search");
const sol_util = require("./solana_util");

const app = express();
app.set("view engine", "ejs");

app.get("/", function(req, res) {
	// res.cookie("name", "express").send("cookie set")
	res.render("pages/index");
});

app.get("/alpha_gallery/:wallet", function(req, res) {
	wallet = req.params.wallet;
	searchReq = new sol_util.SearchRequest(wallet);
	searchRes = sol.search(searchReq);
	res.render("pages/alpha_gallery", { name: wallet, searchRes: searchRes });
});

const port = process.env.PORT || 8080;
app.listen(port);
console.log("Server started at http://localhost:" + port);
