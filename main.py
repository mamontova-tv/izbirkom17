import requests
from bs4 import BeautifulSoup as bs
from multiprocessing.dummy import Pool as ThreadPool

#URL_START - стартовая страница региона по единому округу
URL_START = 'http://www.tyva.vybory.izbirkom.ru/region/tyva?action=show&root_a=172000050&vrn=2172000576653&region=17' \
            '&global=null&type=0&sub_region=17&prver=2&pronetvd=1&root=1'

def get_soup(url):
    '''Извлекаем данные BeautifulSoup '''
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0'}
    response = requests.get(url, headers=headers ).text
    soup = bs(response, 'html.parser')
    return soup

def search_select(soup):
    '''Извлекаем ссылки на уровне'''
    url_all = []
    tag = (soup.findAll( 'form', attrs={'name': 'go_reg'} ))[0]
    for i in tag.findAll('option'):
        try:
            url = (i['value'])
            url_all.append(url)
        except:
            pass
    return url_all

soup = get_soup(URL_START)
level_one = search_select(soup)
try:
    for i in level_one:
        soup_one = (get_soup(i))
        for level_two in search_select(soup_one):
            soup_two = get_soup(level_two)
            uf = soup_two.find('a', string='Результаты выборов по единому округу').get('href')
            print (uf)
except Exception as e:
    print (e)
