# coding: utf-8
import makedic

data = makedic.import_dic()

for num in range(len(data)):
    if data[num]["pos"] == u"名詞" and data[num]["pos1"] == u"サ変接続":
        print u"名詞" + " " + data[num]["base"]
