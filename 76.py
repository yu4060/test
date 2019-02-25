"""
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，
正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
"""



import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import GridSearchCV

import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer as PS

import re

import numpy as np


class FindWords:

    def __init__(self, word):
        self.word = word

    def stopwords(self):
        stop_words = nltk.corpus.stopwords.words('english') + ["'", '"', ':', ';', '.', ',', '-', '--', '!', '?', ' ', '']
        return self.word in stop_words

    def non_features(self):
        non_feauture_words = []
        return self.word in non_feauture_words



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
            return lines

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

class LRAnalyzer:
    def __init__(self, filename, datasize):
        self.filename = filename
        self.datasize = datasize
        self.bow = CountVectorizer()
        self.lr = LogisticRegression(solver='sag', max_iter=1000)

    def training_data(self):
        words = []
        labels = []
        ef = ExtractFeature(self.filename, self.datasize)
        for line in ef.extract_data():
            words.append(' '.join(line[1:]))
            if line[0] == '+1':
                labels.append(1.0)
            else:
                labels.append(0.0)
        return words, labels

    def training(self):
        words, labels = self.training_data()
        vectors = self.bow.fit_transform(words)
        self.lr.fit(vectors[11:], labels[11:])

        #結果
        prediction = self.lr.predict(vectors[0:10])
        probability = self.lr.predict_proba(vectors[0:10])
        for (i, j, l, k) in zip(prediction, labels[0:10], words[0:10], probability):
            print("予測ラベル" + str(i) + ',' + "正解ラベル" + str(j) + ',' + "確率" + str(k) + str(l))

    def feature(self):
        features = self.bow.get_feature_names()
        coefficient = self.lr.coef_

        for (i, j) in zip(features, coefficient[0]):
            print(i)
            print(j)
            print("■")

        sorted = np.argsort(coefficient)
        # トップ10
        for i in sorted[0][-1:-11:-1]:
            print(features[i])
        # ワースト10
        for i in sorted[0][:10]:
            print(features[i])


LR = LRAnalyzer('/Users/yukimatsuo/Desktop/untitled/sentiment.txt', 100)
LR.training()
#LR.feature()
