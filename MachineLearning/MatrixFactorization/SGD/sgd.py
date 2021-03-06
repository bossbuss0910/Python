import numpy as np
import random
import param
import math
from numpy.matrixlib.defmatrix import matrix

class SGD:
    def __init__(self,gamma,lam):
        self.gamma = gamma
        self.lam = lam

    def learn(self,data,ite,all):
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


    def iteration(self,data,iteration):
        all = 0.0
        for user in range(data.Num_User):
            count = 0
            ave = 0.0
            for item in range(data.Num_Item):
                if data.RateMatrix[user][item] != 0:
                    ave += data.RateMatrix[user][item]
                    count += 1
            all += float(ave)/float(count)
        all = all/float(data.Num_User)
        print all
        #Learning
        for ite in range(iteration):
            self.learn(data,ite,all)

    def error(self,user,item,data,all):
        score = data.Bias_User[user] + data.Bias_Item[item] + all
        for k in range(data.Num_K):
            score += data.UserMatrix[user][k] * data.ItemMatrix[k][item]
        return data.RateMatrix[user][item] - score

    def total_error(self,data,all):
        total = 0
        ttotal = 0
        for user in range(data.Num_User):
            count = 0
            for item in range(data.Num_Item):
                if (data.RateMatrix[user][item] != 0.0):
                    count += 1
                    de = self.error(user,item,data,all)
                    total += pow(de,2)
            ttotal += math.sqrt(float(total)/float(count))
        print "RMSE:" + str(total)

    def re(self,data):
        all = 0.0
        for user in range(data.Num_User):
            count = 0
            ave = 0.0
            for item in range(data.Num_Item):
                if data.RateMatrix[user][item] != 0:
                    ave += data.RateMatrix[user][item]
                    count += 1
            all += float(ave)/float(count)
        all = all/float(data.Num_User)

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


