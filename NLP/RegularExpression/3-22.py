# coding: utf-8
import extract
import json
import re

#original
data = extract.inp(u"イギリス")
sentence = data["text"].split("\n")

for line in sentence:
    if "Category" in line:
        lie = line.strip("[]").split(":")
        print lie[1]
print
#answer with regularexpression
data = extract.inp(u"イギリス")
sentence = data["text"].split("\n")
for line in sentence:
    category_line = re.search("^\[\[Category:(.*?)(|\|.*)\]\]$", line)
    if category_line is not None:
        print(category_line.group(1))
