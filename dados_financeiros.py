# -*- coding: utf-8 -*-
"""Dados_financeiros.ipynb

Dados financeiros
"""

#!pip install yfinance

"""## Importação das bibliotecas"""

import pandas as pd
import numpy as np
#from pandas_datareader import data
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import yfinance as yf

"""## Base de dados com uma ação"""

#gol_df = data.DataReader(name = 'GOLL4.SA', data_source='yahoo', start='2024-01-01')
gol_df = yf.download("GOLL4.SA", start='2024-01-01')

gol_df

gol_df.info()

gol_df.head(3)

gol_df.tail(3)

gol_df.describe()

# gol_df[gol_df['Close'] >= 43.79]
gol_df[gol_df[('Close', 'GOLL4.SA')] >= 43.79]

# gol_df[(gol_df['Close'] >= 1.15) & (gol_df['Close'] <= 1.16)]
gol_df[(gol_df[('Close', 'GOLL4.SA')] >= 1.15) & (gol_df[('Close', 'GOLL4.SA')] <= 1.16)]

gol_df.to_csv('gol.csv')

gol_df2 = pd.read_csv('/https://github.com/lj1981/Simulador-/tree/main/gol.csv')
gol_df2

"""## Base de dados com mais ações

- BOVA11: https://www.sunoresearch.com.br/artigos/bova11/
"""

acoes = ['GOLL4.SA', 'CVCB3.SA', 'WEGE3.SA', 'MGLU3.SA', 'TOTS3.SA', 'BOVA11.SA']

acoes_df = pd.DataFrame()
for acao in acoes:
  #acoes_df[acao] = data.DataReader(acao, data_source='yahoo', start='2015-01-01')['Close']
  acoes_df[acao] = yf.download(acao, start='2015-01-01')['Close']

acoes_df

acoes_df = acoes_df.rename(columns={'GOLL4.SA': 'GOL', 'CVCB3.SA': 'CVC', 'WEGE3.SA': 'WEGE',
                                    'MGLU3.SA': 'MGLU', 'TOTS3.SA': 'TOTS', 'BOVA11.SA': 'BOVA'})

acoes_df.columns[0:]

acoes_df.head()

acoes_df.isnull().sum()

acoes_df.shape

acoes_df.dropna(inplace=True)

acoes_df.shape

acoes_df.isnull().sum()

acoes_df.to_csv('acoes.csv')

acoes_df = pd.read_csv('https://github.com/lj1981/Simulador-/tree/main/acoes.csv')
acoes_df

acoes_df.columns[1:]

acoes_df.describe()

"""## Visualização"""

sns.histplot(acoes_df['GOL']);

len(acoes_df.columns)

np.arange(1, len(acoes_df.columns))

plt.figure(figsize=(10,50))
i = 1
for i in np.arange(1, len(acoes_df.columns)):
  plt.subplot(7, 1, i + 1)
  sns.histplot(acoes_df[acoes_df.columns[i]], kde = True)
  plt.title(acoes_df.columns[i])

acoes_df['GOL'].describe()

sns.boxplot(x = acoes_df['GOL']);

plt.figure(figsize=(10,50))
i = 1
for i in np.arange(1, len(acoes_df.columns)):
  plt.subplot(7, 1, i + 1)
  sns.boxplot(x = acoes_df[acoes_df.columns[i]])
  plt.title(acoes_df.columns[i])

acoes_df.plot(x = 'Date', figsize = (15,7), title = 'Histórico do preço das ações');

acoes_df

acoes_df_normalizado = acoes_df.copy()
for i in acoes_df_normalizado.columns[1:]:
  acoes_df_normalizado[i] = acoes_df_normalizado[i] / acoes_df_normalizado[i][0]

acoes_df_normalizado

acoes_df_normalizado.plot(x = 'Date', figsize = (15,7), title = 'Histórico do preço das ações - normalizado');

figura = px.line(title = 'Histórico do preço das ações')
for i in acoes_df.columns[1:]:
  figura.add_scatter(x = acoes_df['Date'], y = acoes_df[i], name = i)
figura.show()

figura = px.line(title = 'Histórico do preço das ações - normalizado')
for i in acoes_df_normalizado.columns[1:]:
  figura.add_scatter(x = acoes_df_normalizado['Date'], y = acoes_df_normalizado[i], name = i)
figura.show()

"""# Solução"""

acoes_ex = ['ABEV3.SA', 'ODPV3.SA', 'VIVT3.SA', 'PETR3.SA', 'BBAS3.SA', 'BOVA11.SA']

acoes_ex_df = pd.DataFrame()
for acao in acoes_ex:
  #acoes_ex_df[acao] = data.DataReader(acao, data_source='yahoo', start = '2015-01-01')['Close']
  acoes_ex_df[acao] = yf.download(acao, start='2015-01-01')['Close']

acoes_ex_df

acoes_ex_df.isnull().sum()

acoes_ex_df.dropna(inplace=True)
acoes_ex_df.shape

acoes_ex_df = acoes_ex_df.rename(columns={'ABEV3.SA': 'AMBEV', 'ODPV3.SA': 'ODONTOPREV', 'VIVT3.SA': 'VIVO',
                                          'PETR3.SA': 'PETROBRAS', 'BBAS3.SA': 'BBRASIL', 'BOVA11.SA': 'BOVA'})

acoes_ex_df.to_csv('acoes_ex.csv')

acoes_ex_df = pd.read_csv('acoes_ex.csv')
acoes_ex_df

acoes_ex_df.describe()

plt.figure(figsize=(10,50))
i = 1
for i in np.arange(1, len(acoes_ex_df.columns)):
  plt.subplot(7, 1, i + 1)
  sns.histplot(acoes_ex_df[acoes_ex_df.columns[i]], kde = True)
  plt.title(acoes_ex_df.columns[i])

plt.figure(figsize=(10,50))
i = 1
for i in np.arange(1, len(acoes_ex_df.columns)):
  plt.subplot(7, 1, i + 1)
  sns.boxplot(x = acoes_ex_df[acoes_ex_df.columns[i]])
  plt.title(acoes_ex_df.columns[i])

figura = px.line(title = 'Histórico do preço das ações')
for i in acoes_ex_df.columns[1:]:
  figura.add_scatter(x = acoes_ex_df['Date'], y = acoes_ex_df[i], name = i)
figura.show()

acoes_ex_df_normalizado = acoes_ex_df.copy()
for i in acoes_ex_df_normalizado.columns[1:]:
  acoes_ex_df_normalizado[i] = acoes_ex_df_normalizado[i] / acoes_ex_df_normalizado[i][0]

acoes_ex_df_normalizado

figura = px.line(title = 'Histórico do preço das ações - normalizado')
for i in acoes_ex_df_normalizado.columns[1:]:
  figura.add_scatter(x = acoes_ex_df_normalizado['Date'], y = acoes_ex_df_normalizado[i], name = i)
figura.show()
