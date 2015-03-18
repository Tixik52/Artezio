
def my_cat_function_read(*file):
		
	if not(file):
		print("Not args", "\n")
	else:
		l = len(file)
		for x in range(0,l):
			if (os.path.isfile(file[x])):
				f = open(file[x], 'r', encoding="utf-8")
				return(f.read())
				f.close()
			else:
				print("File %a isn't found" % file[x], "\n")
		
def my_cat_function_write(m, fileW, *fileR):
	if not(fileR):
		new_file = input()
		nf = open(fileW, m, encoding="utf-8")
		nf.write(new_file)
		nf.close()
	else:
		fileW = tuple(fileW)
		for y in fileW:
			nf = open(y, m, encoding="utf-8")
			for x in fileR:
				f = my_cat_function_read(x)
				nf.write(f)
			nf.close()

# Формат выводы из файла: cat имя файла[ов]										(cat test.txt)
#																				(cat test.txt test2.txt test3.txt)
# Формат записи в файл: cat > имя файла для записи 								(cat > test.txt)
#						cat [имя файла для чтения] > имя файла для записи		(cat test.txt > 123.txt)
#																				(cat test.txt test3.txt > 123.txt)							
# Формат дозаписи в файл: cat >> имя файла для записи 							(cat >> test.txt)
#						  cat [имя файла для чтения] >> имя файла для записи	(cat test.txt >> 123.txt)
#																				(cat test.txt test3.txt >> 123.txt)							
		
import os
str = input("Введите команду: ")
print("\n")
list = str.split(' ')
list.remove('cat')

if list.count('>'):
	if list.index('>') == 0:
		list.remove('>')
		my_cat_function_write('w', list[0])
	else:
		i = list.index('>')
		fileW = list[i+1:]
		fileR = list[0:i]
		my_cat_function_write('w', fileW, *fileR)
elif list.count('>>'):
	if list.index('>>') == 0:
		list.remove('>>')
		my_cat_function_write('a', list[0])
	else:
		i = list.index('>>')
		fileW = list[i+1:]
		fileR = list[0:i]
		my_cat_function_write('a', fileW, *fileR)
else:
	file = my_cat_function_read(*list)
	print(file)