import requests

'''r = requests.get('https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address=서울특별시 영등포구')
rjson = r.json()

store_list = rjson['stores']

for store in store_list:
    if store['remain_stat'] == 'plenty' :
        print(store['name'], store['addr'])'''


gus = ['영등포구', '마포구', '중구']

for gu in gus :
    place = '서울특별시 '+gu
    url ='https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/storesByAddr/json?address='+place

r = requests.get(url)
rjson = r.json()

store_list = rjson['stores']

for store in store_list:
    try :
        if store['remain_stat'] == 'plenty' :
            print(store['name']+'('+store['addr']+')')

    except :
        continue
