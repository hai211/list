my_list = [1,2,3,4,5,6]
so_chan = []
so_le = []
for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0 :
        so_chan.append(my_list[i])
    else:
        so_le.append(my_list[i])

print('so chan', so_chan)
print('so le ', so_le)
