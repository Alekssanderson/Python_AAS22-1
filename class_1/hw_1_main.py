# Задание 1:

# 1) Посчитать Сумму ряда 0 - 88888888:

# 1.1) Вариант 1:
sum_numbers = 0
for item in range(88888889):
    sum_numbers += item
print(sum_numbers)
# Ответ: 3950617249382716

# 1.2) Вариант 2:
A = [i for i in range(88888889)]
sum_numbers = A[-1] * len(A) / 2
print(sum_numbers)
# Ответ: 3950617249382716.0

# 1.3) Вариант 3:
A = range(88888889)
print(sum(A))
# Ответ: 3950617249382716

# 1.4) Вариант 4:
print(sum(range(88888889)))
# Ответ: 3950617249382716



# 2) Посчитать среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]:

# 2.1) Вариант 1:
A = [3, 4, 56, 100, 2, 2, 3]
print(sum(A)/len(A))
# Ответ: 24.285714285714285

# 2.2) Вариант 2:
A = [3, 4, 56, 100, 2, 2, 3]
sum_numbers = 0
len_numbers = len(A)
while A:
    sum_numbers += A.pop()
print(sum_numbers/len_numbers)
# Ответ: 24.285714285714285



# 3) Заменить в строке "asdxfghyxyx" все буквы "х" на "у":

strng = "asdxfghyxyx"
B = list(strng)
for i in range(len(B)):
    if B[i] == "x":
        B.pop(i)
        B.insert(i, "y")
print(B)
# Ответ: ['a', 's', 'd', 'y', 'f', 'g', 'h', 'y', 'y', 'y', 'y']



# 4) Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30], кратных и 3 и 5:

A = [3, 4, 56, 100, 15, 2, 20, 30]
multipl = 1
for i in range(len(A)):
    if A[i] % 3 == 0 and A[i] % 5 == 0:
        multipl *= A[i]
print(multipl)
# Ответ: 450 (15х30)



# 5) Заменить все буквы "x" на "у" в исходной строке без использования дополнительной:

strng = "asdxfghyxyx"
print(strng.replace("x", "y"))
# Ответ: asdyfghyyyy