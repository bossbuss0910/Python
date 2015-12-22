import random
import numpy as np

class parameter:
  def __init__(self,User,Item,comtext,K1,K2,K3):
    #Generate init RateTensor
    self.RateTensor = [[[0 for j in range(Item)]for i in range(User)]for l in range(comtext)]
    #Generate init Decomposing Matrix
    self.Mode1Matrix = [[random.random() for i in range(K1)] for j in range(User)]
    self.Mode2Matrix = [[random.random() for i in range(K2)] for j in range(Item)]
    self.Mode3Matrix = [[random.random() for i in range(K3)] for j in range(comtext)]
    self.UserMatrix = [[]]
    self.ItemMatrix = [[]]
    self.Bias_User = []
    self.Bias_Item = []
    #BaseData
    self.Num_User = User
    self.Num_Item = Item
    self.Num_Comtext = comtext
    self.Num_K1 = K1
    self.Num_K2 = K2
    self.Num_K3 = K3

  def get_sample(self,user,item,comtext):
    self.RateTensor = [[[float(int((random.random()*10)%5)) for i in range(item)] for j in range(user)]for k in range(comtext)]
    print self.RateTensor
