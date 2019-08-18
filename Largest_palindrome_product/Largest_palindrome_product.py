import numpy as np

def reverse(x):

	return x[-1::-1]

func = np.vectorize(reverse)

values = (np.arange(100,1000).reshape(900,1)*np.arange(100,1000)).flatten().astype(str)

print(values[values == func(values)].astype(int).max())