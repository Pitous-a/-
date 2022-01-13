import pandas as pd
import json
# all = pd.read_csv('./world.csv')
all = pd.read_json('./json/2021-12-15.json')
# confirm_day_add = {}
# dead_day_add = {}
# new_vaccinations = {}
# new_tests = {}
total_cases={}
total_deaths={}
total_tests={}
total_vaccinations={}
ls=[[],[],[],[]]
se = set()
for line in all['continent']:
    if(line != None):
        se.add(line)
se = sorted(se)

total_cases['data'] = se


for i in range(len(se)):
    js = all.loc[all['continent'] == se[i]]
    ls[0].append(0)
    ls[1].append(0)
    ls[2].append(0)
    ls[3].append(0)
    for j in range(len(js)):
        ls[0][i]+=int(js.iloc[j]['total_cases']) if js.iloc[j]['total_cases']>0 else 0
        ls[1][i]+=int(js.iloc[j]['total_deaths']) if js.iloc[j]['total_deaths']>0 else 0
        ls[2][i]+=int(js.iloc[j]['total_tests']) if js.iloc[j]['total_tests']>0 else 0
        ls[3][i]+=int(js.iloc[j]['total_vaccinations']) if js.iloc[j]['total_vaccinations']>0 else 0
total_cases['value']=ls[0]
total_deaths['value']=ls[1]
total_tests['value']=ls[2]
total_vaccinations['value']=ls[3]

with open('./continent/total_cases.json','w') as f:
    json.dump(total_cases,f)

with open('./continent/total_deaths.json','w') as f:
    json.dump(total_deaths,f)

with open('./continent/total_tests.json','w') as f:
    json.dump(total_tests,f)

with open('./continent/total_vaccinations.json','w') as f:
    json.dump(total_vaccinations,f)
