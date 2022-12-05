# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def convert_bin(n: int) -> str:
    num = ''
    while n > 0:
        num = str(n % 2) + num
        n //= 2
    return num

n = int(input('Введите число: '))
print(convert_bin(n))
