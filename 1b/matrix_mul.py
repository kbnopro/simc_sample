import numpy as np 
import matplotlib.pyplot as plt 

t , del_t = 0 , 0.01
Nxs = 0 
a , b = 1.5*1e-3 , 2.5*1e-5
N = 2000


def P1 ( cur_Nxs : int ) -> np.float64 :
    return a*del_t*(N-cur_Nxs)

def P2 ( cur_Nxs : int ) -> np.float64 :
    return b*del_t*cur_Nxs*(cur_Nxs-1)/2

def P3 ( cur_Nxs : int ) -> np.float64 :
    return 1 - P1( cur_Nxs ) - P2( cur_Nxs )

prob = np.array([[np.float64(0) for i in range(N+1)] for j in range(N+1)])


for i in range(0,N):
    prob[i][i+1] += P1(i)
for i in range(2,N+1):
    prob[i][i-2] += P2(i)
for i in range(0,N+1):
    prob[i][i] += P3(i)

init_prob = prob 
print(prob)

cnt = 0 

while abs(prob - (prob @ prob)).sum() > np.float64(0.00000001) :
    prob = ( prob @ prob )
    cnt += 1 
    print(abs(1-prob[0].sum()))

print(cnt)


plt.plot(prob[0])
plt.ylabel("steady-state probability")
plt.show()