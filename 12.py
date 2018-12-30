#12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

with open('hightemp.txt', "r") as f:
    data = f.readlines() #データを読み込んでリストにする



with open('col1.txt', "w") as f1, open('col2.txt',"w") as f2: 
    for l in data:
        l = l.split('\t')
        f1.write(l[0] + '\n')
	f2.write(l[1] + '\n')

#with open('col2.txt', "w") as f2: #col2に2列目を保存
#    for l in data:
#        l = l.split('\t')
#        f2.write(l[1] + '\n')

#確認
#cut -f 1-2 hightemp.txt


