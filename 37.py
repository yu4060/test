#37. 頻度上位10語
#出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

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


#ここから問題37
surface_list = []
for line in datalist:
    surface_list.append(line['surface'])

#Counterで数え上げ、上位10語のリストを作る
from collections import Counter

counter = Counter(surface_list)

wordlist = []
countlist = []
for word, count in counter.most_common():
    wordlist.append(word)
    countlist.append(count)


wordlist10 = wordlist[0:10]
countlist10 = countlist[0:10]

#グラフ作成

import numpy as np
import matplotlib.pyplot as plt

left = np.array([1,2,3,4,5,6,7,8,9,10])
height = np.array(countlist10)
plt.bar(left, height, tick_label=wordlist10)
