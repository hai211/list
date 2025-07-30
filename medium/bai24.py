my_list = [1,2,3,2]
tim_so = 2
dem = 0

for i in range(len(my_list)):
    if my_list[i] == tim_so:
        dem += 1
    if dem == 2:
        print(f'tim thay,chi so {i}')
        break
else:
    print("khong tim thay ")
    
