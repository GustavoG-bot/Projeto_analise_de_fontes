from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import os


class Scraping:
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.html = ''
        self.bs4 = ''
        self.driver = ''
        self.descricao = ''
        self.preco = ''
        self.dicionario = ''
        self.df = ''
        self.save_path = r'C:\Users\wilgn\Desktop\Faculdade\3° Semestre\Analise de fontes e textos desestruturados na web\Projeto\Projeto_analise_de_fontes\input\\'

    def faz_request(self):
        self.driver = webdriver.Chrome(self.path)
        self.driver.get(self.url)
        for i in range(10):
            self.driver.find_element_by_xpath(
                '//*[@id="__next"]/div[2]/div/div/div[4]/div[2]/div/article/div[3]/div/div/div/button').click()
            time.sleep(5)
        self.html = self.driver.page_source
        self.driver.quit()

    def recebe_html(self):
        self.bs4 = BeautifulSoup(self.html, 'html.parser')

    def pega_descricao(self):
        html_descricao = self.bs4.find_all('p', {'class':'ProductCard__Title-sc-2vuvzo-0 iBDOQj'})
        self.descricao = [descricao.text for descricao in html_descricao]

    def pega_preco(self):
        html_preco = self.bs4.find_all('span', {'class':'ProductPrice__PriceValue-sc-1tzw2we-6 kBYiGY'})
        self.preco = [preco.text for preco in html_preco]

    def cria_dataframe(self):
        self.pega_descricao()
        self.pega_preco()
        self.df = pd.DataFrame(data={'Descricao': self.descricao[:230],
                                     'Preco': self.preco})

    def salva_dataframe(self):
        os.chdir(os.path.dirname(self.save_path))
        self.df.to_csv('carrefour_scraping.csv')

