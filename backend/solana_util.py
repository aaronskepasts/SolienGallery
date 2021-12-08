import json
import urllib.request

#-----------------------------------------------------------------------

# get data (with image field) given metadata
def get_data_from_url(data_url):
    with urllib.request.urlopen(data_url) as url:
        data = json.loads(url.read().decode())
        return(data)

# Solana NFT object.
class SolanaNFT:
	# Constructs an NFT from an image URL.
	def __init__(self, address, metadata, new=False):
		self.address = address
		if new:
			self.metadata = get_data_from_url(metadata['data']['uri'])
		else:
			self.metadata = metadata

	# Returns the image URL associated with the NFT.
	def get_img_url(self):
		return self.metadata["image"]

#-----------------------------------------------------------------------

# Request for a query of the NFTs owned by a wallet.
class SearchRequest:
	# Constructs a request containing a wallet.
	def __init__(self, wallet):
		self.wallet = wallet

#-----------------------------------------------------------------------

# Response from a query of the NFTs owned by a wallet.
class SearchResponse:
	# Constructs a response containing a list of NFT objects.
	def __init__(self, nft_list):
		self.nft_list = nft_list

	# Serializes object to a JSON formatted string.
	def json(self):
		return json.dumps(self, default=lambda o: o.__dict__)