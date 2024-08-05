from bs4 import BeautifulSoup
import requests
import json
import time

url='https://www.cian.ru/cat.php'

cookies = {
    '_CIAN_GK': 'ae9d4d15-a42d-4df8-9ac1-620c1741ce31',
    '_gcl_au': '1.1.703799869.1722858968',
    'tmr_lvid': '9b8686fe26062fef7b5f4103d6675848',
    'tmr_lvidTS': '1722858968584',
    'domain_sid': '3FwuQOzVmVF8B_C50aA-6%3A1722858968677',
    'sopr_utm': '%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D',
    'uxfb_usertype': 'searcher',
    '_ga': 'GA1.1.1787081564.1722858969',
    '_ym_uid': '1722858970197820366',
    '_ym_d': '1722858970',
    'uxs_uid': 'b453ed40-5321-11ef-99f5-13acaf43e780',
    '_ym_isad': '2',
    'adrdel': '1722858969773',
    'adrdel': '1722858969773',
    'adrcid': 'Atxa_VJaIJzGt7ImntPpnNQ',
    'adrcid': 'Atxa_VJaIJzGt7ImntPpnNQ',
    'afUserId': '73bcdbd8-0c88-4ea9-ab72-f5c79785b425-p',
    'AF_SYNC': '1722858970094',
    'session_region_id': '1',
    'session_main_town_region_id': '1',
    'cf_clearance': 'dqGsrKE0ODUSTqSK1TOID_m7nM2.oucjH4iCfCuzNDw-1722866964-1.0.1.1-KkuoYeCyleBheB1fK4uU.Wi0rvkv0_1aWPqKZuBzYauDY4DuVsfOlq4TGqXo6YGL8lykSrjmaEfRS0lYmRN4bw',
    'login_mro_popup': '1',
    'sopr_session': '17f6200af16c4e58',
    '_ym_visorc': 'b',
    '__cf_bm': 'ISX46KXqpxKNK5rBUfFuU3eURJ_jiMCGPdc_vX2V0dI-1722868427-1.0.1.1-._qEpvdkVZnHlPbho32pMbS6ssktfFF4OuEaViXDo8PVGnMqvBfGf1iPZWXSWGtdzN2MS.t0J8f.A1snLMLhFw',
    'cookie_agreement_accepted': '1',
    'tmr_detect': '0%7C1722868861336',
    '_ga_3369S417EL': 'GS1.1.1722866965.2.1.1722868895.59.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_CIAN_GK=ae9d4d15-a42d-4df8-9ac1-620c1741ce31; _gcl_au=1.1.703799869.1722858968; tmr_lvid=9b8686fe26062fef7b5f4103d6675848; tmr_lvidTS=1722858968584; domain_sid=3FwuQOzVmVF8B_C50aA-6%3A1722858968677; sopr_utm=%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D; uxfb_usertype=searcher; _ga=GA1.1.1787081564.1722858969; _ym_uid=1722858970197820366; _ym_d=1722858970; uxs_uid=b453ed40-5321-11ef-99f5-13acaf43e780; _ym_isad=2; adrdel=1722858969773; adrdel=1722858969773; adrcid=Atxa_VJaIJzGt7ImntPpnNQ; adrcid=Atxa_VJaIJzGt7ImntPpnNQ; afUserId=73bcdbd8-0c88-4ea9-ab72-f5c79785b425-p; AF_SYNC=1722858970094; session_region_id=1; session_main_town_region_id=1; cf_clearance=dqGsrKE0ODUSTqSK1TOID_m7nM2.oucjH4iCfCuzNDw-1722866964-1.0.1.1-KkuoYeCyleBheB1fK4uU.Wi0rvkv0_1aWPqKZuBzYauDY4DuVsfOlq4TGqXo6YGL8lykSrjmaEfRS0lYmRN4bw; login_mro_popup=1; sopr_session=17f6200af16c4e58; _ym_visorc=b; __cf_bm=ISX46KXqpxKNK5rBUfFuU3eURJ_jiMCGPdc_vX2V0dI-1722868427-1.0.1.1-._qEpvdkVZnHlPbho32pMbS6ssktfFF4OuEaViXDo8PVGnMqvBfGf1iPZWXSWGtdzN2MS.t0J8f.A1snLMLhFw; cookie_agreement_accepted=1; tmr_detect=0%7C1722868861336; _ga_3369S417EL=GS1.1.1722866965.2.1.1722868895.59.0.0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

params = {
    'deal_type': 'rent',
    'engine_version': '2',
    'foot_min': '20',
    'metro[0]': '281',
    'offer_type': 'flat',
    'only_foot': '2',
    'sort': 'price_object_order',
    'type': '4',
}


def collect_data():
    response = requests.get(
        url=url,
        params=params,
        cookies=cookies,
        headers=headers,
    )

    bs = BeautifulSoup(response.text, 'html.parser')
    if response.status_code == 200:
        pass
    else:
        print("Error "+ str(response.status_code) + ' try again.')
        exit()

    hrefs = bs.find_all('a', class_ = '_93444fe79c--link--VtWj6')
    product_names = bs.select('[data-mark="OfferTitle"]')
    prices = bs.select('[data-mark="MainPrice"]')
    locations = bs.find_all('div', class_ = '_93444fe79c--labels--L8WyJ')

    result = []
    product_price=[]
    product_href=[]
    product_location=[]

    for price in prices:
        product_price.append(price.text)

    for href in hrefs:
        product_href.append(href.get('href'))

    for location in locations:
        product_location.append(location.text)

    i=0
    for product_name in product_names:
        result.append({
            'name': product_name.text,
            'url': product_href[i],
            'price': product_price[i],
            'location': product_location[i]
        })
        i+=1

    with open ('result_cian.json', 'w', encoding="utf-8") as file: 
        json.dump(result, file, indent = 4, ensure_ascii = False)
        print("Dumped successfully")
    file.close()

def main():
    collect_data()

if __name__ == '__main__': 
    main() 