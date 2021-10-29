// Solana NFT object.
// TODO: This class needs to be finalized.
class SolanaNFT {
	// Construct an NFT from an image URL.  
	constructor(imgUrl) {
		this.imgUrl = imgUrl;
	}

	// Return the image URL associated with the NFT.
	getImgUrl() {
		return this.imgUrl;
	}
}

// Request for a query of the NFTs owned by a wallet.
class SearchRequest {
	// Construct a request containing a wallet.
	constructor(wallet) {
		this.wallet = wallet;
	}
}

// Response from a query of the NFTs owned by a wallet.
class SearchResponse {
	// Construct a response containing a list of NFT objects.
	constructor(nftList) {
		this.nftList = nftList;
	}
}

module.exports = { SolanaNFT, SearchRequest, SearchResponse, };
