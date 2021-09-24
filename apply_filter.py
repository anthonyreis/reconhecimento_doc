from PIL import Image, ImageFilter, ImageOps
import os


def apply_filter(name):
    file_names = [f'imgAssinatura{name}', f'imgGoverno{name}', f'imgNome{name}',
                  f'imgFiliacao{name}', f'imgNaturalidade{name}', f'imgCpf{name}']
    
    for file in file_names:
        image = Image.open(f'{file}.png')

        gray_image = ImageOps.grayscale(image)

        eq_img = ImageOps.equalize(gray_image, mask=None)

        unsharp_img = eq_img.filter(ImageFilter.UnsharpMask(radius=3, percent=150))

        os.remove(f'{file}.png')
        
        unsharp_img.save(f'{file}Filter.png')
