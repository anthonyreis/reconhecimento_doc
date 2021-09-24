import pytesseract
from pytesseract.pytesseract import Output
import cv2 as cv
import re
import os


def reconhece_texto(name):
    words = ''
    date_params = ['Nascimento', 'Expedicao']
    allData = {}

    file_names = [f'imgAssinatura{name}Filter', f'imgGoverno{name}Filter', f'imgRegistro{name}', f'imgNome{name}Filter',
                  f'imgFiliacao{name}Filter', f'imgNaturalidade{name}Filter', f'imgCpf{name}Filter', f'imgNascimento{name}', f'imgExpedicao{name}']

    for file in file_names:
        image = cv.imread(f'{file}.png')

        custom_config = r'--oem 3 --psm 7'

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

        details = pytesseract.image_to_data(
            image, output_type=Output.DICT, config=custom_config, lang='por')

        total_boxes = len(details['text'])

        for sequence_number in range(total_boxes):
            if int(int(float(details['conf'][sequence_number]))) > 50:
                words += details['text'][sequence_number] + ' '

        field_name = re.split('\d', file)[0][3:]
        
        if field_name in date_params:
            words = re.sub('[^\d/]', '', words)

        elif field_name == 'Registro':
            words = re.sub('[^\d\w\.\-]', '', words)
            
        allData[field_name] = words
        words = ''
        
        os.remove(f'{file}.png')
    
    print(allData)   
