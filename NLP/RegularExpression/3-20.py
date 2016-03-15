# coding: utf-8
import json

class inp:
    def input(self,title):
        file = "/Users/TomonotiHayshi/GitHub/Python/NLP/RegularExpression/"
        f = open(file + "jawiki-country.json","r")
        for line in f:
            data = json.loads(line)
            if data["title"] == title:
                ass = data
                return ass

tool = inp()
gf = tool.input(u"イギリス")
print gf["text"]




