import pandas as pd

all=pd.read_csv('./world.csv')
s=set()
for line in all['date']:
    if(line[0:4]=='2021'):
        s.add(line)

for date in s:
    js=all.loc[all['date']==date]
    js.to_json('./json/%s.json'%date,force_ascii=False,orient='records')