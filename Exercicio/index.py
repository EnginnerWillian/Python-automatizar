import os

"""Esse environ serve para entrar em pastas"""
sistema = os.environ  

"""os.getcwd Serve para saber onde estamos navegando."""
print(os.getcwd())

novo_caminho =  '/Users/w1661an/Documents'

os.chdir(novo_caminho)
print(os.getcwd())

"entre em uma pasta e mostra um arquivo"

for root, dirs, file in os.walk("/Users/w1661an/Documents"):
    print(root)

print(os.getcwd())

os.path.basename(os.getcwd())
caminho1 = "/Users/w1661an/Documents"
caminho2 = "/Users/w1661an/Documents/Python"

print(os.path.commonprefix([caminho1, caminho2]))