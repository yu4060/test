#39. Zipfの法則
#単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．


import MeCab
import re

#問題30で作成したdatalist
with open('neko.txt.mecab', "r") as f:
    data = f.read().split('\n')

POS_list = []
for line in data:
    if line == 'EOS': 
        continue
    POS = re.split(',|\\t', line)
    POS_list.append(POS)

POS_list2 = POS_list[0:-1] 

datalist = []
for line in POS_list2:
    dict = {'surface': line[0], 'base': line[7], 'pos': line[1], 'pos1': line[2]}
    datalist.append(dict)


#ここから問題39
surface_list = []
for line in datalist:
    surface_list.append(line['surface'])

#X軸 orderlist Y軸countlist
from collections import Counter

counter = Counter(surface_list)

countlist = []
for word, count in counter.most_common():
    countlist.append(count)

orderlist = range(1, len(countlist) +1)

#グラフ作成
import numpy as np
import matplotlib.pyplot as plt
    
plt.xscale('log')
plt.yscale('log')
plt.scatter(orderlist, countlist)
