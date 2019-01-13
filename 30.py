#夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
#
#なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

#30. 形態素解析結果の読み込み
#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．



import MeCab
import re

# ファイル読み込み（単語+形態素解析結果ごとにsplit）
# 結果　⇒ data[6] = '猫\t名詞,一般,*,*,*,*,猫,ネコ,ネコ'

## MeCabの返り値のフォーマットは以下
## 表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音

with open('neko.txt.mecab', "r") as f:
    data = f.read().split('\n')
    
# 各形態素をリストに格納
# 結果 ⇒　POS_list[6] = ['猫', '名詞', '一般', '*', '*', '*', '*', '猫', 'ネコ', 'ネコ']

POS_list = []
for line in data:
    if line == 'EOS': #EOSを除去しないとリストの項目数が揃わず後でエラーが出る
        continue
    POS = re.split(',|\\t', line)
    POS_list.append(POS)

POS_list2 = POS_list[0:-1] #最後に空のリストが入ってしまいリストの項目数が揃わない現象への対応

# 必要項目を抽出したリストの作成
datalist = []
for line in POS_list2:
    dict = {'surface': line[0], 'base': line[7], 'pos': line[2], 'pos1': line[3]}
    datalist.append(dict)

print(datalist[0:30])

