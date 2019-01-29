"""
50. 文区切り
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
"""
import re

with open('nlp.txt', 'r', encoding='utf8') as f:
    for line in f:
        l1 = re.sub('([\.|;|:|\?|!])(\s+)([A-Z])', r'\1hogehoge\3', line)
        l2 = re.split('hogehoge', l1)

        for l in l2:
            print(l + '\n')
        print('EOS')





