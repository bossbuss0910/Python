def input():
  f = open("/Users/TomonotiHayshi/Desktop/GDrive/learning1781sort.csv","r")
  p = open("/Users/TomonotiHayshi/Desktop/GDrive/learning1781con.csv","w")
  a = 0
  lost = 1209600
  lost = 1814400
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
  dic = {}
  for line in f:
    data = line[:-1].split(",")
    if a == int(data[0]):
      timestampe.append(int(data[3]))
    else:
      if timecheck(timestampe,lost) == True:
        print "User:" + str(a) + " OK"
        count += 1
      timestampe = []
      timestampe.append(int(data[3]))
      a += 1
  print count

def timecheck(time,lost):
  for i in range(len(time)-1):
    if (time[i+1]-time[i]) > lost:
      return False
  return True

def write(user,rate,movie,time,p):
  for i in range(len(time)):
    l = str(user) + "," + str(movie[i]) + "," + str(rate[i]) + "," + str(time[i])
    p.write(l)
    p.write("\n")

if __name__=="__main__":
  input()
