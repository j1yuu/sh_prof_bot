import re
import random

import requests
from bs4 import BeautifulSoup as bs

headers_2 = {
    'method':'GET',
    'scheme':'https',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Cache-Control':'max-age=0',
    'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'Sec-Ch-Ua-Platform':"Windows",
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
}

url='https://baneks.ru/'

def randomAnec():
    global url
    anec_num = random.randint(1, 1142)
    return url+str(anec_num)

def parse_anec():
    uri = randomAnec()
    try:
        r = requests.get(uri, headers=headers_2)
        print(r.status_code)
        soup = bs(r.text, "html.parser")
        return soup.find("p").text
    except:
        return "Бля, чет забыл пиздец"
    