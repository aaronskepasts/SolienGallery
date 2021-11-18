from .solana_util import SearchResponse, SolanaNFT, query_soliens
from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork

#-----------------------------------------------------------------------

# Blockchain API key pair
MY_API_KEY_ID = "q9C1d3NR20jwsC9"
MY_API_SECRET_KEY = "AfKXGyXlYxNOb6T"
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
	api_key_id=MY_API_KEY_ID,
	api_secret_key=MY_API_SECRET_KEY
)

#-----------------------------------------------------------------------

def search(request):
	if request.wallet == "aaron":
		nft_list = []
		address = "FN8EXxCE8Nty5h6iNtfdN8tqmCwFYiSuM6j8bLa9Uc5h"
		metadata = {
			"data": { 
				"name": "Solien #582", 
				"uri": "https://ipfs.io/ipfs/QmSTf4BPk56ozEFwDotw18Zg79Ku6Cm7GjuQmB27pGwrsm",
				"mint": "FN8EXxCE8Nty5h6iNtfdN8tqmCwFYiSuM6j8bLa9Uc5h"
			}
		}

		for i in range(10):
			nft_list.append(SolanaNFT(address, metadata))

		return "", SearchResponse(nft_list)

	# get all NFTs from given wallet
	# e.g. public_key = "Kycg1YrNJ9ezMBErReAJJmHWVtVCaYEdvJbMBC1xhvm"
	# good public_key = "6KQDNrJoPJRa1UHX7C4Wf5FHgjvnswLMTePyUTySFKeQ"
	public_key = request.wallet
	try:
		nft_addresses = BLOCKCHAIN_API_RESOURCE.get_nfts_belonging_to_address(
			public_key,
			network=SolanaNetwork.MAINNET_BETA
		)
	except Exception as ex:
		if "You have run out" in str(ex):
				error_message = "Cannot process call to blockchain."
		else:
			error_message = "The specified wallet number could not be found."
		return error_message, SearchResponse([])

	# filter out non-Solien NFTs
	# fill in this list
	solien_addresses = query_soliens(nft_addresses)

	# create nft objects by searching for metadata at each address
	# populate nft_list to be converted into a response and returned
	nft_list = []
	for address in solien_addresses:
		try:
			nft_metadata = BLOCKCHAIN_API_RESOURCE.get_nft_metadata(
				mint_address=address,
				network=SolanaNetwork.MAINNET_BETA
			)
			nft_list.append(SolanaNFT(address, nft_metadata))
		except Exception as ex:
			if "You have run out" in str(ex):
				error_message = "Cannot process call to blockchain."
			else:
				error_message = "Issue encountered when retrieving an NFT's metadata."
			return error_message, SearchResponse([])

	return "", SearchResponse(nft_list)
