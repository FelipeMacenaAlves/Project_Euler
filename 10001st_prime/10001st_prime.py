import numpy as np
import math

def factors(x):
	values = np.arange(1,math.ceil(x**0.5)+1)
	factors_ = values[x%values == 0]
	factors_ = np.unique(np.concatenate([factors_,x/factors_]))

	return factors_

def is_prime(x):
	if len(factors(x)) == 2:
		return True
	else:
		return False

n = 2
count = 0
while count != 10001:
    if is_prime(n):
        count+=1
    n+=1

print(n-1)