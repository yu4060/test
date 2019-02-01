#57. 係り受け解析
#Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．




from xml.etree import ElementTree
import pydot

tree = ElementTree.parse('/Users/yukimatsuo/Desktop/untitled/nlp.txt.xml')
root = tree.getroot()

edges = []
for i, sentence in enumerate(root.iter('sentence')):
    for dep in sentence.iterfind('./dependencies[@type="collapsed-dependencies"]/dep'):
        governor = dep.findtext('governor')
        dependent = dep.findtext('dependent')
        if dependent != '.' and dependent != ',':
            edges.append((governor, dependent))
    if i == 3:
        g = pydot.graph_from_edges(edges, directed = True)
        g.write_jpeg("{}.jpg".format(i), prog='dot')
        edges =[]
