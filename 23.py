#23. セクション構造
#記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

#イギリス部分を抽出
def uk():
    with open('jawiki-country.json', "r") as f:
        for line in f:
            temp = json.loads(line)
            if 'イギリス' in temp['title']:
                return  temp['text']

#セクション抽出のジェネレーター
def getSec(text):
    for line in text.split('\n'):
        sec = re.match('(=+)\s*([^=]*)(=+)', line)
        if sec:
            yield sec.group(2), len(sec.group(1)) -1
            
#表示
text = uk()
for title, level in getSec(text):
    print(title, level)
