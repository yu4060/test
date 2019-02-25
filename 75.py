"""
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，
重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
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

# 問71


class FindWords:

    def __init__(self, word):
        self.word = word

    def stopwords(self):
        stop_words = nltk.corpus.stopwords.words('english') + ["'", '"', ':', ';', '.', ',', '-', '--', '!', '?', ' ', '']
        return self.word in stop_words

    def non_features(self):
        non_feauture_words = []
        return self.word in non_feauture_words


# 問72
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
            return lines[11:self.datasize]

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

#問73

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
        self.lr.fit(vectors, labels)

        #結果
        prediction = self.lr.predict(vectors[0:10])
        probability = self.lr.predict_proba(vectors[0:10])
#        for (i, j) in zip(prediction, probability):
#            print("ラベル" + str(i) + ',' + "確率" + str(j))

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


LR = LRAnalyzer('sentiment.txt', 10000)
LR.training()
LR.feature()

