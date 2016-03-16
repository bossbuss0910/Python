# coding: utf-8
import makedic

data = makedic.import_dic()

for num in range(len(data)):
    if data[num]["pos"] == u"動詞":
        print data[num]["surface"]
