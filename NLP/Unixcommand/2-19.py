# coding: utf-8
file = "/Users/TomonotiHayshi/GitHub/Python/NLP/Unixcommand/"
f = open(file + "hightemp.txt")
dic = {}
for line in f:
    data = line.split("\t")
    if data[0] not in dic:
        dic[data[0]] = 1
    else:
        dic[data[0]] += 1

for i in sorted(dic.items(),key=lambda x:x[1],reverse=True):
    print i[0]
