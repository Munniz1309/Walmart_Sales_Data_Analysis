import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import datetime 

df = pd.read_csv('Walmart.csv')

# Dataset agrupado por loja
dfNew = df.groupby('Store')

df.describe()
df.info()

# Transformando o dados da coluna date para tipo 'datetime'
df['Date'] = pd.to_datetime(df['Date'])
df['Week'] = pd.to_datetime(df['Date']).dt.week

# Soma de vendas semanais por loja
somaVendas = px.histogram(df, x= 'Store', y = 'Weekly_Sales', 
                          text_auto = True, 
                          histfunc = 'sum', 
                          title = 'Sum of weekly sales by store',
                          color_discrete_sequence = ['darkorange'], 
                          template="simple_white")
somaVendas.show()

# Média de venda semanais por lojas
mediaVendas = px.histogram(df, x= 'Store', y = 'Weekly_Sales', 
                           text_auto = True, 
                           histfunc = 'avg', 
                           title = 'Average weekly sales by store',
                           color_discrete_sequence=['darkorange'], 
                           template="simple_white")
mediaVendas.show()

# Média de vendas semanais por loja em feriados e dias normais
vendasComparacao = px.histogram(df, x = 'Store', y = 'Weekly_Sales',
             color = 'Holiday_Flag', 
             barmode = 'group',
             title = 'Average weekly sales by store on holidays and normal days',
             color_discrete_sequence = ['darkorange', 'black'], 
             template="simple_white",
             histfunc = 'avg')
vendasComparacao.show()

# Média da temperatura por loja
mediaTemperatura = px.histogram(df, x= 'Store', y = 'Temperature', 
                                text_auto = True, 
                                histfunc = 'avg', 
                                title = 'Average temperature by store',
                                color_discrete_sequence=['darkorange'], 
                                template="simple_white")
mediaTemperatura.show()

# Média de preço dos combustíveis por loja
mediaCombustivel = px.histogram(df, x= 'Store', y = 'Fuel_Price', 
                                text_auto = True, 
                                histfunc = 'avg',
                                title = 'Average fuel price by store',
                                color_discrete_sequence=['darkorange'], 
                                template="simple_white")
mediaCombustivel.show()

# Média do CPI por loja
mediaCPI = px.histogram(df, x= 'Store', y = 'CPI', 
                        text_auto = True, 
                        histfunc = 'avg',
                        title = 'Average CPI by store',
                        color_discrete_sequence=['darkorange'], 
                        template="simple_white")
mediaCPI.show()

# Média da taxa de desemprego por loja
mediaTaxaDesemprego = px.histogram(df, x= 'Store', y = 'Unemployment',
                                   text_auto = True, 
                                   histfunc = 'avg',
                                   title = 'Average unemployment rate by store',
                                   color_discrete_sequence=['darkorange'], 
                                   template="simple_white")
mediaTaxaDesemprego.show()

#Correlação
sns.heatmap(df.corr(), cmap = 'Oranges', annot = True)
plt.show()

# Semanas do ano que a loja 20 (loja com maior venda acumulada) ultrapassou a média dela própria
store20 = df.loc[(df.Store == 20)]
count = 0
for i in store20.Weekly_Sales:
  if i >= 2107677:
    count += 1  
print(count)

# Semanas do ano que a loja 20 (loja com maior venda acumulada) ultrapassou a média geral
store20 = df.loc[(df.Store == 20)]
count = 0
for i in store20.Weekly_Sales:
  if i >= 1046965:
    count += 1  
print(count)

# Descrição da loja 20
store20.describe()

#Semanas do ano que a loja 4 (loja escolhida) ultrapassou a média dela própria
store4 = df.loc[(df.Store == 4)]
count = 0
for i in store20.Weekly_Sales:
  if i >= 2094713:
    count += 1  
print(count)

# Semanas do ano que a loja 4 (loja escolhida) ultrapassou a média geral
store4 = df.loc[(df.Store == 4)]
count = 0
for i in store20.Weekly_Sales:
  if i >= 1046965:
    count += 1  
print(count)

# Descrição da loja 4
store4.describe()

dfNew.describe()

# loja escolhida
escolha = dfNew.loc[(dfNew.Weekly_Sales >= 1046965) & (dfNew.Unemployment <= 7.99) & (dfNew.CPI <= 171.57) & (dfNew.Temperature >= 60.66)]
print(escolha) 