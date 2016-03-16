import MeCab

m = MeCab.Tagger()

f = open("/Users/TomonotiHayshi/GitHub/Python/NLP/Morphological analysis/neko.txt")
data = f.read()
f.close()

f = open("/Users/TomonotiHayshi/GitHub/Python/NLP/Morphological analysis/neko.txt.mecab","w")
f.write(m.parse(data))
f.close()
