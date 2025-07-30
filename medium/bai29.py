my_list = [1, 2, 3, 4, 5]
even_sum = 0
odd_sum = 0

for num in my_list:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Tong chan:", even_sum)
print("Tong le:", odd_sum)

