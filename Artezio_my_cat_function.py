
def my_cat_function(*file):
	if not(file):
		print("Not args", "\n")
	else:
		for x in range(0,len(file)):
			#print("%a: \n" % file[x])
			if(os.path.isfile(file[x])):
				f = open(file[x], 'r', encoding="utf-8")
				print(f.read())
				f.close()
			else:
				print("File isn't found", "\n")


import os
			
print("Function without args")
my_cat_function()

print("Function with one args")
my_cat_function('test.txt')

print("Function with more args")
my_cat_function('test.txt', 'test2.txt', 'test3.txt')
