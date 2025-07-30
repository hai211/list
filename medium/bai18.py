my_list = [1, 2, 2, 3, 2, 4]
xoa = 2
ket_qua = []

for i in my_list:
    if i != xoa:
        ket_qua.append(i)

print("Danh sách sau khi xóa:", ket_qua)
