str = "Now I need a drink,alcoholic of corse,after the heavy lectures involing quantam mechanics"
sp = str.split(",")
#print sp
sp1 = ["","",""]
for i in range(len(sp)):
    sp1[i] = sp[i].split(" ")
for i in range(len(sp1)):
    for j in range(len(sp1[i])):
        print len(sp1[i][j])
