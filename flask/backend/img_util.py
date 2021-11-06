from imageio import imread, imwrite
import numpy as np

#-----------------------------------------------------------------------

# Image object.
class Image:
	# Constructs an image from a URL.  
	def __init__(self, img_url):
		# Take the first three RGB channels (discarding alpha channels).
		self.img = imread(img_url)[...,:3]

	# Returns the image.
	def get_img(self):
		return self.img

	# Merges two images horizontally.
	def hmerge(self, other):
		self.img = np.hstack((self.img, other.img))

	# Merges two images vertically.
	def vmerge(self, other):
		self.img = np.vstack((self.img, other.img))

	def save(self, filename):
		imwrite(filename, self.img)

#-----------------------------------------------------------------------

# Request for the creation of a gallery image.
class GalleryRequest:
	# Constructs a request containing a list of images.
	def __init__(self, img_list):
		self.img_list = img_list

	# Returns the number of images in the request.
	def get_size(self):
		return len(self.img_list)

	# Returns the image at index i.
	def get_img(self, i):
		return self.img_list[i]

#-----------------------------------------------------------------------

# Response containing a gallery image.
class GalleryResponse:
	# Constructs a response from a gallery image.
	def __init__(self, img):
		self.img = img

	# Returns the gallery image.
	def get_gallery(self):
		return img
