from .solana_util import SearchResponse, SolanaNFT
from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork

#-----------------------------------------------------------------------

# Blockchain API key pair
MY_API_KEY_ID = "i80Y9AzQjwfOQfR"
MY_API_SECRET_KEY = "RIT7RKOVA2cQy5S"
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
    api_key_id=MY_API_KEY_ID,
    api_secret_key=MY_API_SECRET_KEY
)

#-----------------------------------------------------------------------

# Returns a list Solana NFT objects.
def search(request):
	try:
		assert MY_API_KEY_ID is not None
		assert MY_API_SECRET_KEY is not None
	except AssertionError:
		raise Exception("API keypair broken")

	# Aaron's Solien NFT Address = 'FN8EXxCE8Nty5h6iNtfdN8tqmCwFYiSuM6j8bLa9Uc5h'
	# Ape NFT Address = 'GUqyT6hsve7TeJVR8NWZriPTVj6wZVkp9FZAsiHy3aYA'

	# nft_addresses will be a list of Strings of NFT addresses
	# to be retrieved from wallet
	nft_addresses = [request.wallet]
	nft_list = []
	
	for address in nft_addresses:
		nft_metadata = BLOCKCHAIN_API_RESOURCE.get_nft_metadata(
			mint_address=address,
			network=SolanaNetwork.MAINNET_BETA
		)
		nft_list.append(SolanaNFT(address, nft_metadata))

	for i in range(10):
		nft_list.append(nft_list[0])

	return SearchResponse(nft_list)
