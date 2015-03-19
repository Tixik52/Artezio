
def my_zip_function(*obj):
	if not(obj):
		print("No args", "\n")
		return None
	else:
		for number_elem in range(min(len(x) for x in obj)):
			result = []
			for number_obj in obj:
				result.append(number_obj[number_elem])
			yield (tuple(result))



lst = [1,2,3,4,5,6,7,8,9,10]
i = my_zip_function(range(10), ['a','b','c','d','e'], 'qweasdzxc', lst, range(17))
for o in i:
	print(o)

