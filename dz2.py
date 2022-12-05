#2-Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def zadacha2():
    spisok = input("Задайте список чисел через пробел:   ").split()
    print(spisok)
    rez = []
    for i in range ((len(spisok)+1)//2):
        rez.append(int(spisok[i])*int(spisok[-(i+1)]))
    print(rez)    
zadacha2()   