#14. 先頭からN行を出力
#自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．


n = input("行数を指定：") #コマンドライン引数がなにか分からない
n = int(n) #inputで入れた値は文字列になってしまうようなので変換

with open('hightemp.txt', "r") as f:
    data = f.readlines() #データを読み込んでリストにする
    
for i in range(n):
        print(data[i])

# 確認
# head -n 5 hightemp.txt

