import pandas as pd
import json
all = pd.read_csv('./china.csv')

confirm_day_add={}
suspect_day_add={}
dead_day_add={}
heal_day_add={}
c=[]
s=[]
d=[]
h=[]
se = set()
for line in all['date']:
    if(line[0:4]=='2021'):
        se.add(line)
se=sorted(se)
confirm_day_add['data']=se


for i in range(len(se)):
    js = all.loc[all['date'] == se[i]]
    c.append(0)
    s.append(0)
    d.append(0)
    h.append(0)
    for j in range(len(js)):
        c[i]+=js.iloc[j]['confrim_day_add'] if js.iloc[j]['confrim_day_add']>0 else 0
        s[i]+=js.iloc[j]['suspect_day_add'] if js.iloc[j]['suspect_day_add']>0 else 0
        d[i]+=js.iloc[j]['dead_day_add'] if js.iloc[j]['dead_day_add']>0 else 0
        h[i]+=js.iloc[j]['heal_day_add'] if js.iloc[j]['heal_day_add']>0 else 0
confirm_day_add['value']=c
suspect_day_add['value']=s
dead_day_add['value']=d
heal_day_add['value']=h


with open('./dates/confirm_day_add.json','w') as f:
    json.dump(confirm_day_add,f)

with open('./dates/suspect_day_add.json','w') as f:
    json.dump(suspect_day_add,f)

with open('./dates/dead_day_add.json','w') as f:
    json.dump(dead_day_add,f)

with open('./dates/heal_day_add.json','w') as f:
    json.dump(heal_day_add,f)

