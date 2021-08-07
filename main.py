from tqdm import tqdm
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from selenium import webdriver
import os
import re
import json 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_driver = os.path.join(os.getcwd(),  "headers/chromedriver")

wd = webdriver.Chrome(options=chrome_options)

# open it, go to a website, and get results

date = datetime.now()-timedelta(hours = 5)

wd.get('https://cuantoestaeldolar.pe')
page_source = wd.page_source
wd.quit




soup = BeautifulSoup(page_source, 'html.parser')

#extract casas de cambio

date = datetime.now()-timedelta(hours = 5)

x = soup.find('div', attrs = {'class' : 'clear-fix block-online-change'})
x = x.find_all('div', attrs = {'class' : 'wrapper-table tb_dollar'})

x = [w.get_text() for w in x]
x = [w.strip() for w in x]

x = x[::2]
x = [w.replace('\n', '') for w in x ]
x = [w.split('Cambiar') for w in x ]

datetime_str = date.strftime("%Y_%m_%d-%I_%M_%S")

info_now = {}
info_now[datetime_str] = {}

for i in x:
  info_now[datetime_str][i[0]] = {}
  
  compra_aux = re.findall('^\d.\d?\d?\d?\d', i[1])
  info_now[datetime_str][i[0]]["compra"] = float(compra_aux[0])

  venta_aux = re.findall('\d.\d?\d?\d?\d?\d$', i[1])
  info_now[datetime_str][i[0]]["venta"] = float(venta_aux[0])

if os.path.exists('r/r.json'):

  with open('r/r.json', 'r') as f:
    loaded_data = json.load(f)

  loaded_data.update(info_now)

  with open('r/r.json', 'w') as f:
    json.dump(loaded_data, f)

  print('ga1')


else:
  os.mkdir('r/')
  with open('r/r.json', 'w') as f:
    json.dump(info_now, f)

  print('ga')
  
