import random
import numpy as np

class parameter:
  def __init__(self,User,Item,comtext):
    #Generate init RateTensor
    self.RateTensor = [[[0 for j in range(Item)]for i in range(User)]for l in range(comtext)]
    #Generate init Decomposing Matrix
    self.coreTensor = [[[]]]
    self.Mode1Matrix = [[random.random() for i in range(User)] for j in range(User)]
    self.Mode2Matrix = [[random.random() for i in range(Item)] for j in range(Item)]
    self.Mode3Matrix = [[random.random() for i in range(comtext)] for j in range(comtext)]
    #BaseData
    self.Num_User = User
    self.Num_Item = Item
    self.Num_Comtext = comtext
  def get_sample(self):
    print "RateTensor:"
    self.RateTensor = [[[float(random.randint(1,5)) for i in range(len(self.RateTensor[0][0]))] for j in range(len(self.RateTensor[0]))]for k in range(len(self.RateTensor))]
    self.tensor_display(self.RateTensor)
    print

  def tensor_display(self,tensor):
      for i in range(len(tensor)):
          if i == 0:
              print "[" + str(np.matrix(tensor[i]))
          if i != 0 and i != (len(tensor) - 1):
              print " " + str(np.matrix(tensor[i])) + ","
          if i != 0 and i == (len(tensor) - 1):
              print " " + str(np.matrix(tensor[i])) + "]"
