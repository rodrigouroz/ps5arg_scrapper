#!/usr/bin/env python

import logging
from bs4 import BeautifulSoup
import yaml
from lib.notifier import Notifier
import requests

# logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# configuration    
with open("configuration.yml", 'r') as ymlfile:
    cfg = yaml.safe_load(ymlfile)

disable_ssl = False
if 'disable_ssl' in cfg:
    disable_ssl = cfg['disable_ssl']

notifier = Notifier.get_instance(cfg['notifier'], disable_ssl)

# get page
#ps5_availability_page = requests.get('https://ps5arg-availability.vercel.app/')
ps5_availability_page = requests.get('http://localhost:3000')
page_content = BeautifulSoup(ps5_availability_page.content, 'lxml')
stores = page_content.select('a p')

check = False
for store in stores:
    if store.get_text() != 'No disponible':
        check = True
        break

if check:
    notifier.notify('Hay que verificar al menos una tienda: https://ps5arg-availability.vercel.app')