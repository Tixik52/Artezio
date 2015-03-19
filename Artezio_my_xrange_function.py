def my_xrange_function(stop, start=0, step=1):
	list = []
	if start!=0: start, stop = stop, start 
	if not(stop):
		print("Not args", "\n")
		return None
	elif start > stop:
		print("Start > Stop", "\n")
		return None
	else:
		if start != 0: x = start
		else: x = 0
		while x < stop:
			yield x
			x = x + step
			
	
i = my_xrange_function(5,21,3)

for o in i:
	print(o)