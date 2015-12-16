import numpy as np
import random
import param
from numpy.matrixlib.defmatrix import matrix

class SVD:
    def __init__(self,gamma = 0.001,lam = 0.0001,ite = 2000):
        self.gamma = gamma
        self.lam = lam
        self.iteration = ite

    def learn(self,data):
        ave = 0.0
        all = 0.0
        for user in range(data.Num_User):
            for item in range(data.Num_Item):
                ave += data.RateMatrix[user][item]
            all += ave/5.0

        for ite in range(self.iteration):
            for user in range(data.Num_User):
                for item in range(data.Num_Item):
                    if (data.RateMatrix[user][item] != 0):
                        error_ui = self.error(user,item,data,all)
                        g_e = self.gamma * error_ui
                        g_l = self.gamma * self.lam
                        data.Bias_User[user] += g_e - g_l * data.Bias_User[user]
                        data.Bias_Item[item] += g_e - g_l * data.Bias_Item[item]
                        for k in range(data.Num_K):
                            old = data.UserMatrix[user][k]
                            data.UserMatrix[user][k] += g_e * data.ItemMatrix[k][item] - g_l * data.UserMatrix[user][k]
                            data.ItemMatrix[k][item] += g_e * old - g_l * data.ItemMatrix[k][item]
            if (ite % 100) == 0:
                self.total_error(data,all)
        self.re(data,all)

    def error(self,user,item,data,all):
        score = data.Bias_User[user] + data.Bias_Item[item] + all
        for k in range(data.Num_K):
            score += data.UserMatrix[user][k] * data.ItemMatrix[k][item]
        return data.RateMatrix[user][item] - score

    def total_error(self,data,all):
        total = 0
        for user in range(data.Num_User):
            for item in range(data.Num_Item):
                if (data.RateMatrix[user][item] != 0.0):
                    de = self.error(user,item,data,all)
                    total += pow(de,2)
        print "Total_Error:" + str(total)

    def re(self,data,all):
        result = [[0 for i in range(data.Num_Item)]for j in range(data.Num_User)]
        for user in range(data.Num_User):
            for item in range(data.Num_Item):
                score = data.Bias_User[user] + data.Bias_Item[item] + all
                for k in range(data.Num_K):
                    score += data.UserMatrix[user][k] * data.ItemMatrix[k][item]
                result[user][item] = score
        print
        print np.matrix(data.RateMatrix)
        print
        print np.matrix(result)


