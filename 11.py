#11. タブをスペースに置換
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

with open('hightemp.txt', "r") as f:
    data = f.read() #データを読み込む
data = data.replace("	", " ") #データを置換

with open('hightemp11.txt', "w") as f: #新しいファイルに置換したデータを書き込む
    f.write(data)

#確認
# sed 's/\t/ /g' hightemp.txt
# tr '\t' ' ' < hightemp.txt
# expand -t 1 hightemp.txt
