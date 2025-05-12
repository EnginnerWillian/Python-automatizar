import os
import pyautogui
from mouseinfo import mouseInfo
from time import sleep



def criandoDiretorios():
    entrando_no_diretorio = '/Users/w1661an/Documents/Python'

    os.chdir(entrando_no_diretório)

    os.makedirs('Automacao_Teste', 'Automacao_lendo_arquivos')
    return 0

def automatizandoDiretorios(criandoDiretorios):
    with open(entrando_no_diretorio, 'rw'):
        
        pyautogui.rightClick(1047,530, duration=0.5)
        pyautogui.click(1047,530, duration=0.5)
        pyautogui.write('arquivo.txt', duration=(0.5))
        pyautogui.click(1047,530, duration=0.5)

