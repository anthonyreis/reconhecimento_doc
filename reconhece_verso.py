import os
import cv2 as cv


def reconhece_verso(doc_path, name):
    imgVerso = cv.imread(doc_path)

    height, width, channels = imgVerso.shape

    tam_registro_inicial = height * 0.117
    tam_registro_final = (height * 0.117) + (height * 0.1)
    pos_inicial_registro = width * 0.135
    pos_final_registro = width * 0.513

    cv.imwrite(f'imgRegistro{name}.png', imgVerso[int(tam_registro_inicial):int(
        tam_registro_final), int(pos_inicial_registro):int(pos_final_registro)])

    tam_nome_inicial = height * 0.21
    tam_nome_final = (height * 0.21) + (height * 0.09)
    pos_inicial_nome = width * 0.04
    pos_final_nome = width * 0.795

    cv.imwrite(f'imgNome{name}.png', imgVerso[int(tam_nome_inicial):int(
        tam_nome_final), int(pos_inicial_nome):int(pos_final_nome)])

    tam_filiacao_inicial = height * 0.34
    tam_filiacao_final = (height * 0.34) + (height * 0.155)
    pos_inicial_filiacao = width * 0.04
    pos_final_filiacao = width

    cv.imwrite(f'imgFiliacao{name}.png', imgVerso[int(tam_filiacao_inicial):int(
        tam_filiacao_final), int(pos_inicial_filiacao):int(pos_final_filiacao)])

    tam_naturalidade_inicial = height * 0.52
    tam_naturalidade_final = (height * 0.52) + (height * 0.08)
    pos_inicial_naturalidade = width * 0.04
    pos_final_naturalidade = width * 0.536

    cv.imwrite(f'imgNaturalidade{name}.png', imgVerso[int(tam_naturalidade_inicial):int(
        tam_naturalidade_final), int(pos_inicial_naturalidade):int(pos_final_naturalidade)])

    tam_cpf_inicial = height * 0.72
    tam_cpf_final = (height * 0.72) + (height * 0.117)
    pos_inicial_cpf = width * 0.04
    pos_final_cpf = width * 0.497

    cv.imwrite(f'imgCpf{name}.png', imgVerso[int(tam_cpf_inicial):int(
        tam_cpf_final), int(pos_inicial_cpf):int(pos_final_cpf)])

    tam_nascimento_inicial = height * 0.51
    tam_nascimento_final = (height * 0.51) + (height * 0.104)
    pos_inicial_nascimento = width * 0.61
    pos_final_nascimento = width

    cv.imwrite(f'imgNascimento{name}.png', imgVerso[int(tam_nascimento_inicial):int(
        tam_nascimento_final), int(pos_inicial_nascimento):int(pos_final_nascimento)])

    tam_expedicao_inicial = height * 0.12
    tam_expedicao_final = (height * 0.135) + (height * 0.09)
    pos_inicial_expedicao = width * 0.53
    pos_final_expedicao = width

    cv.imwrite(f'imgExpedicao{name}.png', imgVerso[int(tam_expedicao_inicial):int(
        tam_expedicao_final), int(pos_inicial_expedicao):int(pos_final_expedicao)])
