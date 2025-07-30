my_list1=  [10,20,30,40,50]
my_list2 = [1,3]
my_list3 = []
for i in range(len(my_list1)):
    if i not in my_list2:
        my_list3.append(my_list1[i])
print(my_list3)
