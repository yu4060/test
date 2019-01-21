#35. 名詞の連接
#名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

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

    
#ここから問題35。
count = 0
nseq = []
sol = []
for line in datalist:
    if line['pos'] == '名詞' :
        nseq.append(line['surface'])
        count += 1
    else:
        if count > 1:
            sol.append(nseq)
        count = 0
        nseq = []

sol
