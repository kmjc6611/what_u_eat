from __future__ import print_function
import json, urllib.request

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.myproject

apikey = 'e2b7a94889b847808871'

startRow = 1
endRow = 100

url = 'http://openapi.foodsafetykorea.go.kr/api/e2b7a94889b847808871/I2790/json/' + str(startRow) + '/' + str(endRow)

data = urllib.request.urlopen(url).read()
output = json.loads(data)
foods = output['I2790']['row']
for food in foods:
    name = food['DESC_KOR']
    company = food['MAKER_NAME']
    kcal = food['NUTR_CONT1']
    carbo = food['NUTR_CONT2']
    pro = food['NUTR_CONT3']
    fat = food['NUTR_CONT4']

    # print(name, company, kcal, carbo, pro, fat)
    doc = {
        'name': name,
        'company': company,
        'kcal': kcal,
        'carbo': carbo,
        'pro': pro,
        'fat': fat
    }
    db.food.insert_one(doc)
