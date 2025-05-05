import os
"""Esse environ serve para entrar em pastas"""
sistema = os.environ  

"""os.getcwd Serve para saber onde estamos navegando."""
print(os.getcwd())

novo_caminho =  '/Users/w1661an/Documents'

os.chdir(novo_caminho)
print(os.getcwd())


"""Cria um arquivo dentro da pasta que estamos navegando"""
os.mkdir("Teste1 ")

print(os.listdir())



caminho = "/2021/janeiro/21/manha"
os.makedirs(caminho)
print(os.listdir())
os.rmdir(r"Teste1, Teste2")