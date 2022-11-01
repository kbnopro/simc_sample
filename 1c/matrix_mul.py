import numpy as np 
import matplotlib.pyplot as plt 

t , del_t = 0 , 0.1
Nxs = 0 
a , b = 1.5*1e-3 , 2.5*1e-5

class query :

    def __init__(self, n : int) -> None: 
        self.N = n
        self.prob = np.array([[np.float64(0) for i in range(self.N+1)] for j in range(self.N+1)])


        for i in range(0,self.N):
            self.prob[i][i+1] += self.P1(i)
        for i in range(2,self.N+1):
            self.prob[i][i-2] += self.P2(i)
        for i in range(0,self.N+1):
            self.prob[i][i] += self.P3(i)

        self.init_prob = self.prob 


        while abs(self.prob - (self.prob @ self.init_prob)).sum() > np.float64(0.0000000001) :
            self.prob = ( self.prob @ self.prob )


    def P1 ( self , cur_Nxs : int ) -> np.float64 :
        return a*del_t*(self.N-cur_Nxs)

    def P2 ( self , cur_Nxs : int ) -> np.float64 :
        return b*del_t*cur_Nxs*(cur_Nxs-1)/2

    def P3 ( self , cur_Nxs : int ) -> np.float64 :
        return 1 - self.P1( cur_Nxs ) - self.P2( cur_Nxs )

    def ans(self) -> np.int64 :
        sum = 0 
        for val , prob in enumerate(self.prob[0]) :
            sum += val*prob
        return sum 

from tqdm import tqdm 

MAX_N = 700

res = []

for i in tqdm(range(0,MAX_N,3)):
    res.append(query(i).ans())



plt.plot(np.array(res))
plt.ylabel("expected C_i")
plt.xlabel("value of N")
plt.show()