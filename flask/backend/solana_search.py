from .solana_util import SearchResponse, SolanaNFT, only_soliens
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

def search(request):
	try:
		assert MY_API_KEY_ID is not None
		assert MY_API_SECRET_KEY is not None
	except AssertionError:
		raise Exception("API keypair is broken")


	# get all NFTs from given wallet
	# e.g. public_key = "Kycg1YrNJ9ezMBErReAJJmHWVtVCaYEdvJbMBC1xhvm"
	public_key = request.wallet
	nfts = BLOCKCHAIN_API_RESOURCE.get_nfts_belonging_to_address(
		public_key,
		network=SolanaNetwork.MAINNET_BETA
	)
		

	# filter out non-Solien NFTs
	# fill in this list
	nfts = only_soliens(nfts)

	# create nft objects by searching for metadata at each address
	# populate nft_list to be converted into a response and returned
	nft_list = []
	for address in nfts:
		nft_metadata = BLOCKCHAIN_API_RESOURCE.get_nft_metadata(
			mint_address=address,
			network=SolanaNetwork.MAINNET_BETA
		)
		nft_list.append(SolanaNFT(address, nft_metadata))

	return SearchResponse(nft_list)

