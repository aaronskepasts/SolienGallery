const sol_util = require('./solana_util');

// Returns a list of 20 hard-coded Solana NFT objects.
// TODO: This function should return the response after a query to the
//       blockchain.
function search(request) {
	let img_url = "https://ipfs.io/ipfs/QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU";
	let nftList = [];
	for (let i = 0; i < 10; i++) {
		nftList.push(new sol_util.SolanaNFT(img_url));
	}
	return new sol_util.SearchResponse(nftList);
}

module.exports = { search };