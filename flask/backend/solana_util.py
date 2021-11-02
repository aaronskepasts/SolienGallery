# Solana NFT object.
# TODO: This class needs to be finalized.
class SolanaNFT:
	# Construct an NFT from an image URL.  
	def __init__(self, img_url):
		self.img_url = img_url

	# Return the image URL associated with the NFT.
	def get_img_url(self):
		return self.img_url

# Request for a query of the NFTs owned by a wallet.
class SearchRequest:
	# Construct a request containing a wallet.
	def __init__(self, wallet):
		self.wallet = wallet

# Response from a query of the NFTs owned by a wallet.
class SearchResponse:
	# Construct a response containing a list of NFT objects.
	def __init__(self, nft_list):
		self.nft_list = nft_list
