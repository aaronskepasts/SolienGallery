// Solana NFT object.
// TODO: This class needs to be finalized.
class SolanaNFT {
	// Construct an NFT from an image URL.  
	constructor(img_url) {
		this.img_url = img_url;
	}

	// Return the image URL associated with the NFT.
	img_url() {
		return this.img_url;
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
