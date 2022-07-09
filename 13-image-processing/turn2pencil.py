import imageio
import matplotlib.pyplot as plt

img = "263697.20.jpg"
start_img = imageio.imread(img)
# start_img.shape(196, 160, 30)
import numpy as np


def grayscale(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])
gray_img = grayscale(start_img)
plt.imshow(gray_img, cmap='gray')
plt.show()
inverted_img = 255-gray_img

import scipy.ndimage
blur_img = scipy.ndimage.filters.gaussian_filter(inverted_img,sigma=5)
plt.imshow(blur_img, cmap='gray')
plt.show()
def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')
final_img= dodge(blur_img,gray_img)
plt.imshow(final_img, cmap='gray')
plt.show()