import json
from sys import stderr
from .solana_util import SearchResponse, SolanaNFT
from theblockchainapi import TheBlockchainAPIResource, SolanaNetwork
import urllib.request

#-----------------------------------------------------------------------

# Blockchain API key pair (keep thease secret)
MY_API_KEY_ID = "YOUR KEY HERE"
MY_API_SECRET_KEY = "YOUR KEY HERE"
BLOCKCHAIN_API_RESOURCE = TheBlockchainAPIResource(
	api_key_id=MY_API_KEY_ID,
	api_secret_key=MY_API_SECRET_KEY
)

#-----------------------------------------------------------------------

# Helper function to parse errors.
def parse_err(ex):
	assert(ex != None)
	err_message = "A server error has occurred."
	if "run out" in ex:
		err_message = "Cannot process call to blockchain."
	elif "value for public_key" in ex:
		err_message = "The specified wallet number could not be found."
	elif "[test]" in ex:
		err_message = ex[:-6]  # Remove [test] tag.
	elif "no Solien" in ex:
		err_message = "Wallet contains no Solien NFTs."
	return err_message

#-----------------------------------------------------------------------

# Helper function to filter out non-Solien NFTs.
def query_soliens(nft_addresses):
	assert(nft_addresses != None)
	with open('cache/solien_addresses.json') as solien_address:
		soliens = json.load(solien_address)
	solien_addresses = [nft for nft in nft_addresses if nft in soliens]
	return solien_addresses

#-----------------------------------------------------------------------

# get data (with image field) given metadata
def get_data_from_url(data_url):
    assert(data_url)
    with urllib.request.urlopen(data_url) as url:
        data = json.loads(url.read().decode())
        return(data)

#-----------------------------------------------------------------------

# Returns the NFTs owned by the wallet in a given SearchRequest.
def search(request):
	assert(request != None)
	# Retrieve the NFTs from the given wallet.
	try:
		# Hard-coded test error.
		if request.wallet == "error":
			raise Exception("Error Message.[test]")

		# Hard-coded test wallet.
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

		# Retrieve the NFTs in wallet via a call to the Blockchain API.
		# Example wallet public_key:
		#   "Kycg1YrNJ9ezMBErReAJJmHWVtVCaYEdvJbMBC1xhvm"  (Aaron's Wallet)

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

		# Raise exception if no Solien addresses in wallet
		if len(solien_addresses) == 0:
			error_message = "Wallet contains no Solien NFTs"
			raise Exception(error_message)

		# Return the NFTs as custom objects in a SearchResponse.
		nft_list = []

		# 4SU7eEW4ELxE4At9TZ1ftNT8wvXLKA8p6yR2bc3bc86R is not cached Solien NFT
		not_cached = "4SU7eEW4ELxE4At9TZ1ftNT8wvXLKA8p6yR2bc3bc86R"

		for address in solien_addresses:
			# If NFT is not cached, retrieve metadata from blockchain
			if address == not_cached:
				metadata = BLOCKCHAIN_API_RESOURCE.get_nft_metadata(
					mint_address=address,
					network=SolanaNetwork.MAINNET_BETA
				)

				# get data from metadata which contains the image field
				metadata = get_data_from_url(metadata['data']['uri'])
				tempNFT = SolanaNFT(address, metadata)

			# If NFT is cached, retrieve metadata from cache
			else:
				cached_nft_location = "cache/soliens/" + address + ".json"
				with open(cached_nft_location) as metadata_json:
					metadata = json.load(metadata_json)
				tempNFT = SolanaNFT(address, metadata)

			nft_list.append(tempNFT)

		return SearchResponse(nft_list)

	except Exception as ex:
		print(ex, file=stderr)
		error_message = parse_err(str(ex))
		raise Exception(error_message)
