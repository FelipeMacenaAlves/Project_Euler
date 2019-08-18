import numpy as np
import math

def factors(x):
	values = np.arange(1,math.ceil(x**0.5)+1)
	factors_ = values[x%values == 0]
	factors_ = np.unique(np.concatenate([factors_,x/factors_]))

	return len(factors_)

fac = np.vectorize(factors)

aux = np.array([0])
for i in range(1,100000000,10000):
    aux = np.concatenate([aux,np.arange(i,i+10000)])
    numbers = aux.cumsum(dtype=np.int64)
    facs = fac(numbers)
    if len(numbers[facs>500])>=1:
        print(numbers[facs>=500][0])
        break




