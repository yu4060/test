#43. 名詞を含む文節が動詞を含む文節に係るものを抽出
#名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

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

#チャンク内の各単語をまとめる関数
def comWords(cnk):
    words = ""
    for mrp in cnk.morphs:
        words += getattr(mrp, "surface")
    return words


# 43の回答
# チャンクごとに、①morphsに名詞のmorphが含まれているか確認、
# ②含まれていた場合、係り先のmorphsに動詞のmorphが含まれているか確認
# ③含まれていた場合、係り元と係り先の文節を表示 ⇒breakして次のチャンクチェック
# 含まれていない場合はcontinue

for stc in article[:30]:
    for cnk in stc:
        for mrp in cnk.morphs:
            if mrp.pos == "名詞" and int(cnk.dst) > 0:
                startwords = comWords(cnk)
                end_no = int(cnk.dst)
                end_cnk = stc[end_no]
                for mrp in end_cnk.morphs:
                    if mrp.pos == "動詞":
                        endwords = comWords(end_cnk)
                        print(startwords + "\t" + endwords)
                        break
                    else:
                        continue
                break
            else:
                continue

