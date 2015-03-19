
def func_list_a(lst):
	return [x**2 for x in lst]
		
def func_list_b(lst):
	return [x for x in lst[1::2]]
		
def func_list_c(lst):
	return [x**2 for x in lst[1::2] if x != 0 and x%2 == 0]
	

print(func_list_a([1,2,3,4,5,6,7,8,9,10]))
print(func_list_b([1,2,3,4,5,6,7,8,9,10]))
print(func_list_c([1,2,3,4,5,6,7,8,9,10]))
