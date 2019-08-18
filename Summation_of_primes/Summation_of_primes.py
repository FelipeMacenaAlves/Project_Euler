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

values = sum(list(filter(is_prime,range(2,2000000))))

print(values)

