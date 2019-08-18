def fibonacci(n,limit=None):
	data = [1,2]
	if limit:
		while data[-1] < limit:
			data.append(data[-1] + data[-2])
		else:
			data = data[:-1]
	else:
		if n < 3:
			return data
		for element in range(n-2):
			data.append(data[-1] + data[-2])
	return data

print(sum(filter(lambda x: x%2 == 0,fibonacci(None,4000000))))