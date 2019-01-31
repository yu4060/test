"""
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現（representative mention）に置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
"""
# 例えば、He ＝ HOTTA　とする。
# このとき、HOTTAが代表参照表現、Heが参照表現となる。
#　「He goes to souna everyday.」⇒「HOTTA(He) goes to souna everyday.」とするのが課題。

#  一つの代表参照表現に対応する参照表現は<coreference>タグ内にまとめられている。
#  代表参照表現には<mention representative="true">というタグがつき、その下に参照表現が<mention>タグ付きでまとめられている。
# <要素名 属性="値">内容</要素名>

from xml.etree import ElementTree

tree = ElementTree.parse('/Users/yukimatsuo/Desktop/untitled/nlp.txt.xml')
root = tree.getroot()

texts = ""
for coreference in root.iter('coreference'):
    rep_mention = coreference.findtext('./mention[@representative="true"]/text')
    if rep_mention is None:
        continue
    else:
        #print("■" + str(rep_mention) + "■")

        for i, mention in enumerate(coreference.iter('mention')):
            if i == 0:
                continue
            else:
                sentence_no = mention.findtext('sentence')
                start = mention.findtext('start')
                end = mention.findtext('end')
                text = mention.findtext('text')
                info_mention = (sentence_no, start, end, text)
                #print(info_mention)

                for sentence in root.iter('sentence'):
                    if sentence.get("id") == sentence_no:
                        for token in sentence.iter('token'):
                            if token.get("id") == start:
                                texts += "▼" + rep_mention + "("
                            if token.get("id") == end:
                                texts += token.findtext('word') + ")"
                            else:
                                texts += token.findtext('word')

print(texts)
