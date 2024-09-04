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
    'uxfb_usertype': 'searcher',
    '_ga': 'GA1.1.1787081564.1722858969',
    '_ym_uid': '1722858970197820366',
    '_ym_d': '1722858970',
    'uxs_uid': 'b453ed40-5321-11ef-99f5-13acaf43e780',
    'adrcid': 'Atxa_VJaIJzGt7ImntPpnNQ',
    'adrcid': 'Atxa_VJaIJzGt7ImntPpnNQ',
    'afUserId': '73bcdbd8-0c88-4ea9-ab72-f5c79785b425-p',
    'cookie_agreement_accepted': '1',
    '__cf_bm': '.gDwSZhnfsJaQ5KnCNsWIAfVuw8EWyYYfh3dKMaRoM4-1725379177-1.0.1.1-OH60vZ2sDizhKyez2Jzrfm9UkpRW5T1GLyL74iBHgon.QwZA5xakVYew64SIWvsOnETVMxSmvTPIaviAILNj1g',
    'cf_clearance': 'LisV7KX2dL8yXeh.iwE2cN1IbrkPVuRNs3MMBEM74R4-1725379181-1.2.1.1-Zn_sc3qoJCpr5c8e3mRiPCOU1lzfAQPOeLSln8w0.j029fo3gCwHQKy_mcS_ZE4kVBcjsOY0cWalgXuUEnr_ct.yImCw4rjNOCHRyA9DUPNeFWre6I7XYnHLX576oOXCRYnid16g5ylO95ZVVhyP9KqDhTIHtR5Ij4A0Xj7U4Iz8ORovCXKe.4Ov_c6zKSoW6OdJ8OTEsJY5ZpfByS5wrDsoq3PYM21SE9J.xwWCKGwIg.sOXOGhjko5czFoiy4VSdk9fs6vN4jiOZWOBJP39y3dyedEzLI8wJfPxPiVl3kkuSwtDbdMPMerX5y9NDiY9SLkeExst3cZXM8RmFwhyZVnlC.5ez7YRidFyyoH64Kh3zMmoqFRUBG6oH4lL_d_obH0y._g6V5zJ8CSepQzOg',
    'login_mro_popup': '1',
    'domain_sid': '3FwuQOzVmVF8B_C50aA-6%3A1725379171394',
    'sopr_utm': '%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D',
    'sopr_session': '8482108151214c5e',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'adrdel': '1725379180057',
    'adrdel': '1725379180057',
    'acs_3': '%7B%22hash%22%3A%2240a47f53e220d7da5392%22%2C%22nextSyncTime%22%3A1725465580101%2C%22syncLog%22%3A%7B%22224%22%3A1725379180101%2C%221228%22%3A1725379180101%2C%221230%22%3A1725379180101%7D%7D',
    'acs_3': '%7B%22hash%22%3A%2240a47f53e220d7da5392%22%2C%22nextSyncTime%22%3A1725465580101%2C%22syncLog%22%3A%7B%22224%22%3A1725379180101%2C%221228%22%3A1725379180101%2C%221230%22%3A1725379180101%7D%7D',
    'AF_SYNC': '1725379180223',
    'session_region_id': '1',
    'session_main_town_region_id': '1',
    'cian_app_tooltip_key': '1',
    'uxfb_card_satisfaction': '%5B291919163%2C270998805%2C287111478%2C305229825%5D',
    'tmr_detect': '0%7C1725379836851',
    '_ga_3369S417EL': 'GS1.1.1725379174.3.1.1725379854.33.0.0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    # 'cookie': '_CIAN_GK=ae9d4d15-a42d-4df8-9ac1-620c1741ce31; _gcl_au=1.1.703799869.1722858968; tmr_lvid=9b8686fe26062fef7b5f4103d6675848; tmr_lvidTS=1722858968584; uxfb_usertype=searcher; _ga=GA1.1.1787081564.1722858969; _ym_uid=1722858970197820366; _ym_d=1722858970; uxs_uid=b453ed40-5321-11ef-99f5-13acaf43e780; adrcid=Atxa_VJaIJzGt7ImntPpnNQ; adrcid=Atxa_VJaIJzGt7ImntPpnNQ; afUserId=73bcdbd8-0c88-4ea9-ab72-f5c79785b425-p; cookie_agreement_accepted=1; __cf_bm=.gDwSZhnfsJaQ5KnCNsWIAfVuw8EWyYYfh3dKMaRoM4-1725379177-1.0.1.1-OH60vZ2sDizhKyez2Jzrfm9UkpRW5T1GLyL74iBHgon.QwZA5xakVYew64SIWvsOnETVMxSmvTPIaviAILNj1g; cf_clearance=LisV7KX2dL8yXeh.iwE2cN1IbrkPVuRNs3MMBEM74R4-1725379181-1.2.1.1-Zn_sc3qoJCpr5c8e3mRiPCOU1lzfAQPOeLSln8w0.j029fo3gCwHQKy_mcS_ZE4kVBcjsOY0cWalgXuUEnr_ct.yImCw4rjNOCHRyA9DUPNeFWre6I7XYnHLX576oOXCRYnid16g5ylO95ZVVhyP9KqDhTIHtR5Ij4A0Xj7U4Iz8ORovCXKe.4Ov_c6zKSoW6OdJ8OTEsJY5ZpfByS5wrDsoq3PYM21SE9J.xwWCKGwIg.sOXOGhjko5czFoiy4VSdk9fs6vN4jiOZWOBJP39y3dyedEzLI8wJfPxPiVl3kkuSwtDbdMPMerX5y9NDiY9SLkeExst3cZXM8RmFwhyZVnlC.5ez7YRidFyyoH64Kh3zMmoqFRUBG6oH4lL_d_obH0y._g6V5zJ8CSepQzOg; login_mro_popup=1; domain_sid=3FwuQOzVmVF8B_C50aA-6%3A1725379171394; sopr_utm=%7B%22utm_source%22%3A+%22google%22%2C+%22utm_medium%22%3A+%22organic%22%7D; sopr_session=8482108151214c5e; _ym_isad=2; _ym_visorc=b; adrdel=1725379180057; adrdel=1725379180057; acs_3=%7B%22hash%22%3A%2240a47f53e220d7da5392%22%2C%22nextSyncTime%22%3A1725465580101%2C%22syncLog%22%3A%7B%22224%22%3A1725379180101%2C%221228%22%3A1725379180101%2C%221230%22%3A1725379180101%7D%7D; acs_3=%7B%22hash%22%3A%2240a47f53e220d7da5392%22%2C%22nextSyncTime%22%3A1725465580101%2C%22syncLog%22%3A%7B%22224%22%3A1725379180101%2C%221228%22%3A1725379180101%2C%221230%22%3A1725379180101%7D%7D; AF_SYNC=1725379180223; session_region_id=1; session_main_town_region_id=1; cian_app_tooltip_key=1; uxfb_card_satisfaction=%5B291919163%2C270998805%2C287111478%2C305229825%5D; tmr_detect=0%7C1725379836851; _ga_3369S417EL=GS1.1.1725379174.3.1.1725379854.33.0.0',
    'priority': 'u=0, i',
    'referer': 'https://www.cian.ru/snyat/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

params = {
    'deal_type': 'rent',
    'engine_version': '2',
    'foot_min': '20',
    'metro[0]': '281',
    'offer_type': 'flat',
    'only_foot': '2',
    'room2': '1',
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