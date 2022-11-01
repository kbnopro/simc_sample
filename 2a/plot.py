import matplotlib.pyplot as plt
import tqdm as tqdm
import numpy as np


alpha , beta = 0.3 , 0.5 

def f2 ( x : float ) -> float : 
    return ( alpha * (1-x) - beta * x**2 )



analytical = [0]
index = [0]
delta = 1/1000

for i in tqdm.tqdm(range(1,int(10/delta))):
    index.append(i*delta)
    analytical.append(analytical[-1]+f2(analytical[-1])*delta)



cnt = 0 

# for i in range(len(numerical)):
#     cnt += abs(numerical[i]-analytical[i])

for x in analytical :
    print(x)

plt.plot(index,analytical)
plt.show()



# print(cnt)

