import urllib.request, json

# Solana NFT object.
class SolanaNFT:
	# Construct an NFT from an image URL.  
	def __init__(self, address, metadata):
		self.address = address
		self.metadata = metadata
		with urllib.request.urlopen(metadata['data']['uri']) as url:
			data = json.loads(url.read().decode())
			self.data = data
			self.img_url = data['image']

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
