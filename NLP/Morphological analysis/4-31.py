# coding: utf-8
import MeCab
import makedic

dic = makedic.import_dic()

for num in range(len(dic)):
    if dic[num]["pos"] == u"動詞":
        print dic[num]["base"]
