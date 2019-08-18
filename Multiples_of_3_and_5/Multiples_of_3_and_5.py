import numpy as np

vector = np.arange(1,1000)

print(vector[(vector%5 == 0) | (vector%3 == 0)].sum())