import param
import time
import tensor
import numpy as np

def display(data):
    print "Mode1:U(1)"
    print data.Mode1Matrix
    print
    print "Mode2:U(2)"
    print data.Mode2Matrix
    print
    print "Mode3:U(3)"
    print data.Mode3Matrix
    print

def run(data):
    data.get_sample()
    tf = tensor.HOSVD()
    for mode in range(1,4):
       tf.unfolding(data,mode)
    display(data)
    print "CoreTensor:"
    tf.core_calc(data)
    data.tensor_display(data.coreTensor)

if __name__=="__main__":
    start = time.time()
    data = param.parameter(5,4,3)
    run(data)
    Run_time = time.time() - start
    print "Run_time:" + str(Run_time)
