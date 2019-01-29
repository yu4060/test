"""
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
"""
import re

#CoreNLPをインストールしnlp.txt.xmlを作成

from xml.etree import ElementTree

tree = ElementTree.parse('nlp.txt.xml')
root = tree.getroot()

for token in root.iter('token'):
    if token.findtext('NER') == "PERSON":
        print(token.findtext('word'))
