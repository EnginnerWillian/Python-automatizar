import pyautogui
from time import sleep
from mouseinfo import mouseInfo

#Usando pyautogui para clicar e escrever automaticamente no banco de dados o nome de usuário
pyautogui.click(1295,542, duration=2)
pyautogui.write('Willian')
#Usando pyautogui para clicar e escrever automaticamente no banco de dados a senha de usuário
pyautogui.click(1296,548, duration=2)
pyautogui.write('123456')

#Usando pyautogui para clicar automaticamente  em registrar no banco de dados 
pyautogui.click(1190,595 , duration=2)

#Criando um loop de repetição para escolher o produto, quantidade e preço
with open('Clientes e Pedidos/Clientes e Pedidos.xlsx','r') as arquivo:
    for linha in arquivo:
        produto =  linha.split(',')[0]
        quantidade =  linha.split(',')[1]
        preco =  linha.split(',')[2]

#Usando pyautogui para clicar e escrever automaticamente no banco de dados o nome de produto,quantidade e preço
        pyautogui.click(1047,530, duration=0.5)
        pyautogui.write('Produto')

        pyautogui.click(1042,554,duration=0.5)
        pyautogui.write('Quantidade')
        
        pyautogui.click(1034,580, duration=0.5)
        pyautogui.write('preco')
        
        

