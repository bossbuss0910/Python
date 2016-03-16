# coding: utf-8
import MeCab
import json

def import_dic:
    dict = {}
    t = 0
    f = open("/Users/TomonotiHayshi/GitHub/Python/NLP/Morphological analysis/neko.txt.mecab")
    for line in f:
        if line != "EOS":
            data = line.split()
            dict[t] = {}
            data[0] = data[0].decode('utf-8')
            dict[t]["base"] = data[0]
            root = data[1].split(",")
            dict[t]["pos"] = root[0].decode("utf-8")
            dict[t]["pos1"] = root[1].decode("utf-8")
            dict[t]["surface"] = root[6].decode("utf-8")
            t += 1

def print_dic:
    print json.dumps(dict, sort_keys=True, indent=4,ensure_ascii=False)
