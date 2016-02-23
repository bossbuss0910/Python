# coding: utf-8
import sys

file = "/Users/TomonotiHayshi/GitHub/Python/NLP/Unixcommand/"
f = open(file + "hightemp.txt","r")
input = sys.stdin.readline()
count = 0
for line in f:
    linel = line.strip("\n")
    print linel
    count += 1
    if count == int(input):
        break

