import json

with open('input_ios.json') as f: 
   data = json.load(f)

prod_in = input().upper() 

prod_data = [x for x in data['sales'] if x['prod']==prod_in] 
dic = {}
for x in prod_data: 
    if x['country'] in dic:
        dic[x['country']] += x['price']
    else:
        dic[x['country']] = x['price']

print("Country with max sales",max(dic, key=dic.get))