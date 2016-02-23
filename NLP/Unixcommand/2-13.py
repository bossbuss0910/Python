file = "/Users/TomonotiHayshi/GitHub/Python/NLP/Unixcommand/"
r1 = open(file + "col1.txt","r")
r2 = open(file + "col2.txt","r")
w = open(file + "marge.txt","w")
first = []
second = []
for line1 in r1:
    ll = line1.split("\n")
    first.append(ll[0])
for line2 in r2:
    ll = line2.split("\n")
    second.append(ll[0])

for i in range(len(first)):
    w.write(first[i] + " " + second[i])
    w.write("\n")
