# Análise dos dados
import numpy as np
import camelot
import missingno as mn
import seaborn as sb
import plotly.express as px
import matplotlib.pyplot as plt

def marca(dfa):
    dfa['Marca'] = pd.np.where(dfa['Descricao'].str.contains('Samsung'), 'Samsung', 
                              pd.np.where(dfa['Descricao'].str.contains('LG'), 'LG',
                              pd.np.where(dfa['Descricao'].str.contains('Motorola'), 'Motorola',
                              pd.np.where(dfa['Descricao'].str.contains('Xiaomi'), 'Xiaomi' , 
                              pd.np.where(dfa.Descricao.str.contains('Positivo'), 'Positivo', 'Outra')))))
    return dfa

def capacidade(dff): 
    dff['Capacidade'] = pd.np.where(dff.Descricao.str.contains('32GB'), '32GB', 
                pd.np.where(dff.Descricao.str.contains('64GB'), '64GB',
                pd.np.where(dff.Descricao.str.contains('128GB'), '128GB',
                pd.np.where(dff.Descricao.str.contains('256GB'), '256GB', 'Outro')))) 

    return dff

def pivotCAPAmarca(df123):
    pivot = pd.pivot_table(df123, index='Marca', columns='Capacidade', values='Preco', aggfunc={'Preco':np.mean})
    pivot_aux = pivot.unstack().reset_index()
    pivot_aux.columns = ['Capacidade', 'Marca', 'Preco']
    
    return px.bar(pivot_aux, x='Marca', y='Preco', color='Capacidade', barmode='group', title='Relação entre capacidade, marca e preço')

# Atenção, para importar as funções não vá pelo caminho chique do apply #humilde df = marca(df) e df = capacidade(df) e pivotCAPAmarca(df)