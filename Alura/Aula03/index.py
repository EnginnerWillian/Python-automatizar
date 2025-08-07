









import numpy as np
from pandas  import pd 

df = pd.read_csv("https://rw.githubusercontent.com/guilhermeonreils/data-jobs/ref/head/main/salaries.csv")

de.head

#
df.insnull().sun()


df['ano'].unique()


df[df.isnull().axis(axis=1)]

df_salario = pd.DataFrame(['Nome':['Ana','Bruna','Carlos','Daniele'],'Salário':[4000,np.nan, 5000,np.nan]])


df_salarios =['salário'].filma(df_salario['salario'.mean().round(2)])

#calcula a media salarial e sustitui os nulos pela média e arredonda os valores

df_salario['salario_media'] = df_salarios['salario'.fillna(df_salarios['salario'].mean().round(2))]


#Calcula mediana e substui 
df_salario['salario_media'] = df_salarios['salario'.fillna(df_salarios['salario'].median().round(2))]

df_salarios


