# Função retirada do projeto 1 de Cdados
import re
import pandas as pd
import os


def cleanup(text):
    punctuation = '[!-.:?;\n$%#@)(\/“_ショッポ]'
    pattern = re.compile(punctuation)
    text_subbed = re.sub(pattern, '', text)
    return text_subbed


def corrige_num(dfp):
    dfp = dfp.replace('.', '')
    dfp = dfp.replace(',', '.')
    dfp = dfp.replace('R$', '')
    dfp = dfp.replace(' ', '')

    dfp = float(dfp)

    return dfp


def salva_novo_df_limpo(df, save_path):
    os.chdir(os.path.dirname(save_path))

    return df.to_csv('scraping_limpo.csv')
