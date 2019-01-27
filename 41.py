#41. 係り受け解析結果の読み込み（文節・係り受け）
#40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ


import re

# 前処理はXML形式のほうがいいかもという気がしたのでファイルを再度作成
## cabocha -f3 neko.txt -o neko.xml.cabocha

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __repr__(self):
        return "surface: %s base: %s pos: %s pos1: %s " % (self.surface, self.base, self.pos, self.pos1)



#class Chunkを定義
class Chunk:
    def __init__(self, no,dst):
        self.no = no
        self.morphs = []
        self.dst = dst
        self.srcs = []

    def __repr__(self):
        return "no: %s morphs: %s dst: %s srcs: %s　\n" % (self.no, self.morphs, self.dst, self.srcs)

if __name__ == '__main__':
    data = []
    #ファイル読み込み
    with open('neko.xml.cabocha', "r") as f:
        data = f.read().split('\n')

    # ここから41
    # articleはsentenceのリスト
    # sentenceはchunkのリスト
    # chunkはid、morphs、dst、srcsのリスト
    # morphsはmorphのリスト


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
                        dstto = sentence[getdst - 1] #リンク先のチャンク
                        dstto.srcs.append(dstfrom) # リンク先チャンクのsrcsにdstfromを追加

# sentenceのリストをarticleに追加
                article.append(sentence)
                sentence = []

#　結果の表示
word = ""
result = []
for ch in article[8]: #　8文目に含まれているchunkがch
    for m in ch.morphs:
        sfc = getattr(m, "surface")
        word += sfc
    dstto = getattr(ch, "dst")
    result.append((word, dstto))
    word = ""

print(result)
