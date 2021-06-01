# Análise dos dados
import numpy as np
import camelot
import missingno as mn
import seaborn as sb
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt


def marca(dfa):
    dfa['Marca'] = pd.np.where(dfa['Descricao'].str.contains('Samsung'), 'Samsung',
                               pd.np.where(dfa['Descricao'].str.contains('LG'), 'LG',
                                           pd.np.where(dfa['Descricao'].str.contains('Motorola'), 'Motorola',
                                                       pd.np.where(dfa['Descricao'].str.contains('Xiaomi'), 'Xiaomi',
                                                                   pd.np.where(dfa.Descricao.str.contains('Positivo'),
                                                                               'Positivo',
                                                                               pd.np.where(dfa.Descricao.str.contains(
                                                                                   'Multilaser'), 'Multilaser',
                                                                                           pd.np.where(
                                                                                               dfa.Descricao.str.contains(
                                                                                                   'Nokia'), 'Nokia',
                                                                                               pd.np.where(
                                                                                                   dfa.Descricao.str.contains(
                                                                                                       'Moto'),
                                                                                                   'Motorola',
                                                                                                   pd.np.where(
                                                                                                       dfa.Descricao.str.contains(
                                                                                                           'Xiaomí'),
                                                                                                       'Xiaomi',
                                                                                                       pd.np.where(
                                                                                                           dfa.Descricao.str.contains(
                                                                                                               'Redimi'),
                                                                                                           'Xiaomi',
                                                                                                           pd.np.where(
                                                                                                               dfa.Descricao.str.contains(
                                                                                                                   'SAMSUNG'),
                                                                                                               'Samsung',
                                                                                                               'Outra')))))))))))
    return dfa


def capacidade(dff):
    dff['Capacidade'] = pd.np.where(dff.Descricao.str.contains('32GB'), '32GB',
                                    pd.np.where(dff.Descricao.str.contains('64GB'), '64GB',
                                                pd.np.where(dff.Descricao.str.contains('128GB'), '128GB',
                                                            pd.np.where(dff.Descricao.str.contains('256GB'), '256GB',
                                                                        pd.np.where(dff.Descricao.str.contains('64Gb'),
                                                                                    '64GB',
                                                                                    pd.np.where(
                                                                                        dff.Descricao.str.contains(
                                                                                            '128Gb'), '128GB',
                                                                                        pd.np.where(
                                                                                            dff.Descricao.str.contains(
                                                                                                '32Gb'), '32GB',
                                                                                            pd.np.where(
                                                                                                dff.Descricao.str.contains(
                                                                                                    '256Gb'), '256GB',
                                                                                                pd.np.where(
                                                                                                    dff.Descricao.str.contains(
                                                                                                        '32gb'), '32GB',
                                                                                                    pd.np.where(
                                                                                                        dff.Descricao.str.contains(
                                                                                                            '64gb'),
                                                                                                        '64GB',
                                                                                                        pd.np.where(
                                                                                                            dff.Descricao.str.contains(
                                                                                                                '128gb'),
                                                                                                            '128GB',
                                                                                                            pd.np.where(
                                                                                                                dff.Descricao.str.contains(
                                                                                                                    '256gb'),
                                                                                                                '256GB',
                                                                                                                'Outro'))))))))))))

    return dff


def pivotCAPAmarca(df123):
    pivot = pd.pivot_table(df123, index='Marca', columns='Capacidade',
                           values='Preco', aggfunc={'Preco': np.mean})
    pivot_aux = pivot.unstack().reset_index()
    pivot_aux.columns = ['Capacidade', 'Marca', 'Preco']

    fig = px.bar(pivot_aux, x='Marca', y='Preco', color='Capacidade',
                 barmode='group', title='Relação entre capacidade, marca e preço')

    return [pivot, fig]


def cores(dff22):
    dff22['Cores'] = pd.np.where(dff22.Descricao.str.contains('Azul'), 'Azul',
                                 pd.np.where(dff22.Descricao.str.contains('Preto'), 'Preto',
                                             pd.np.where(dff22.Descricao.str.contains('Branco'), 'Branco',
                                                         pd.np.where(dff22.Descricao.str.contains('Verde'), 'Verde',
                                                                     pd.np.where(
                                                                         dff22.Descricao.str.contains('Vermelho'),
                                                                         'Vermelho',
                                                                         pd.np.where(
                                                                             dff22.Descricao.str.contains('Cinza'),
                                                                             'Cinza',
                                                                             pd.np.where(
                                                                                 dff22.Descricao.str.contains('White'),
                                                                                 'Branco', 'Outro')))))))
    return dff22


def pivotCAPAcores(df1234):
    pivot = pd.pivot_table(df1234, index='Marca', columns='Cores',
                           values='Preco', aggfunc={'Preco': np.mean})
    pivot_aux = pivot.unstack().reset_index()
    pivot_aux.columns = ['Cores', 'Marca', 'Preco']

    fig = px.bar(pivot_aux, x='Marca', y='Preco', color='Cores', barmode='group',
                  title='Relação entre cores, marca e preço dos celulares')

    return [fig, pivot]

# Atenção, para importar as funções não vá pelo caminho chique do apply #humilde df = marca(df) e df = capacidade(df) e pivotCAPAmarca(df)
