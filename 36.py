#36 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

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


#ここから問題36
##DatalistからSurfaceだけを並べたリストをつくる(Counterがリストしか受け付けてくれないので)
surface_list = []
for line in datalist:
    surface_list.append(line['surface'])

##Counterで数え上げる
from collections import Counter
counter = Counter(surface_list)
for word, count in counter.most_common():
    print(word, count)


