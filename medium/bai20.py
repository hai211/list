my_list = [1,2,3,4,2,4,5]
check = True

for i in range(0,len(my_list)):
    for j in range(i+1,len(my_list)):
        if my_list[j]==my_list[i]:
            check = False
            break
if check == False:
    print('False')
else:
    print('True')