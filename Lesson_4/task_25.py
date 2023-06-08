#Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
#Количество повторов добавляется к символам с помощью постфикса формата _n.
#Input: a a a b c a a d c d d
#Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
#Для решения данной задачи используйте функцию .split()
sequence = 'a a a b a c b b d'.split()
letters = {}
result = ''
for i in range(len(sequence)):
    if sequence[i] not in letters.keys():
        letters[sequence[i]] = 1
        result += f'{sequence[i]} '
    else:
        result += f'{sequence[i]}_{letters[sequence[i]]} '
        letters[sequence[i]] += 1
print(result)