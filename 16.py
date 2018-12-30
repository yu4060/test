#16. ファイルをN分割する
#自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

n = input("ファイル数を指定：")
n = int(n)

with open('hightemp.txt', "r") as f:
    data = f.readlines() #データを読み込んでリストにする

l = -(-len(data) // n) #行数（全行数 /  分割ファイル数、あまりは切り上げ）
print("ファイル全体の行数:" + str(len(data)))
print("1ファイルに書き込む行数:" + str(l))

for i in range(n): #iはファイル数、jは行数
    with open('file{}.txt'.format(i+1), "w") as f:
        for j in range(i*l, min(len(data), (i+1)*l)): #(0行からl行目の1行前まで)（l行目から2*l行の1行前まで）…
            f.write(data[j])

# 確認(多分以下であっているが自分の環境では確認できず）
# split -n 3 hightemp.txt split.txt




