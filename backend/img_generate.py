from .img_util import GalleryResponse, Image

#-----------------------------------------------------------------------

# Generates a gallery from a GalleryRequest and returns its URL.
def generate_gallery(request):
    # Parse the request.
    nft_imgs = request.get_nft_imgs()
    background_img = request.get_background_img()
    if background_img == None:
        background_img = Image()
        background_img.generate((1500, 500), color=0xf8f9fa)

    # Rescale the NFT images.
    for img in nft_imgs:
        img.rescale(0.225)

    # Generate and upload the gallery image.
    background_img.overlay(nft_imgs)
    url = background_img.upload()

    # Return the URL of the new image.
    return url
