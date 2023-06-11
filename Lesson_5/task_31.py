#Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0= 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#Требуется найти N-е число Фибоначчи
#Input: 7
#Output: 21
#Задание необходимо решать через рекурсию

def fibonacci(n):
    if (n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))
n = int(input("Введите число членов последовательности:"))
print("Последовательность Фибоначчи:")
for i in range(n):
    print(fibonacci(i))