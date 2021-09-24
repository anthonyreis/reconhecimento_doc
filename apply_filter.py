import cv2 as cv
from PIL import Image, ImageFilter, ImageOps

image = Image.open('imgExpedicao.png')

gray_image = ImageOps.grayscale(image)

eq_img = ImageOps.equalize(gray_image, mask=None)

unsharp_img = eq_img.filter(ImageFilter.UnsharpMask(radius=3, percent=150))

unsharp_img.save('imgExpedicaoEqUnsharp.png')

cv.waitKey(0)