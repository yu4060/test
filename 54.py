"""
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""
import re

#CoreNLPをインストールしnlp.txt.xmlを作成

from xml.etree import ElementTree

tree = ElementTree.parse('nlp.txt.xml')
root = tree.getroot()

for token in root.iter('token'):
    word = token.findtext('word')
    lemma = token.findtext('lemma')
    pos = token.findtext('POS')
    print(str(word) + "\t" + str(lemma) + "\t" + str(pos))
