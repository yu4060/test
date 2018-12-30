#13. col1.txtとcol2.txtをマージ
#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

with open('col1.txt', "r") as f1:
    data1 = f1.read()
data1 = data1.split('\n') #前回の課題でcol1に入れた改行を一度消している

with open('col2.txt', "r") as f2:
    data2 = f2.read()
data2 = data2.split('\n')
    
with open('col.txt', "w") as f:
    for (a, b) in zip(data1, data2):
        f.write(a + '\t' + b + '\n')

# 確認
# paste col1.txt col2.txt 


