#40. 係り受け解析結果の読み込み（形態素）
#形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．


import re

# 前処理
## 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．
## cabocha -f1 neko.txt -o neko.txt.cabocha


#Classを定義
class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
        
    def print(self):
        print([self.surface, self.base, self.pos, self.pos1])

#ファイル読み込み
with open('neko.txt.cabocha', "r") as f:
    data = f.read().split('\n')

# 各形態素をリストに格納
# 結果 ⇒　POS_list[6] = ['猫', '名詞', '一般', '*', '*', '*', '*', '猫', 'ネコ', 'ネコ']

article = []
sentence = []
for line in data:
    if line[:1] == '*': #最初の文字が* からはじまる箇所は除去も除去
        continue
    elif line == 'EOS': #EOSを除去しないとリストの項目数が揃わず後でエラーが出る
        if sentence:
            article.append(sentence)
        sentence = []
    else:
        POS = re.split(',|\\t', line)
        sentence.append(POS)


#article2 = article[0:-1] #最後に空のリストが入ってしまいリストの項目数が揃わない現象への対応

# 必要項目を抽出したリストの作成
datalist = []
for line in article2[3]:
    datalist.append(Morph(
        line[0],
        line[7],
        line[1],
        line[2],
    ))

for morph in datalist:
        morph.print()

