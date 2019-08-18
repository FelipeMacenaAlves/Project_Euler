import numpy as np

values = np.arange(2,1000000)
aux = np.where(values!=1)

while len(aux[0]) != 1:
    values = np.where(values == 1, values, np.where(values%2==0, values/2, (3*values)+1))
    aux = np.where(values != 1)

print(np.arange(2,1000000)[aux])
