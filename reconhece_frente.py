import os
import cv2 as cv
import reconhece_verso

def reconhece_frente(doc_path, name):
    imgFrente = cv.imread(doc_path)

    height, width, channels = imgFrente.shape

    tam_governo_inicial = height * 0.088
    tam_governo_final = (height * 0.11) + (height * 0.052)
    lateral_esquerda_governo = width * 0.27
    lateral_direita_governo = (width * 0.27) + (width * 0.6)

    cv.imwrite(f'imgGoverno{name}.png', imgFrente[int(tam_governo_inicial):int(
        tam_governo_final), int(lateral_esquerda_governo):int(lateral_direita_governo)])

    tam_centro_inicio = height * 0.26
    tam_centro_final = (height * 0.26) + (height * 0.44)
    tam_foto_inicial = width * 0.5
    tam_foto_final = (width * 0.5) + (width * 0.4)

    cv.imwrite(f'imgFoto{name}.png', imgFrente[int(tam_centro_inicio):int(
        tam_centro_final), int(tam_foto_inicial):int(tam_foto_final)])

    tam_assinatura_inicial = height * 0.72
    tam_assinatura_final = (height * 0.76) + (height * 0.125)
    dist_lateral_esquerda = width * 0.09
    dist_lateral_direita = (width * 0.09) + (width * 0.8075)

    #cv.rectangle(imgFrente, (int(dist_lateral_esquerda), int(tam_assinatura_inicial)), (int(dist_lateral_direita), int(tam_assinatura_final)), (255, 0, 0), 2)
    cv.imwrite(f'imgAssinatura{name}.png', imgFrente[int(tam_assinatura_inicial):int(
        tam_assinatura_final), int(dist_lateral_esquerda):int(dist_lateral_direita)])
