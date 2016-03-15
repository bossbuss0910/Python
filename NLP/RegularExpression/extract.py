# coding: utf-8
import json

def inp(title):
    file = "/Users/TomonotiHayshi/GitHub/Python/NLP/RegularExpression/"
    f = open(file + "jawiki-country.json","r")
    for line in f:
        data = json.loads(line)
        if data["title"] == title:
            ass = data
            return ass





