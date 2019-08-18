import numpy as np

numbers = np.arange(20,1000000000,20)

for i in range(1,21):
	numbers = numbers[numbers%i == 0]

print(numbers.min())

