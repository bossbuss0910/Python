# coding: utf-8
import makedic

dict = {}
t = 0
f = open("/Users/TomonotiHayshi/GitHub/Python/NLP/Morphological analysis/neko.txt.mecab")
line = f.readline()
while line != u"EOS":
        data = line.split()
        root = data[1].split(",")
        if root[0].decode("utf-8") == u"名詞":
            str = data[0].decode("utf-8")
            line1 = f.readline()
            data1 = line1.split()
            root1 = data1[1].split(",")
            if data1[0].decode("utf-8") == u"の":
                str1 = data1[0].decode("utf-8")
                line2 = f.readline()
                data2 = line2.split()
                root2 = data2[1].split(",")
                if root2[0].decode("utf-8") == u"名詞":
                    str2 = data2[0].decode("utf-8")
                    print str +" "+ str1 +" "+ str2
        line = f.readline()

