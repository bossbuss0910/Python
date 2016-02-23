# coding: utf-8
import sys

file = "/Users/TomonotiHayshi/GitHub/Python/NLP/Unixcommand/"
f = open(file + "hightemp.txt","r")
input = sys.stdin.readline()
count = 0
asd = []

for line in f:
    asd.append(line)

for i in range(len(asd)):
    ss = asd[len(asd)-1-i].strip("\n")
    print ss
    count += 1
    if count == int(input):
        break

