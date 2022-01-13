import pandas as pd
import json
all = pd.read_csv('./china.csv')
s = set()
for line in all['date']:
    if(line[0:4]=='2021'):
        s.add(line)

ss = set()
for line in all['province']:
    ss.add(line)

for date in s:
    js = all.loc[all['date'] == date]
    ls=[]
    for province in ss:
        h = js.loc[js['province'] == province]
        confirm, dead, heal, suspect, confrim_day_add, suspect_day_add, dead_day_add, heal_day_add = 0, 0, 0, 0, 0, 0, 0, 0
        for i in range(len(h)):
            confirm += h.iloc[i]['confirm']
            dead += h.iloc[i]['dead']
            heal += h.iloc[i]['heal']
            suspect += h.iloc[i]['suspect']
            confrim_day_add += h.iloc[i]['confrim_day_add']
            suspect_day_add += h.iloc[i]['suspect_day_add']
            dead_day_add += h.iloc[i]['dead_day_add']
            heal_day_add += h.iloc[i]['heal_day_add']
        lsi = pd.DataFrame({'province': [province], 'date': [date], 'confirm': [confirm],
                           'dead': [dead], 'heal': [heal], 'suspect': [suspect], 'confirm_day_add': [confrim_day_add],
                           'suspect_day_add': [suspect_day_add], 'dead_day_add': [dead_day_add], 'heal_day_add':
                           [heal_day_add]})
        ls.append(lsi)
    pdjs=pd.concat(ls)
    pdjs.to_json('./json/%s.json'%date,force_ascii=False,orient='records')
