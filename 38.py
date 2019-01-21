#38. ヒストグラム
#単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

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

#Counterで数え上げる
from collections import Counter

counter = Counter(surface_list)

wordlist = []
countlist = []
for word, count in counter.most_common():
    wordlist.append(word)
    countlist.append(count)


#グラフ作成
import numpy as np
import matplotlib.pyplot as plt

plt.hist(countlist, range(0,100))
