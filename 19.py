#19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
#各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．

with open('hightemp.txt', "r") as f:
    data = f.readlines() #データを読み込んでリストにする

col0 = []

for l in data:
    l = l.split('\t')
    col0.append(l[0])

import collections
collections.Counter(col0)

sorted(collections.Counter(col0).items(), key=lambda x: x[1])
