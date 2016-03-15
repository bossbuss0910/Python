# coding: utf-8
import extract
import json

f = u"イギリス"
data = extract.inp(f)

for line in data["text"].split("\n"):
    if "Category" in line:
        print line
