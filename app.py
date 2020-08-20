from __future__ import print_function
import json, urllib.request

apikey = 'e2b7a94889b847808871'

startRow = 1
endRow = 10

url = 'http://openapi.foodsafetykorea.go.kr/api/e2b7a94889b847808871/I2790/json/' + str(startRow) + '/' + str(endRow)

data = urllib.request.urlopen(url).read()
output = json.loads(data)

name = output['I2790']['row'][0]['DESC_KOR']
kcal = output['I2790']['row'][0]['NUTR_CONT1']

print(name, kcal)
