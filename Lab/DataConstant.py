def input():
  f = open("/Users/TomonotiHayshi/Desktop/GDrive/Train1781re/learning1781sort.csv","r")
#  f = open("/Users/TomonotiHayshi/Desktop/GDrive/test1781sort.csv","r")
#  p = open("/Users/TomonotiHayshi/Desktop/GDrive/learning1781con.csv","w")
  a = 0
#  lost = 1209600
#  lost = 1814400
  lost = 2592000
#  lost = 5184000
#  lost = 10368000
#  lost = 15552000
  b = -1
  count = 0
  user = []
  movie = []
  rate = []
  timestampe = []
  lenl = []
  dic = {}
  for line in f:
    data = line[:-1].split(",")
    if a == int(data[0]):
      timestampe.append(int(data[3]))
    else:
      if timecheck(timestampe,lost) == True:
        print "User:" + str(a) + " OK"
        user.append(a)
        lenl.append(len(timestampe))
        count += 1
      timestampe = []
      timestampe.append(int(data[3]))
      a += 1
  print count
  print user
  f.close()
  write2(user,lenl)

def timecheck(time,lost):
  for i in range(len(time)-1):
    if (time[i+1]-time[i]) > lost:
      return False
  return True

def output(CD):
    list = testmake()
    p = open(CD + "test1781sort.csv","r")
    a = open(CD + "Train1781re/test364.csv","w")
    for line in p:
        data = line.split(",")
        user = int(data[0])
        if user in list:
            a.write(line)
    p.close()
    a.close()


def testmake():
    userls = []
    f = open("/Users/TomonotiHayshi/Desktop/GDrive/Train1781re/learning364.csv")
    for line in f:
        data = line.split(",")
        if int(data[0]) not in userls:
            userls.append(int(data[0]))
    return userls

def write2(userls,len):
    a = 0
    count = 0
    f = open("/Users/TomonotiHayshi/Desktop/GDrive/Train1781re/learning1781sort.csv","r")
    p = open("/Users/TomonotiHayshi/Desktop/GDrive/learning1781con.csv","w")
#    f = open("/Users/TomonotiHayshi/Desktop/GDrive/test1781sort.csv","r")
#    p = open("/Users/TomonotiHayshi/Desktop/GDrive/test1781con.csv","w")
    for line in f:
        data = line.split(",")
        if int(data[0]) == userls[a]:
            p.write(line)
            count += 1
            if count == len[a]:
                a += 1
                count = 0
                if a ==228:
                    break
    f.close()
    p.close()

def write(user,rate,movie,time,p):
  for i in range(len(time)):
    l = str(user) + "," + str(movie[i]) + "," + str(rate[i]) + "," + str(time[i])
    p.write(l)
    p.write("\n")

if __name__=="__main__":
    CD = "/Users/TomonotiHayshi/Desktop/GDrive/"
#    input()
    output(CD)
