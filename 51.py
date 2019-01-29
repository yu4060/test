"""
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
"""
import re

def splitSentences():
    with open('nlp.txt', 'r', encoding='utf8') as f:
        for line in f:
            l1 = re.sub('([\.|;|:|\?|!])(\s+)([A-Z])', r'\1hogehoge\3', line)
            l2 = re.split('hogehoge', l1)

            for l in l2:
                yield l + '\n'

def splitWords():
    for s in splitSentences():
        words = re.split('\s+', s)

        for w in words:
            yield w

for i in splitWords():
    print(i)

