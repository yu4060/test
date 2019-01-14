#34. 「AのB」
#2つの名詞が「の」で連結されている名詞句を抽出せよ．

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
    
#ここから問題34。「posが名詞・surfaceが"の"・posが名詞」の順番に並んでいる箇所を発見すればOK?
np_list = []

datalist2 = datalist[1:]
datalist3 = datalist[2:]

for line, line2, line3 in zip(datalist, datalist2, datalist3):
    if line['pos'] == '名詞' and line2['surface'] == 'の' and line3['pos'] == '名詞' :
        np = [line['surface'], line2['surface'], line3['surface']]
        np_list.append(np)

np_list
