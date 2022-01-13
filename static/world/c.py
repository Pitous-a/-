import pandas as pd
import json
all = pd.read_csv('./world.csv')

confirm_day_add={}
dead_day_add={}
new_vaccinations={}
new_tests={}
c=[]
t=[]
d=[]
v=[]
se = set()
for line in all['date']:
    if(line[0:4]=='2021'):
        se.add(line)
se=sorted(se)
confirm_day_add['data']=se


for i in range(len(se)):
    js = all.loc[all['date'] == se[i]]
    c.append(0)
    t.append(0)
    d.append(0)
    v.append(0)
    for j in range(len(js)):
        c[i]+=int(js.iloc[j]['new_cases']) if js.iloc[j]['new_cases']>0 else 0
        t[i]+=int(js.iloc[j]['new_tests']) if js.iloc[j]['new_tests']>0 else 0
        d[i]+=int(js.iloc[j]['new_deaths']) if js.iloc[j]['new_deaths']>0 else 0
        v[i]+=int(js.iloc[j]['new_vaccinations']) if js.iloc[j]['new_vaccinations']>0 else 0
confirm_day_add['value']=c
new_tests['value']=t
dead_day_add['value']=d
new_vaccinations['value']=v

with open('./dates/confirm_day_add.json','w') as f:
    json.dump(confirm_day_add,f)

with open('./dates/new_vaccinations.json','w') as f:
    json.dump(new_vaccinations,f)

with open('./dates/dead_day_add.json','w') as f:
    json.dump(dead_day_add,f)

with open('./dates/new_tests.json','w') as f:
    json.dump(new_tests,f)

