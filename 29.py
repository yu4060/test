#29. 国旗画像のURLを取得する
#テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

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


#国旗画像のファイル参照を取得
fragfile = dict['国旗画像']

#以下を参照してMediaWikiのAPIからURL取得
##https://www.mediawiki.org/wiki/API:Imageinfo/ja

import requests

S = requests.Session()
URL = "https://ja.wikipedia.org/w/api.php"
PARAMS = {
    "action":"query",
    "format":"json",
    "prop": "imageinfo",
    "iiprop":"url",
    "titles":"File:" + fragfile,
}

R = S.get(url = URL, params = PARAMS)
DATA = R.json() #dict

#DATAから、key：URLに対応するvalueを取るとURLが取得できる。
DATA['query']['pages']['-1']['imageinfo'][0]['url'] #DATAの辞書の階層がめっちゃ深い
