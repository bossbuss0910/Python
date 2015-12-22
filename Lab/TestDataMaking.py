def input(users):
    f = open("/Users/TomonotiHayshi/Desktop/GDrive/TrainData"+str(users)+"/UserID"+str(users)+".csv","r")
    list = []
    for line in f:
        Udata = line.split(",")
        list.append(Udata[1])
    f.close()
    output(list,users)

def output(list,users):
    f = open("/Users/TomonotiHayshi/Desktop/GDrive/TrainData"+str(users)+"/test.csv","w")
    p = open("/Users/TomonotiHayshi/Desktop/GDrive/ml-latest/ratings.csv","r")
    p.readline()
    ucount = 0
    for line in p:
        Udata = line.split(",")
        Udata[0] = int(Udata[0])
        if int(list[ucount]) == Udata[0]:
            if int(Udata[3]) > 1406818800:
                f.write(line)

    print ucount

def usercount(list,users):
    count = {}
    c = 1
    co = 0
    f = open("/Users/TomonotiHayshi/Desktop/GDrive/ml-latest/ratings.csv","r")
    f.readline()
    for line in f:
        udata = line.split(",")
        if int(udata[0]) == c:
            co += 1
        else:
            count[c] = co
            print str(c)+":"+str(count[c])
            c += 1
            co = 1 

if __name__=="__main__":
    users = 1781
    list = []
    usercount(list,users)
    #input(users)
