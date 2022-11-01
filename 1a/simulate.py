""" Stimulate the process and print out the result to log """

import matplotlib.pyplot as plt

t , del_t = 0 , 0.1
Nxs = 0 
a , b = 1.5*1e-3 , 2.5*1e-5
N = 100 
max_t = 10

def P1 () -> float :
    return a*del_t*(N-Nxs)

def P2 () -> float :
    return b*del_t*Nxs*(Nxs-1)/2

def P3 () -> float :
    return 1 - P1() - P2()

from random import random 




for i in range(5):
    log = []
    cur_t = 0 
    Nxs = 0 
    while cur_t <= max_t:
        case = random()
        if case < P1() :
            Nxs = Nxs + 1 
        elif case < P1() + P2() :
            Nxs = Nxs - 2
        cur_t = cur_t + del_t
        log.append(Nxs)
    plt.plot(log)
    plt.show()


    
