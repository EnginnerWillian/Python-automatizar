import pyodbc

dados_conexao = (
    "Driver={SQL SERVER};"
    "SERVER=MacBook-Pro-de-Rafael-Azambuja.local;"
    "Database=PYTHONSQL;"
)

conexap = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")

cursor = conexao.cursor()

id = 3
cliente = "Lira Python"
produto "Carro"
data = "25/08/2021"
preco = "50000"
quantidade = 1                  
comando = """"INSERT INTO VENDAS (id_vendas, cliente, produto, data_venda)
                                                                                                                                                                                                                                VALUES
    INSERT INTO VENDAS (id_vendas, cliente, produto, data_venda)
VALUES
    (1,'Alon', 'Iphone', '15/02/2021', 6000, 1)    
""""

cursor.execute(comando)
cursor.commit() 
