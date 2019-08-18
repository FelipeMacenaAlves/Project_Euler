import numpy as np

A = np.arange(1,1000)
B = np.arange(1,1000).reshape(999,1)
C = np.sqrt(A**2+B**2)
result = (A + B) + C

print(B[np.where(result==1000)[0][0]] * A[np.where(result==1000)[0][1]] * C[np.where(result==1000)[0][0],np.where(result==1000)[0][1]])



