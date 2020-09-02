
import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text


def get_id_last_ad(url,Sections):
    html = get_html(url)
    soup = BeautifulSoup(html,'lxml')
    ad_top = soup.find('div',class_='b-page__lenta')
    ad_top = ad_top.find('div',id='projects-list').find_all('div',class_='topprjpay')
    ads = soup.find('div',id='projects-list').find_all('div',class_='b-post')
    for ad in ads:
        if ad in ad_top:
            continue
        else:
            necessary_ad = ad
            break
    necessary_ad_url = 'https://www.fl.ru' + necessary_ad.find('h2').find('a').get('href')
    html = get_html(necessary_ad_url)
    soup = BeautifulSoup(html,'lxml')
    try:
        as_ = soup.find('div',class_='b-layout b-layout_overflow_hidden b-layout_margbot_10').find('div',class_='b-layout__txt b-layout__txt_fontsize_11 b-layout__txt_padbot_20').find_all('a')
        sections = []
        for a in as_:
            sections.append(a.text.strip())
    except:
        sections = []
    startPars = False
    for section in sections:
        if section in Sections:
            startPars = True
            break
    if startPars:
        #id
        try:
            id = soup.find('h1',class_='b-page__title').get('id').split('_')[-1].strip()
        except:
            id = ''
        #Дата
        try:
            date = soup.find('div',class_='b-layout_margbot_10').find('div',class_='b-layout__txt_padbot_30').find('div',class_='b-layout__txt b-layout__txt_fontsize_11')
            date = date.text
            date =  date.strip().encode('utf-8').decode('utf-8')
        except:
            date = ''
        
        f = open('text.txt','w')
        #Задание
        try:
            task = soup.find('h1',class_='b-page__title').text.strip().encode('utf-8').decode('utf-8')
        except:
            task = ''
        #Стоимость
        try:
            cash = soup.find('td',class_='b-layout__td b-layout__td_padtb_10 b-layout__td_right b-layout__td_ipad').find('div',class_='b-layout__txt b-layout__txt_fontsize_11').text.strip().encode('utf-8').decode('utf-8')
        except:
            cash = ''
        try:
            f.write(task+'\n'+cash+'\n'+date)
        except:
            text = 'Новое объявление'
            f.write(text)
        f.close()
        return id
    else:
        return False
#Sect = ['SMM (маркетинг в соцсетях)','Интернет-магазины']
#print(get_id_last_ad('https://www.fl.ru/projects/',Sect))
        
        
        
        







