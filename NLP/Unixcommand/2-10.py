# coding: utf-8
f = open("/Users/TomonotiHayshi/GitHub/Python/NLP/Unixcommand/hightemp.txt","r")
count = 0
for line in f:
    count += 1 

print "行数：" + str(count)
