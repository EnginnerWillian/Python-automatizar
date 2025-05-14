import os
import pyautogui
from time import sleep

# Caminho base
diretorio_base = '/Users/w1661an/Documents/Python'

def criando_diretorios():
    os.chdir(diretorio_base)

    # Criando dois diretórios
    os.makedirs('Automacao_Teste', exist_ok=True)
    os.makedirs('Automacao_lendo_arquivos', exist_ok=True)

def automatizando_diretorios():
    # Exemplo de automatização — isso apenas demonstra cliques e escrita
    sleep(1)  # Tempo para o usuário focar na área correta, se necessário
    pyautogui.rightClick(1047, 530, duration=0.5)
    sleep(0.5)
    pyautogui.click(1047, 530, duration=0.5)
    pyautogui.write('arquivo.txt', duration=0.5)
    sleep(0.5)
    pyautogui.click(1047, 530, duration=0.5)

# Execução
criando_diretorios()
automatizando_diretorios()
