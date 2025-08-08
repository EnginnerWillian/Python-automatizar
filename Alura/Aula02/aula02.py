








import pandas as pd

                                    df = pd.read_csv("https://rw.githubusercontent.com/guilhermeonreils/data-jobs/ref/head/main/salaries.csv")
df.head()
df.info()
df.descrier(            )


#Mostra as colunas e linhas
df.shape()

linhas, colunas =df.shape("0", df.shape(1))
print("Linhas:", linhas)
print("Colunas: ", colunas)


df.columns

df.raname(columns=_renoamear, inplace=True)
df["nivel_experiencia"].value_counts()
df.columns






