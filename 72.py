"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer as PS

import re

# 問71と同じ


class FindWords:

    def __init__(self, word):
        self.word = word

    def stopwords(self):
        stop_words = nltk.corpus.stopwords.words('english') + ["'", '"', ':', ';', '.', ',', '-', '--', '!', '?', ' ', '']
        return self.word in stop_words

    def non_features(self):
        non_feauture_words = []
        return self.word in non_feauture_words


# 問72：ファイル読み込み⇒単語に分割⇒ストップワード除去⇒
class ExtractFeature:

    def __init__(self, filename, datasize):
        self.filename = filename
        self.datasize = datasize

    def split_data(self):
        lines = []
        with open(self.filename, 'r', encoding ='cp1252') as f:
            for line in f:
                words = re.split('\s', line)
                lines.append(words)
            return lines[:self.datasize]

    def extract_data(self):
        lines = []
        words = []
        for line in self.split_data():
            for word in line:
                find = FindWords(word)
                if find.stopwords() or find.non_features():
                    continue
                else:
                    stemmer = PS()
                    stem = stemmer.stem(word)
                    words.append(stem)
            lines.append(words)
            words = []

        return lines



data = ExtractFeature('sentiment.txt', 5)
for i in data.extract_data():
    print(i)




