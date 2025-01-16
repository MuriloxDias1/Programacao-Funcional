
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled_numbers = []
for number in numbers:
    doubled_numbers.append(number * 2)

even_numbers = []
for number in doubled_numbers:
    if number % 2 == 0:
        even_numbers.append(number)

total_sum = 0
for number in even_numbers:
    total_sum += number

print("Lista original:", numbers)
print("Números dobrados:", doubled_numbers)
print("Números pares dobrados:", even_numbers)
print("Soma total dos números pares dobrados:", total_sum)
