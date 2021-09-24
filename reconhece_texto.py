import pytesseract
from pytesseract.pytesseract import Output
import cv2 as cv


def reconhece_texto():
    words = []

    image = cv.imread('imgExpedicaoEqUnsharp.png')

    # configuring parameters for tesseract

    custom_config = r'--oem 3 --psm 6'

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    #print(pytesseract.image_to_string(image=threshold_img, lang='por'))

    details = pytesseract.image_to_data(
        image, output_type=Output.DICT, config=custom_config, lang='por')

    print(details.keys())
    print(details['text'])
    print(details['conf'])
    # print(pytesseract.image_to_string(r'C:\Users\User\Desktop\imagens_rg\frente\img16.png'))

    total_boxes = len(details['text'])
    
    for sequence_number in range(total_boxes):
        if int(int(float(details['conf'][sequence_number]))) > 50:
            words.append(details['text'][sequence_number])
           
            (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number],
                            details['width'][sequence_number],  details['height'][sequence_number])

            gray_image = cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv.imshow('captured text', gray_image)
    print(words)

    cv.waitKey(0)

    cv.destroyAllWindows()
