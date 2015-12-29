#Implementatioin by High_Oder_SVD
import param
import math
import numpy as np

class HOSVD:
    def unfolding(self,data,mode):
        if mode == 3:
            d4 = len(data.RateTensor[0])*len(data.RateTensor[0][0])
            Matrix = [[0 for i in range(d4)]for j in range(len(data.RateTensor))]
            for d3 in range(len(data.RateTensor[0])):
                for i in range(len(data.RateTensor[0][0])):
                    for j in range(len(data.RateTensor)):
                        Matrix[j][(len(data.RateTensor[0][0])*d3)+i] = data.RateTensor[j][d3][i]
            data.Mode3Matrix = self.svd(Matrix)

        if mode == 2:
            d4 = len(data.RateTensor[0])*len(data.RateTensor)
            Matrix = [[0 for i in range(d4)]for j in range(len(data.RateTensor[0][0]))]
            for d3 in range(len(data.RateTensor)):
                for i in range(len(data.RateTensor[0])):
                    for j in range(len(data.RateTensor[0][0])):
                        Matrix[j][(len(data.RateTensor[0])*d3)+i] = data.RateTensor[d3][i][j]
            data.Mode2Matrix = self.svd(Matrix)

        if mode == 1:
            d4 = len(data.RateTensor)*len(data.RateTensor[0][0])
            Matrix = [[0 for i in range(d4)]for j in range(len(data.RateTensor[0]))]
            for d3 in range(len(data.RateTensor[0][0])):
                for i in range(len(data.RateTensor)):
                    for j in range(len(data.RateTensor[0])):
                        Matrix[j][(len(data.RateTensor)*d3)+i] = data.RateTensor[i][j][d3]
            data.Mode1Matrix = self.svd(Matrix)

    def svd(self,matrix):
        U,S,V = np.linalg.svd(matrix)
        return U

    def core_calc(self,data):
        data.coreTensor = [[[0 for i in range(len(data.Mode2Matrix))]for j in range(len(data.Mode1Matrix))]for l in range(len(data.Mode3Matrix))]
        for a in range(len(data.Mode3Matrix[0])):
            for b in range(len(data.Mode1Matrix[0])):
                for c in range(len(data.Mode2Matrix[0])):
                    data.coreTensor[a][b][c] = self.calc(data,a,b,c)

    def calc(self,data,a,b,c):
        re = 0
        for i in range(len(data.Mode3Matrix)):
            for j in range(len(data.Mode1Matrix)):
                for l in range(len(data.Mode2Matrix)):
                    re += data.RateTensor[i][j][l] * data.Mode3Matrix[i][a] * data.Mode1Matrix[j][b] * data.Mode2Matrix[l][c]
        return re

    def RMSE(self,data):
        re = [[[0 for i in range(len(data.RateTensor[0][0]))]for j in range(len(data.RateTensor[0]))]for l in range(len(data.RateTensor))]
        total = 0
        for i in range(len(data.RateTensor)):
            for j in range(len(data.RateTensor[0])):
                for l in range(len(data.RateTensor[0][0])):
                    re[i][j][l] = self.error(data,i,j,l)
                    if data.RateTensor[i][j][l] != 0:
                        total += pow(data.RateTensor[i][j][l] - re[i][j][l],2)
        total = total/float(data.Num_User + data.Num_Item + data.Num_Comtext)
        data.tensor_display(re)
        print
        print "RMSE:" + str(total)

    def error(self,data,i,j,l):
        re = 0
        for a in range(len(data.Mode3Matrix)):
            for b in range(len(data.Mode1Matrix)):
                for c in range(len(data.Mode2Matrix)):
                    re += data.coreTensor[a][b][c] * data.Mode3Matrix[i][a] * data.Mode1Matrix[j][b] * data.Mode2Matrix[l][c]
        return re

if __name__=="__main__":
    data = param.parameter(6,5,4)
    data.get_sample()
    tf = HOSVD()
    for i in range(3):
        a = tf.unfolding(data,i+1)
    tf.core_calc(data)
    tf.RMSE(data)
