"""
Stanford Core NLPの句構造解析の結果（S式）を読み込み，
文中のすべての名詞句（NP）を表示せよ．
入れ子になっている名詞句もすべて表示すること．
"""

from xml.etree import ElementTree
import pydot
import re

tree = ElementTree.parse('/Users/yukimatsuo/Desktop/untitled/nlp.txt.xml')
root = tree.getroot()
\

data = []
sentence = []
for parse in root.iter('parse'):
    parse2 = parse.text.replace('(', '■(■')
    parse3 = parse2.replace(')', '■)■')
    parse4 = parse3.split('■')

    for parse5 in parse4:
        parse6 = re.sub(r'([A-Z])( )([a-zA-Z])', r'\1■\3', parse5)
        fragment = parse6.split('■')
        sentence.append(fragment)

    data.append(sentence)
    sentence = []



def split_phrase(sentence):
    count = 0
    phrase = []
    phrase_list = []

    for i in sentence[1:]:
        if i[0] == '(':
            count += 1
            phrase.append(i)

        if len(i) > 1:
            phrase.append(i)

        if i[0] == ')':
            count += -1
            if count == 0:
                phrase_list.append(phrase)
                phrase_list.append(split_phrase(phrase))
            else:
                phrase.append(i)

    return phrase_list

#挫折
