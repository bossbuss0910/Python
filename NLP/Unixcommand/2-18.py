# coding: utf-8
import sys

file = "/Users/TomonotiHayshi/GitHub/Python/NLP/Unixcommand/"
f = open(file + "hightemp.txt","r")
count = 0
asd = []
for line in f:
    line = line.split("\t")
    asd.append(line)

for line in sorted(asd, key=lambda x: float(x[2]), reverse=True):
        print "\t".join(line).strip("\n")

