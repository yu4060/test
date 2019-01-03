#21. カテゴリ名を含む行を抽出
#記事中でカテゴリ名を宣言している行を抽出せよ．

import json
import re

ctg = []
with open('jawiki-country.json', "r") as f:
    for line in f:
        temp = json.loads(line)
        
        if re.search('\[Category', temp['text']):
            ctg.append(temp['text'])
        else:
            pass
