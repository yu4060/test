'''
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい． 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ． ただし，出力は以下の仕様を満たすようにせよ．

動詞を含む文節において，最左の動詞の基本形を述語とする
述語に係る助詞を格とする
述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．

始める  で
見る    は を
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語と格パターンの組み合わせ
「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
'''

# 41の結果を利用しarticleというデータリストを作成

import re

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __repr__(self):
        return "surface: %s base: %s pos: %s pos1: %s " % (self.surface, self.base, self.pos, self.pos1)

class Chunk:
    def __init__(self, no,dst):
        self.no = no
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def __repr__(self):
        return "no: %s morphs: %s dst: %s srcs: %s　\n" % (self.no, self.morphs, self.dst, self.srcs)

data = []
#ファイル読み込み
with open('neko.xml.cabocha', "r") as f:
    data = f.read().split('\n')

article = []
sentence = []
chunk = None
edges = []
for line in data:
    if re.search('<chunk', line):
        search_no = re.search('(id=\")(.+?)(\"\slink)', line)
        no = search_no.group(2)

        search_dst = re.search('(link=\")(.+?)(\"\srel)', line)
        dst = search_dst.group(2)

        chunk = Chunk(no, dst)

    elif re.search('<tok', line):
        tok = re.search('(feature=\")(.+?)(\">)', line)
        pos = re.split(',', tok.group(2))
        sfc = re.search('(\">)(.+?)(</tok>)', line)
        chunk.morphs.append(Morph(
            sfc.group(2),
            pos[6],
            pos[0],
            pos[1],
        ))

    elif line == ' </chunk>':
        if chunk:
            sentence.append(chunk)
        chunk = []

    elif line == '</sentence>':
        if sentence:

            # srcsをセット
            for ch in sentence:
                getdst = int(getattr(ch, "dst"))
                dstfrom = getattr(ch, "no")
                if getdst > 0:
                    dstto = sentence[getdst] #リンク先のチャンク
                    dstto.srcs.append(dstfrom) # リンク先チャンクのsrcsにdstfromを追加

            # sentenceのリストをarticleに追加
            article.append(sentence)
            sentence = []

# ここから45
result = []
for stc in article[:10]:
    for cnk in stc:
        for mrp in cnk.morphs:
            if mrp.pos == "動詞" and len(cnk.srcs) > 0:
                verb = getattr(mrp, "base")
                particles = ""
                end_no_list = cnk.srcs
                for i in end_no_list:
                    end_cnk = stc[int(i)]
                    for mrp in end_cnk.morphs:
                        if mrp.pos == "助詞":
                            particle = getattr(mrp, "base")
                            particles += particle + " "
                result.append((verb, particles))
                break
            else:
                continue


print(result)
