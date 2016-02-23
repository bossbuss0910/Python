def input(num):
    userls = []
    f = open("/Users/TomonotiHayshi/Desktop/GDrive/More20/50learning"+str(num)+".csv")
    for line in f:
        data = line.split(",")
        user = int(data[0])
        if user not in userls:
            userls.append(user)
    f.close()
    write(userls,num)

def write(userls,num):
    p = open("/Users/TomonotiHayshi/Desktop/GDrive/More20/50UserID"+str(num)+".csv","w")
    for i in range(len(userls)):
        p.write(str(i)+","+str(userls[i]))
        p.write("\n")
    p.close()

if __name__=="__main__":
    input(908)
