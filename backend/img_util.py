import cloudinary
import cloudinary.uploader
import cloudinary.utils

from io import BytesIO
from PIL import Image as PilImage 
import requests

#-----------------------------------------------------------------------

# Cloudinary configuration.
cloudinary.config( 
  cloud_name = "dskvzlrpw", 
  api_key = "126823135136982", 
  api_secret = "fYxRRjhC4_C2GVteU65f_QRKh94" 
)

#-----------------------------------------------------------------------

# Image object.
class Image:
    # Constructs an image from a URL.  
    def __init__(self):
        self.img = None
        self.w = None
        self.h = None

    # Generates an image with the given size and color (and color mode).
    def generate(self, size, color=0, mode="RGB"):
        self.img = PilImage.new(mode, size, color)
        (self.w, self.h) = size

    # Loads image from a URL.
    def load(self, url):
        response = requests.get(url)
        self.img = PilImage.open(BytesIO(response.content))
        (self.w, self.h) = self.img.size

    # Loads image from a path.
    def open(self, path):
    	self.img = PilImage.open(path)
    	(self.w, self.h) = self.img.size

    # Rescale the dimensions of the image by scale.
    def rescale(self, scale):
        self.w = round(scale * self.w)
        self.h = round(scale * self.h)
        self.img = self.img.resize((self.w, self.h))

    # Overlays other images on top of the image.
    # TODO: This function assumes that all images in others are the
    #       same size. We need to address how we handle differently
    #       shaped images.
    def overlay(self, others):
        n = len(others)
        padding = round((self.w - n * others[0].w) / (n + 1))
        height = round((self.h - others[0].h) / 2)
        for i, other in enumerate(others):
            width = (i + 1) * padding + i * other.w
            coords = (width, height)
            self.img.paste(other.img, coords)

    # Uploads the image and returns its URL. 
    def upload(self):
        img_bytes = BytesIO()
        self.img.save(img_bytes, format="PNG")
        response = cloudinary.uploader.upload(img_bytes.getvalue())
        # url = cloudinary.utils.private_download_url(response["public_id"], "png")
        return response["url"]

#-----------------------------------------------------------------------

# Request for the creation of a gallery image.
class GalleryRequest:
    # Constructs a request containing a list of images.
    def __init__(self, nft_imgs, background_img=None):
        self.nft_imgs = nft_imgs
        self.background_img = background_img

    # Returns the list of NFT images.
    def get_nft_imgs(self):
        return self.nft_imgs

    # Returns the background image.
    def get_background_img(self):
        return self.background_img

#-----------------------------------------------------------------------

# Response containing a gallery image.
class GalleryResponse:
    # Constructs a response from a gallery image.
    def __init__(self, img):
        self.img = img

    # Returns the gallery image.
    def get_gallery(self):
        return self.img
