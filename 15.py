#15. 末尾のN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．


n = input("行数を指定：")
n = int(n)

with open('hightemp.txt', "r") as f:
    data = f.readlines() #データを読み込んでリストにする
data = list(reversed(data)) #一度逆順にする
r = []

for i in range(n): 　#下からn行を取得
    r.append(data[i])

r2 = list(reversed(r)) #天地が逆転しているので戻す

for i in range(n): #表示
    print(r2[i])

# 感想：もう少しスマートなやりかたはないのか
# 確認
# tail -n 5 hightemp.txt

