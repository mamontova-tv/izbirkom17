import requests
from bs4 import BeautifulSoup as bs

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

def get_data(soup):
    data = soup
    uf = data.find( 'a', string='Единый округ' ).parent()
    name = [t.text for t in uf]

    data_1 = data.find('td', string='Число избирателей, внесенных в список избирателей на момент окончания голосования' ).parent()
    data_1 = [t.find('b') for t in data_1 if t.find('b')][0].text

    data_2 = data.find( 'td', string='Число бюллетеней, полученных участковой избирательной комиссией' ).parent()
    data_2 = [t.find( 'b' ) for t in data_2 if t.find( 'b' )][0].text

    data_3 = data.find( 'td', string='Число бюллетеней, выданных избирателям, проголосовавшим досрочно' ).parent()
    data_3 = [t.find( 'b' ) for t in data_3 if t.find( 'b' )][0].text

    data_4 = data.find( 'td', string='Число бюллетеней, выданных избирателям в помещении для голосования в день голосования' ).parent()
    data_4 = [t.find( 'b' ) for t in data_4 if t.find( 'b' )][0].text

    data_5 = data.find( 'td', string='Число бюллетеней, выданных избирателям, проголосовавшим вне помещения для голосования в день голосов' ).parent()
    data_5 = [t.find( 'b' ) for t in data_5 if t.find( 'b' )][0].text

    data_6 = data.find( 'td', string='Число погашенных бюллетеней' ).parent()
    data_6 = [t.find( 'b' ) for t in data_6 if t.find( 'b' )][0].text

    data_7 = data.find( 'td', string='Число бюллетеней, содержащихся в переносных ящиках для голосования' ).parent()
    data_7 = [t.find( 'b' ) for t in data_7 if t.find( 'b' )][0].text

    data_8 = data.find( 'td', string='Число бюллетеней, содержащихся в стационарных ящиках для голосования' ).parent()
    data_8 = [t.find( 'b' ) for t in data_8 if t.find( 'b' )][0].text

    data_9 = data.find( 'td', string='Число недействительных бюллетеней' ).parent()
    data_9 = [t.find( 'b' ) for t in data_9 if t.find( 'b' )][0].text

    data_10 = data.find( 'td', string='Число действительных бюллетеней' ).parent()
    data_10 = [t.find( 'b' ) for t in data_10 if t.find( 'b' )][0].text

    data_11 = data.find( 'td', string='Число утраченных бюллетеней' ).parent()
    data_11 = [t.find( 'b' ) for t in data_11 if t.find( 'b' )][0].text

    data_12 = data.find( 'td', string='Число бюллетеней, не учтенных при получении' ).parent()
    data_12 = [t.find( 'b' ) for t in data_12 if t.find( 'b' )][0].text

    data_13 = data.find( 'td', string='1.1. Политическая партия ЛДПР – Либерально-демократическая партия России' ).parent()
    data_13 = [t.find( 'b' ) for t in data_13 if t.find( 'b' )][0].text

    data_14 = data.find( 'td', string='2.3. Политическая партия КОММУНИСТИЧЕСКАЯ ПАРТИЯ КОММУНИСТЫ РОССИИ' ).parent()
    data_14 = [t.find( 'b' ) for t in data_14 if t.find( 'b' )][0].text

    data_15 = data.find( 'td', string='3.4. Политическая партия СПРАВЕДЛИВАЯ РОССИЯ' ).parent()
    data_15 = [t.find( 'b' ) for t in data_15 if t.find( 'b' )][0].text

    data_16 = data.find( 'td', string='4.5. Всероссийская политическая партия "ЕДИНАЯ РОССИЯ"' ).parent()
    data_16 = [t.find( 'b' ) for t in data_16 if t.find( 'b' )][0].text

    data_17 = data.find( 'td', string='5.6. Политическая партия "КОММУНИСТИЧЕСКАЯ ПАРТИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ"' ).parent()
    data_17 = [t.find( 'b' ) for t in data_17 if t.find( 'b' )][0].text

    return (name + [data_1, data_2, data_3, data_4, data_5, data_6, data_7, data_8,
                   data_9, data_10, data_11, data_12, data_13, data_14, data_15, data_16, data_17])

soup = get_soup(URL_START)
level_one = search_select(soup)
try:
    for i in level_one:
        soup_one = (get_soup(i))
        for level_two in search_select(soup_one):
            soup_two = get_soup(level_two)
            uf = soup_two.find('a', string='Результаты выборов по единому округу').get('href')
            soup_three = get_soup(uf)
            data = get_data(soup_three)
            print (data)
except Exception as e:
    print (e)
