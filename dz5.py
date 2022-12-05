# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fibonachi(n: int) -> list:
    ans_arr = []
    a, b = 1, 1
    for i in range(n-1):
            ans_arr.append(a)
            a, b = b, a + b
    a, b = 0, 1
    for i in range(n):
        ans_arr.insert(0,a)
        a, b = b, a - b
    return ans_arr

n = int(input('Введите число: '))
print(fibonachi(n))