"""
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．

述語: nsubj関係とdobj関係の子（dependant）を持つ単語
主語: 述語からnsubj関係にある子（dependent）
目的語: 述語からdobj関係にある子（dependent）
"""


from xml.etree import ElementTree
import pydot

tree = ElementTree.parse('/Users/yukimatsuo/Desktop/untitled/nlp.txt.xml')
root = tree.getroot()

edges_shugo = []
edges_mokutekigo = []
results = []
for i, sentence in enumerate(root.iter('sentence')):
    for dependencies in sentence.iter('dependencies'):
        if dependencies.get('type') == 'collapsed-dependencies':
            for dep in dependencies.iter('dep'):
                if dep.get("type") == 'nsubj':
                    jutsugo = (dep[0].get('idx'), dep.findtext('governor'))
                    shugo = (dep[1].get('idx'), dep.findtext('dependent'))
                    edges_shugo.append((jutsugo, shugo))
                if dep.get("type") == 'dobj':
                    jutsugo = (dep[0].get('idx'), dep.findtext('governor'))
                    mokutekigo = (dep[1].get('idx'), dep.findtext('dependent'))
                    edges_mokutekigo.append((jutsugo, mokutekigo))

    for edge_s in edges_shugo:
        for edge_m in edges_mokutekigo:
            if edge_s[0][0] == edge_m[0][0]:
                results.append((edge_s[1][1], edge_s[0][1], edge_m[1][1]))
                edges_shugo = []
                edges_mokutekigo = []

print(results)
