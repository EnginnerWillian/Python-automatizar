import os
from time import sleep



def criando_diretorios():
    entrando_no_diretório = '/Users/w1661an/Documents/Python'

    os.chdir(entrando_no_diretório)

    os.makedirs('Automacao_Teste', 'Automacao_lendo_arquivos')
    return 0

