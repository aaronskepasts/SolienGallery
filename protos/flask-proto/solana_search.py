from solana_util import SearchResponse, SolanaNFT

#-----------------------------------------------------------------------

# Returns a list of 20 hard-coded Solana NFT objects.
# TODO: This function should return the response after a query to the
#       blockchain.
def search(request):
	img_url = "https://ipfs.io/ipfs/QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU"
	nftList = []
	for i in range(10):
		nftList.append(SolanaNFT(img_url))
	return SearchResponse(nftList)
