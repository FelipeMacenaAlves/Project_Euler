import numpy as np

values = np.arange(1,101)

answer = (values.sum()**2) - (values**2).sum()

print(answer)