import random
import numpy as np

class parameter:
  def __init__(self,User = 7,Item = 7,K = 4):
    #Generate init RateMatrix
    self.RateMatrix = [[0 for i in range(Item)] for j in range(User)]
    #Generate init Decomposing Matrix
    self.UserMatrix = [[random.random() for i in range(K)] for j in range(User)]
    self.ItemMatrix = [[random.random() for i in range(Item)] for j in range(K)]
    self.Bias_User = [random.random() for i in range(User)]
    self.Bias_Item = [random.random() for j in range(Item)]
    #BaseData
    self.Num_User = User
    self.Num_Item = Item
    self.Num_K = K

  def get_sample(self):
    Mat = np.matrix(self.RateMatrix)
    self.RateMatrix =[[float(int((random.random()*10)%5)) for i in range(Mat.shape[1])] for j in range(Mat.shape[0])]
    print np.matrix(self.RateMatrix)
