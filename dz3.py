#3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
def defference (number: list) -> float:
    print(number)
    min = float((number[0]))%1
    max = float((number[0]))%1
    for i in number:
        i = (float(i))%1
        if i == 0:
            continue
        if i > max:
            max = i
        elif i < min:
            min =  i
    return round((max-min),4)
test = [1.1, 1.251, 3.1, 5, 10.01]
print('min - max(test):',defference(test))
