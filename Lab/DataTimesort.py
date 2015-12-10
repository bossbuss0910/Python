def input():
  f = open("/Users/TomonotiHayshi/Desktop/OneDrive/More20/learning1997.csv","r")
  p = open("/Users/TomonotiHayshi/Desktop/OneDrive/learning1997con.csv","w")
  a = 0
  b = -1
  user = []
  movie = []
  rate = []
  timestampe = []
  dic = {}
  for line in f:
    data = line[:-1].split(",")
    if a == int(data[0]):
      b += 1
      movie.append(int(data[1]))
      rate.append(float(data[2]))
      timestampe.append(int(data[3]))
      for i in  range(len(timestampe)):
        if timestampe[i] > timestampe[b]:
          c = timestampe[i]
          d = rate[i]
          e = movie[i]
          timestampe[i] = timestampe[b]
          rate[i] = rate[b]
          movie[i] = movie[b]
          timestampe[b] = c
          rate[b] = d
          movie[b] = e
    else:
      write(a,rate,movie,timestampe,p)
      a += 1
      b = 0
      movie = []
      movie.append(int(data[1]))
      rate = []
      rate.append(float(data[2]))
      timestampe = []
      timestampe.append(int(data[3]))

def write(user,rate,movie,time,p):
  for i in range(len(time)):
    l = str(user) + "," + str(movie[i]) + "," + str(rate[i]) + "," + str(time[i])
    p.write(l)
    p.write("\n")

if __name__=="__main__":
  input()
