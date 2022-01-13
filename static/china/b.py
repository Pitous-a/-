import pandas as pd

all = pd.read_csv('./china.csv')
max=0
for line in all['confrim_day_add']:
    if(line>max):
        max=line
print(max)


