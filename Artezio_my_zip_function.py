
def my_zip_function(*obj):
	if not(obj):
		print("Not args", "\n")
		return None
	else:
		n = my_zip_method_count(obj)
		for number_elem in range(n):
			result = []
			for number_obj in obj:
				result.append(number_obj[number_elem])
			yield (tuple(result))

def my_zip_method_count(*args):
	number = []
	for x in args:
		i=0
		for k in x: i = i + 1
		number.append(i)
	return min(number)

lst = [1,2,3,4,5,6,7,8,9,10]
i = my_zip_function(range(5), ['a','b','c','d'], 'qweasd', lst)
for o in i:
	print(o)

