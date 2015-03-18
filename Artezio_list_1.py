#5.Изучить list comprehension. Написать короткие функции, принимающие один аргумент-список чисел и возвращающие:
#a.    Список квадратов чисел;
#b.    Каждый второй элемент списка;
#c.    Квадраты чётных элементов на нечётных позициях;


def func_list_a(lst):
	return [x**2 for x in lst]
		
def func_list_b(lst):
	return [x for x in lst[1::2]]
		
def func_list_c(lst):
	lst2=[]
	for x in lst[1::2]:
		lst2.append(x)
		lst2.append(x**2)
	return lst2
	
def func_list_c2(lst):
	return [x for x in lst[1::2] if x is list[1::2]]

if __name__ == '__main__':
	
	print(func_list_a([1,2,3,4,5,6,7,8,9,10]))
	print(func_list_b([1,2,3,4,5,6,7,8,9,10]))
	print(func_list_c([1,2,3,4,5,6,7,8,9,10]))
	print(func_list_c2([1,2,3,4,5,6,7,8,9,10]))