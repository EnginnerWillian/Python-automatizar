from pandas import pd
from metplotlib import plt
import seabornß 








#Gráficos de torta
remote_contagens = df_limpo     ['remoto'_value_counts().reset_index()]
remote_contagens.columns ['tipo_trabalho', 'quatidades']


fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
title='Proporção dos tipos de  trabalho'
)


#Gráfico de barras

df_lipo['senioridade'.value_counts().plot(kind='bar',title="Distruibuição de seneriodade")]

