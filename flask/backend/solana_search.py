from .solana_util import SearchResponse, SolanaNFT, query_soliens
from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork

#-----------------------------------------------------------------------

# Blockchain API key pair
MY_API_KEY_ID = "j5I8K5JRLdm1G5e"
MY_API_SECRET_KEY = "4TWbSQge5IthbcW"
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
	api_key_id=MY_API_KEY_ID,
	api_secret_key=MY_API_SECRET_KEY
)

#-----------------------------------------------------------------------

def search(request):
	try:
		assert MY_API_KEY_ID is not None
		assert MY_API_SECRET_KEY is not None
	except AssertionError:
		raise Exception("API keypair is broken")


	# get all NFTs from given wallet
	# e.g. public_key = "Kycg1YrNJ9ezMBErReAJJmHWVtVCaYEdvJbMBC1xhvm"
	# good public_key = "6KQDNrJoPJRa1UHX7C4Wf5FHgjvnswLMTePyUTySFKeQ"
	public_key = request.wallet
	nft_addresses = BLOCKCHAIN_API_RESOURCE.get_nfts_belonging_to_address(
		public_key,
		network=SolanaNetwork.MAINNET_BETA
	)


	# filter out non-Solien NFTs
	# fill in this list
	solien_addresses = query_soliens(nft_addresses)

	# create nft objects by searching for metadata at each address
	# populate nft_list to be converted into a response and returned
	nft_list = []
	counter = 0
	for address in solien_addresses:
		nft_metadata = BLOCKCHAIN_API_RESOURCE.get_nft_metadata(
			mint_address=address,
			network=SolanaNetwork.MAINNET_BETA
		)
		nft_list.append(SolanaNFT(address, nft_metadata))
		# counter += 1
		# if counter == 2:
		# 	break

	return SearchResponse(nft_list)
