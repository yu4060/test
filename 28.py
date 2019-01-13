#28. MediaWikiマークアップの除去
#27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．


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

#強調除去
basic2 = re.sub("'{2,}", "", basic)

#内部リンクマークアップ除去
##[[記事名|表示文字]]  => 表示文字か
##[[記事名|表示文字]]  => 記事名　のどちらかにする
basic3 = re.sub(r"\[\[([^]]+)\]\]", lambda m: m.group(1).split("|")[-1], basic2)

#{{hogehoge}}表現の成形。例：{{lang|fr|Dieu et mon droit}}⇒Dieu et mon droit
basic4 = re.sub(r"\{\{([^}]+)\}\}", lambda m: m.group(1).split("|")[-1], basic3)

#htmlマークアップ除去
basic5 = re.sub(r"<([^>]+)>", "", basic4)

#[hogehoge]除去
basic6 = re.sub(r"\[([^]]+)\]", "", basic5)


#フィールド名・値抽出
def getTarget(text):
    for line in text.split('\n'):
        regex = re.compile('\|(.+?)\s=\s(.+)')
        m = re.search(regex, line)
        if m:
            yield m.group(1), m.group(2)
            
#辞書オブジェクトとして格納
for key, value  in getTarget(basic6):
    dict[key] = value

dict
