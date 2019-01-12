24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ


import json
import re

#イギリス部分を抽出
def uk():
    with open('jawiki-country.json', "r") as f:
        for line in f:
            temp = json.loads(line)
            if 'イギリス' in temp['title']:
                return  temp['text']

#ファイル参照箇所抽出
def getFile(text):
    for line in text.split('\n'):
        m = re.search('(?:File|ファイル):([^\|]+)\|', line)
        if m:
            yield m.group(1)
            
#表示
text = uk()
for title in getFile(text):
    print(title)
