例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．

返事をする      と に は        及ばんさと 手紙に 主人は
このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．

コーパス中で頻出する述語（サ変接続名詞+を+動詞）
コーパス中で頻出する述語と助詞パターン
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

if __name__ == '__main__':

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

    #チャンク内の各単語をまとめる関数
    def comWords(cnk):
        words = ""
        for mrp in cnk.morphs:
            words += getattr(mrp, "surface")
        return words


    # ここから47
    result = []
    for stc in article:
        for cnk in stc:
            for mrp in cnk.morphs:
                if mrp.pos == "動詞":
                    verb = mrp.base
                    verbs = ""
                    particles = ""
                    args = ""
                    bgn_no_list = cnk.srcs

                    for i in bgn_no_list:
                        bgn_cnk = stc[int(i)]
                        for j, mrpbgn in enumerate(bgn_cnk.morphs):

#サ変接続だけを抽出
                            if mrpbgn.pos1 == "サ変接続":
                                if j + 1 < len(bgn_cnk.morphs) and bgn_cnk.morphs[j+1].base == "を":
                                    noun = getattr(mrpbgn, "surface")
                                    verbs = noun + "を" + verb

# 動詞にかかる助詞及びその助詞節を抽出
                            if mrpbgn.pos == "助詞" and mrpbgn.base != "を":
                                particle = getattr(mrpbgn, "base")
                                particles += particle + " "
                                arg = comWords(bgn_cnk)
                                args += arg + " "



#動詞にサ変接続がかかっている場合だけ、結果を追加

                    if verbs and args and particles:
                        result.append((verbs, particles, args))
                        break
                    else:
                        continue
                else:
                    continue


    print(result)
