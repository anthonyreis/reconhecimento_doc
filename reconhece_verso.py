import os
import cv2 as cv


def reconhece_verso(doc_path):
    imgVerso = cv.imread(doc_path)

    height, width, channels = imgVerso.shape

    tam_registro_inicial = height * 0.117
    tam_registro_final = (height * 0.117) + (height * 0.1)
    pos_inicial_registro = width * 0.135
    pos_final_registro = width * 0.513

    #cv.rectangle(imgVerso, (int(pos_inicial_registro), int(tam_registro_inicial)), (int(pos_final_registro), int(tam_registro_final)), (255, 0, 0), 2)
    cv.imwrite('imgRegistro.png', imgVerso[int(tam_registro_inicial):int(
        tam_registro_final), int(pos_inicial_registro):int(pos_final_registro)])

    tam_nome_inicial = height * 0.21
    tam_nome_final = (height * 0.21) + (height * 0.09)
    pos_inicial_nome = width * 0.04
    pos_final_nome = width * 0.795

    #cv.rectangle(imgVerso, (int(pos_inicial_nome), int(tam_nome_inicial)), (int(pos_final_nome), int(tam_nome_final)), (255, 0, 0), 2)
    cv.imwrite('imgNome.png', imgVerso[int(tam_nome_inicial):int(
        tam_nome_final), int(pos_inicial_nome):int(pos_final_nome)])

    tam_filiacao_inicial = height * 0.34
    tam_filiacao_final = (height * 0.34) + (height * 0.155)
    pos_inicial_filiacao = width * 0.04
    pos_final_filiacao = width

    #cv.rectangle(imgVerso, (int(pos_inicial_filiacao), int(tam_filiacao_inicial)), (int(pos_final_filiacao), int(tam_filiacao_final)), (255, 0, 0), 2)
    cv.imwrite('imgFiliacao.png', imgVerso[int(tam_filiacao_inicial):int(
        tam_filiacao_final), int(pos_inicial_filiacao):int(pos_final_filiacao)])

    tam_naturalidade_inicial = height * 0.52
    tam_naturalidade_final = (height * 0.52) + (height * 0.08)
    pos_inicial_naturalidade = width * 0.04
    pos_final_naturalidade = width * 0.536

    #cv.rectangle(imgVerso, (int(pos_inicial_naturalidade), int(tam_naturalidade_inicial)), (int(pos_final_naturalidade), int(tam_naturalidade_final)), (255, 0, 0), 2)
    cv.imwrite('imgNaturalidade.png', imgVerso[int(tam_naturalidade_inicial):int(
        tam_naturalidade_final), int(pos_inicial_naturalidade):int(pos_final_naturalidade)])

    tam_cpf_inicial = height * 0.72
    tam_cpf_final = (height * 0.72) + (height * 0.117)
    pos_inicial_cpf = width * 0.04
    pos_final_cpf = width * 0.497

    #cv.rectangle(imgVerso, (int(pos_inicial_cpf), int(tam_cpf_inicial)), (int(pos_final_cpf), int(tam_cpf_final)), (255, 0, 0), 2)
    cv.imwrite('imgNaturalidade.png', imgVerso[int(tam_cpf_inicial):int(
        tam_cpf_final), int(pos_inicial_cpf):int(pos_final_cpf)])

    tam_nascimento_inicial = height * 0.51
    tam_nascimento_final = (height * 0.51) + (height * 0.104)
    pos_inicial_nascimento = width * 0.61
    pos_final_nascimento = width

    #cv.rectangle(imgVerso, (int(pos_inicial_nascimento), int(tam_nascimento_inicial)), (int(pos_final_nascimento), int(tam_nascimento_final)), (255, 0, 0), 2)
    cv.imwrite('imgNascimento.png', imgVerso[int(tam_nascimento_inicial):int(
        tam_nascimento_final), int(pos_inicial_nascimento):int(pos_final_nascimento)])

    tam_expedicao_inicial = height * 0.12
    tam_expedicao_final = (height * 0.135) + (height * 0.09)
    pos_inicial_expedicao = width * 0.53
    pos_final_expedicao = width

    #cv.rectangle(imgVerso, (int(pos_inicial_expedicao), int(tam_expedicao_inicial)), (int(pos_final_expedicao), int(tam_expedicao_final)), (255, 0, 0), 2)
    cv.imwrite('imgExpedicao.png', imgVerso[int(tam_expedicao_inicial):int(
        tam_expedicao_final), int(pos_inicial_expedicao):int(pos_final_expedicao)])

    #cv.imshow('docVerso', imgVerso)

    cv.waitKey(0)
