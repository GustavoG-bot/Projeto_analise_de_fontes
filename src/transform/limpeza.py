#Função retirada do projeto 1 de Cdados 
import re

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
