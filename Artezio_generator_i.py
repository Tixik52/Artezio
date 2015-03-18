def generator_i():
	yield 1
	
	
i = int(input("Ввведите число запросов генератора: "))
for x in range(0, i):
	print("Ваше значение генератора: ", generator_i())