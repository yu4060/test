25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

import json
import re

#イギリス部分を抽出
def uk():
    with open('jawiki-country.json', "r") as f:
        for line in f:
            temp = json.loads(line)
            if 'イギリス' in temp['title']:
                return  temp['text']


#基礎情報抽出
regex = re.compile('基礎情報(.+?)\}\}\n', flags=(re.MULTILINE | re.DOTALL))
m = re.search(regex, uk())
basic = m.group(1)

#フィールド名・値抽出
def getTarget(text):
    for line in text.split('\n'):
        regex = re.compile('\|(.+?)\s=\s(.+)')
        m = re.search(regex, line)
        if m:
            yield m.group(1), m.group(2)
            
#辞書オブジェクトとして格納
for key, value  in getTarget(basic):
    dict[key] = value

dict
