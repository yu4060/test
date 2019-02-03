"""
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．
"""

# 単語についてはnltkにストップリストを使用。記号も追加
import nltk
from nltk.corpus import stopwords

class StopWord:

    def __init__(self, word):
        self.word = word
        self.stop_words = nltk.corpus.stopwords.words('english') + ["'", '"', ':', ';', '.', ',', '-', '!', '?', "'s"]

    def find(self):
        return self.word in self.stop_words

    def result(self):
        print(self.word, self.find())

a = StopWord("love")
a.result()
