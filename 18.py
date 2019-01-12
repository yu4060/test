#18. 各行を3コラム目の数値の降順にソート
#各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

with open('hightemp.txt', "r") as f:
    data = f.readlines() #データを読み込んでリストにする
sorted(data, key=lambda data: data.split('\t')[2], reverse=True)

#　確認
#sort -t "\t" -k 3 -r hightemp.txt
