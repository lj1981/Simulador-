# -*- coding: utf-8 -*-
"""Visualização_de_dados_financeiros.ipynb"""

"""## Importação das bibliotecas"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import yfinance as yf

"""## Base de dados com uma ação"""

# Baixar dados de uma ação diretamente do Yahoo Finance
gol_df = yf.download("GOLL4.SA", start='2024-01-01')

# Salvando os dados localmente e carregando do GitHub
gol_df.to_csv('gol.csv')
gol_df2 = pd.read_csv('https://raw.githubusercontent.com/lj1981/Simulador-/main/gol.csv')
gol_df2

"""## Base de dados com mais ações"""

acoes = ['GOLL4.SA', 'CVCB3.SA', 'WEGE3.SA', 'MGLU3.SA', 'TOTS3.SA', 'BOVA11.SA']

acoes_df = pd.DataFrame()
for acao in acoes:
    acoes_df[acao] = yf.download(acao, start='2024-01-01')['Close']

acoes_df = acoes_df.rename(columns={
    'GOLL4.SA': 'GOL', 'CVCB3.SA': 'CVC', 'WEGE3.SA': 'WEGE',
    'MGLU3.SA': 'MGLU', 'TOTS3.SA': 'TOTS', 'BOVA11.SA': 'BOVA'
})

acoes_df.dropna(inplace=True)

# Salvando os dados localmente e carregando do GitHub
acoes_df.to_csv('acoes.csv')
acoes_df = pd.read_csv('https://raw.githubusercontent.com/lj1981/Simulador-/main/acoes.csv')
acoes_df

"""## Visualização"""

sns.histplot(acoes_df['GOL'])

plt.figure(figsize=(10, 50))
for i, column in enumerate(acoes_df.columns[1:], 1):
    plt.subplot(7, 1, i)
    sns.histplot(acoes_df[column], kde=True)
    plt.title(column)

acoes_df_normalizado = acoes_df.copy()
for column in acoes_df_normalizado.columns[1:]:
    acoes_df_normalizado[column] /= acoes_df_normalizado[column].iloc[0]

figura = px.line(title='Histórico do preço das ações')
for column in acoes_df.columns[1:]:
    figura.add_scatter(x=acoes_df['Date'], y=acoes_df[column], name=column)
figura.show()

figura_normalizado = px.line(title='Histórico do preço das ações - normalizado')
for column in acoes_df_normalizado.columns[1:]:
    figura_normalizado.add_scatter(
        x=acoes_df_normalizado['Date'], y=acoes_df_normalizado[column], name=column)
figura_normalizado.show()

"""## Exercício e solução"""

acoes_ex = ['ABEV3.SA', 'ODPV3.SA', 'VIVT3.SA', 'PETR3.SA', 'BBAS3.SA', 'BOVA11.SA']

acoes_ex_df = pd.DataFrame()
for acao in acoes_ex:
    acoes_ex_df[acao] = yf.download(acao, start='2015-01-01')['Close']

acoes_ex_df = acoes_ex_df.rename(columns={
    'ABEV3.SA': 'AMBEV', 'ODPV3.SA': 'ODONTOPREV', 'VIVT3.SA': 'VIVO',
    'PETR3.SA': 'PETROBRAS', 'BBAS3.SA': 'BBRASIL', 'BOVA11.SA': 'BOVA'
})

acoes_ex_df.dropna(inplace=True)

# Salvando os dados localmente e carregando do GitHub
acoes_ex_df.to_csv('acoes_ex.csv')
acoes_ex_df = pd.read_csv('https://raw.githubusercontent.com/lj1981/Simulador-/main/acoes_ex.csv')
acoes_ex_df

plt.figure(figsize=(10, 50))
for i, column in enumerate(acoes_ex_df.columns[1:], 1):
    plt.subplot(7, 1, i)
    sns.histplot(acoes_ex_df[column], kde=True)
    plt.title(column)

acoes_ex_df_normalizado = acoes_ex_df.copy()
for column in acoes_ex_df_normalizado.columns[1:]:
    acoes_ex_df_normalizado[column] /= acoes_ex_df_normalizado[column].iloc[0]

figura_ex_normalizado = px.line(title='Histórico do preço das ações - normalizado')
for column in acoes_ex_df_normalizado.columns[1:]:
    figura_ex_normalizado.add_scatter(
        x=acoes_ex_df_normalizado['Date'], y=acoes_ex_df_normalizado[column], name=column)
figura_ex_normalizado.show()
