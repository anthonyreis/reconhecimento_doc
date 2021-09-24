from PIL import Image, ImageFilter, ImageOps


def apply_filter(img_path):
    image = Image.open(img_path)

    gray_image = ImageOps.grayscale(image)

    eq_img = ImageOps.equalize(gray_image, mask=None)

    unsharp_img = eq_img.filter(ImageFilter.UnsharpMask(radius=3, percent=150))

    unsharp_img.save('imgExpedicaoEqUnsharp.png')
