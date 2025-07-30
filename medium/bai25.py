my_list = [1, 2, 3, 4, 5]
n = 3

if n > len(my_list):
    print("N lớn hơn độ dài danh sách")
else:
    result = my_list[:n]
    print("N phần tử đầu tiên:", result)
