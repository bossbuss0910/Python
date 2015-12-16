import param
import numpy as np
import svd
import time

def run():
    data = param.parameter()
    data.get_sample()
    MF = svd.SVD()
    MF.learn(data)

if __name__=="__main__":
    start = time.time()
    run()
    end = time.time()
    print "RunTime:" + str(end - start)
