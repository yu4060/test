"""
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""
import re

#CoreNLPをインストールしnlp.txt.xmlを作成

from xml.etree import ElementTree

tree = ElementTree.parse('nlp.txt.xml')
root = tree.getroot()

for word in root.iter('word'):
    print(word.text)

