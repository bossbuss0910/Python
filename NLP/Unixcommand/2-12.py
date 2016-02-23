file = "/Users/TomonotiHayshi/GitHub/Python/NLP/Unixcommand/"
f = open(file + "hightemp.txt","r")
first = []
second = []
for line in f:
    data = line.split("\t")
    first.append(data[0])
    second.append(data[1])

w1 = open(file + "col1.txt","w")
w2 = open(file + "col2.txt","w")
for i in range(len(first)):
    w1.write(first[i] + "\n")
    w2.write(second[i] + "\n")
