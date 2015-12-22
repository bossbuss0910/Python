import param
import numpy as np
import sgd
import time

def run():
    #Get Parameter
    data = param.parameter(15,15,5)
    data.get_sample()
    #Get SVD_Data
    MF = sgd.SGD(0.001,0.0001)
    MF.iteration(data,2000)
    #Outuout Result
    MF.re(data)

if __name__=="__main__":
    start = time.time()
    run()
    end = time.time()
    print "RunTime:" + str(end - start)
