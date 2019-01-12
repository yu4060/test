#20. JSONデータの読み込み
#Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

import json

with open('jawiki-country.json', "r") as f:
    for line in f:	#fを1行ずつ読み込む
        temp = json.loads(line)
        if temp['title'] == 'イギリス':	#fのキーtitleがイギリスだったら表示
            print(temp['text'])
            break
