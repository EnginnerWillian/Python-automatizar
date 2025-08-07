# Aplicando conceitos de programação de dados com Biblioteca Pandas









from pandas import pd


df = pd.Dataframe()



dados = {'Recibimento': ['R$1000', 'R$15'],
         'Gastos':['R$550', 'R$45', 'R$30']}


df['Recibemento'] = df['Recebimento'].str.replace('R$', '', regex=False).a
df ['Gastos'] = df['Gastos'].str.replace('R$', '', regex=False).astype(float)


print(df)


pd.df(dados)
                    