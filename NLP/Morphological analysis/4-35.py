# coding: utf-8
import makedic

dict = {}
t = 0
f = open("/Users/TomonotiHayshi/GitHub/Python/NLP/Morphological analysis/neko.txt.mecab")
line = f.readline()
while line != u"EOS":
    list = {}
    pp = 0
    data = line.split()
    root = data[1].split(",")
    if root[0].decode("utf-8") == u"名詞":
        pp = 1
        list[pp-1] = data[0].decode("utf-8")
        print list[pp-1]
        line = f.readline()
        data1 = line.split()
        root1 = data1[1].split(",")
        while root1[0].decode("utf-8") == u"名詞":
            pp += 1
            list[pp-1] = data1[0].decode("utf-8")
            line = f.readline()
            data1 = line.split()
            root1 = data1[1].split(",")
    if t < pp:
        t = pp
        dict[pp] = list
    line = f.readline()
print t
#for i in range(t):
print dict[t]

