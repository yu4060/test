#31. 動詞
#動詞の表層形をすべて抽出せよ．

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
    
#ここから問題31。posが動詞になっているもののsurfaceを抽出すればOK
v_list = []
for line in datalist:
    if line['pos'] == '動詞':
        v_list.append(line['surface'])

print(v_list)
