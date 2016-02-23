# coding: utf-8
f = open("/Users/TomonotiHayshi/GitHub/Python/NLP/Unixcommand/hightemp.txt","r")
file = []
for line in f:
    data = line.split("\t")
    data[3] =  data[3].strip("\n")
    file.append(" ".join(data))

for i in file:
    print i
