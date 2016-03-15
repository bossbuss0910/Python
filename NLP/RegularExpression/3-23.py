# coding: utf-8
import json
import extract
import re

data = extract.inp(u"イギリス")
data = data["text"].split("\n")

for line in data:
    section = re.search("^==+(.*[^=])==+$",line)
    if section is not  None:
        if re.search("^==([^=].*[^=])==$",line) is not None:
            a = 1 
        else:
            a = 2
        print u"セクション名:" + section.group(1) + u" レベル:" + str(a)
