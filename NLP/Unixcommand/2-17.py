# coding: utf-8
import sys

file = "/Users/TomonotiHayshi/GitHub/Python/NLP/Unixcommand/"
f = open(file + "hightemp.txt","r")
group = []
for line in f:
    line = line.split("\t")
    if line[0] not in group:
        group.append(str(line[0]))
for i in range(len(group)):
    print group[i]

