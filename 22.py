#22. カテゴリ名の抽出
#記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import json
import re

ctg = []
with open('jawiki-country.json', "r") as f:
    for line in f:
        temp = json.loads(line)
        
        match = re.search('\[Category\:(.+?)((\|.*\]){0,1}(\]))', temp['text'])
        if match:
            print(match.group(1))

