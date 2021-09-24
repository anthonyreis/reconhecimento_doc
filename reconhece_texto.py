import pytesseract
from pytesseract.pytesseract import Output
import cv2 as cv

words = []

# importing modules

# reading image using opencv

image = cv.imread('imgExpedicaoEqUnsharp.png')

#configuring parameters for tesseract

custom_config = r'--oem 3 --psm 6'

# now feeding image to tesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

#print(pytesseract.image_to_string(image=threshold_img, lang='por'))

details = pytesseract.image_to_data(image, output_type=Output.DICT, config=custom_config, lang='por')

print(details.keys())
print(details['text'])
print(details['conf'])
#print(pytesseract.image_to_string(r'C:\Users\User\Desktop\imagens_rg\frente\img16.png'))

total_boxes = len(details['text'])
i = 0
for sequence_number in range(total_boxes):
    if int(int(float(details['conf'][sequence_number]))) > 50:
            words.append(details['text'][sequence_number])
            i += 1
            (x, y, w, h) = (details['left'][sequence_number], details['top'][sequence_number], details['width'][sequence_number],  details['height'][sequence_number])

            gray_image = cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# display image

cv.imshow('captured text', gray_image)
print(words)

# Maintain output window until user presses a key

cv.waitKey(0)

# Destroying present windows on screen

cv.destroyAllWindows()
