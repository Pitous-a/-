import pandas as pd

all = pd.read_csv('./world.csv')
max=0
for line in all['total_cases']:
    if(line>max):
        max=line
print(max)