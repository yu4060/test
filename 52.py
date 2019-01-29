"""
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．
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

from nltk.stem.porter import PorterStemmer as PS

ps = PS()

for w in splitWords():
    print(w + '\t' + ps.stem(w))

