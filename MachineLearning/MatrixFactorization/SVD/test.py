import param
import numpy as np
import svd
import time

def run():
    #Get Parameter
    data = param.parameter(7,7,4)
    data.get_sample()
    #Get SVD_Data
    MF = svd.SVD(0.001,0.0001)
    MF.iteration(data,2000)
    #Outuout Result
    MF.re(data)

if __name__=="__main__":
    start = time.time()
    run()
    end = time.time()
    print "RunTime:" + str(end - start)
