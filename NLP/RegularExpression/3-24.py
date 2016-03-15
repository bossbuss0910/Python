# coding: utf-8
import re
import json
import extract

data = extract.inp(u"イギリス")
data = data["text"].split("\n")

for line in data:
    asd = re.search(u"^(File|ファイル):(.*\.jpg)\|.*(\|/*)?",line)
    if asd is not None:
        print asd.group(2)
