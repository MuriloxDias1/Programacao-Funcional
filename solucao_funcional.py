from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

doubled_numbers = list(map(lambda x: x * 2, numbers))

even_numbers = list(filter(lambda x: x % 2 == 0, doubled_numbers))

total_sum = reduce(lambda x, y: x + y, even_numbers)

print("Lista original:", numbers)
print("Números dobrados:", doubled_numbers)
print("Números pares dobrados:", even_numbers)
print("Soma total dos números pares dobrados:", total_sum)
