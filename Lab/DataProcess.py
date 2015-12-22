def input():
  count = {}
  count2 = {}
  item = []
  item2 = []
  i = 0
  j = 0
  k = 0
  dic = {}
  dic2 = {}
  userls = []
  user2ls = []
  f  = open("/Users/TomonotiHayshi/Desktop/GDrive/ml-latest/ratings.csv")
  for line in f:
    if i != 0:
      userdata = line[:-1].split(',')
      userdata[3] = int(userdata[3])
#      if userdata[3] > 1122822000 and userdata[3] < 1406818800:
      if userdata[3] > 1280588400 and userdata[3] < 1406818800:
#      if userdata[3] > 1343746800 and userdata[3] < 1406818800:
        if (userdata[0] not in dic) == True:
          dic[userdata[0]] = {}
        dic[userdata[0]][userdata[1]] = line
#        print dic[userdata[0]]
        if (userdata[0] not in count) == True:
          count[userdata[0]] = 1
        else:
          count[userdata[0]] += 1

      if userdata[3] > 1406818800:
        if (userdata[0] not in dic2) == True:
          dic2[userdata[0]] = {}
        dic2[userdata[0]][userdata[1]] = line
        if (userdata[0] not in count2) == True:
          count2[userdata[0]] =1
        else:
          count2[userdata[0]] += 1
    i = 1
  k1 = 0
  k2 = 0
  for u,k in count.items():
    if k >= 20 and (u in count2) == True:
      if count2[u] >= 20:
        userls.append(u)
        k1 += 1
        for i in range(len(userls)):
          if int(userls[k1 - 1]) < int(userls[i]):
            a = int(userls[i])
            userls[i] = int(userls[k1 - 1])
            userls[k1 - 1] = a
  f.close()
  write(userls,dic)

def write(userls,dic):
  """
  p = open("/Users/TomonotiHayshi/Desktop/OneDrive/More10/UserID"+str(len(userls))+".csv","w")
  for us in range(len(userls)):
    p.write(str(us)+","+str(str(userls[us])))
    p.write("\n")
  p.close()
  """
  f = open("/Users/TomonotiHayshi/Desktop/GDrive/More20/learning"+str(len(userls))+".csv","w")
  for user in range(len(userls)):
    for a,line in dic[str(userls[user])].items():
      f.write(line)
  f.close()


def write2(userls,dic2):
  f = open("/Users/TomonotiHayshi/Desktop/GDrive/More20/test"+str(len(userls))+".csv","w")
  for user in range(len(userls)):
    for a,line in dic2[str(userls[user])].items():
      f.write(line)
  f.close()

if __name__=="__main__":
        input()


