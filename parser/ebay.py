import logging
import json
import requests
from lxml import html
from get_headers import get_headers


logging.basicConfig(level=logging.INFO)


def ebay_get_html(productid, proxy):
    url = f'https://www.ebay.com/itm/{productid}'
    headers = get_headers()
    if proxy:
        proxies = {proxy.split(':')[0]: proxy }
    else:
        proxies = None
    try:
        response = requests.get(url,headers=headers, proxies=proxies)
    except Exception as e:
        logging.info(f'Error request')
        logging.info(f'{e}')
        return 'Error'
    return response.text



"""
    print(r)
    tree = html.fromstring(r.content)
    #jsons = tree.xpath('//div[@id="JSDF"]/script/text()')
    jsons = tree.xpath('//script/text()')
    print(len(jsons))
    for j in jsons:
        if 'vim_C=(window' in j:
            print(j)
"""

