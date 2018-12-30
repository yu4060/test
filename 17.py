#17. １列目の文字列の異なり
#1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．


with open('hightemp.txt', "r") as f:
    data = f.readlines() #データを読み込んでリストにする


col1 = set() #1列目の集合を作成
for x in data:
    x1 = x.split('\t')
    col1.add(x1[0])

print(col1)

