import json
from sys import stderr

from .solana_util import SearchResponse, SolanaNFT
from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork

#-----------------------------------------------------------------------

# Blockchain API key pair
MY_API_KEY_ID = "pvFe4YVTcQxmgzS"
MY_API_SECRET_KEY = "1ftzweRMXGxPLWo"
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
	api_key_id=MY_API_KEY_ID,
	api_secret_key=MY_API_SECRET_KEY
)

#-----------------------------------------------------------------------

# Helper function to parse errors.
def parse_err(ex):
	err_message = "A server error has occurred."
	if "run out" in ex:
		err_message = "Cannot process call to blockchain."
	elif "value for public_key" in ex:
		err_message = "The specified wallet number could not be found."
	elif "[test]" in ex:
		err_message = ex[:-6]  # Remove [test] tag.
	return err_message

#-----------------------------------------------------------------------

# Helper function to filter out non-Solien NFTs.
def query_soliens(nft_addresses):
	with open('cache/solien_addresses.json') as solien_address:
	    soliens = json.load(solien_address)
	solien_addresses = [nft for nft in nft_addresses if nft in soliens]
	return solien_addresses

#-----------------------------------------------------------------------

# Returns the NFTs owned by the wallet in a given SearchRequest.
def search(request):
	# Retrieve the NFTs from the given wallet.
	try:
		# Hard-coded error.
		if request.wallet == "error":
			raise Exception("Error Message.[test]")

		# Hard-coded general use case.
		if request.wallet == "aaron":
			nft_list = []
			address = "FN8EXxCE8Nty5h6iNtfdN8tqmCwFYiSuM6j8bLa9Uc5h"
			metadata = {
				"image": "https://ipfs.io/ipfs/QmXiDcEu27TeBo2seYDuy81xtKmeYk3QUtjinNEnhpgReU",
				"data": {
					"name": "Solien #582",
					"uri": "https://ipfs.io/ipfs/QmSTf4BPk56ozEFwDotw18Zg79Ku6Cm7GjuQmB27pGwrsm",
					"mint": "FN8EXxCE8Nty5h6iNtfdN8tqmCwFYiSuM6j8bLa9Uc5h"
				}
			}

			for i in range(10):
				nft_list.append(SolanaNFT(address, metadata))

			return SearchResponse(nft_list)

		# Retrieve the NFTs via a call to the Blockchain API.
		# Examples:
		#    "Kycg1YrNJ9ezMBErReAJJmHWVtVCaYEdvJbMBC1xhvm"  (aaron)
		#    "6KQDNrJoPJRa1UHX7C4Wf5FHgjvnswLMTePyUTySFKeQ" (other)

		public_key = request.wallet
		nft_addresses = BLOCKCHAIN_API_RESOURCE.get_nfts_belonging_to_address(
			public_key,
			network=SolanaNetwork.MAINNET_BETA
		)

	except Exception as ex:
		print(ex, file=stderr)
		error_message = parse_err(str(ex))
		raise Exception(error_message)

	# Return the Solien NFTs.
	try:
		# Filter out non-Solien NFT addresses.
		solien_addresses = query_soliens(nft_addresses)

		# Return the NFTs as custom objects in a SearchResponse.
		nft_list = []

		for address in solien_addresses:
			# Retrieve the metadata at the given address via a call to
			# the Blockchain API.
			# nft_metadata = BLOCKCHAIN_API_RESOURCE.get_nft_metadata(
			# 	mint_address=address,
			# 	network=SolanaNetwork.MAINNET_BETA
			# )
			cached_nft_location = "cache/soliens/" + address + ".json"
			with open(cached_nft_location) as metadata_json:
			    metadata = json.load(metadata_json)
			nft_list.append(SolanaNFT(address, metadata))
		return SearchResponse(nft_list)

	except Exception as ex:
		print(ex, file=stderr)
		error_message = parse_err(str(ex))
		raise Exception(error_message)
