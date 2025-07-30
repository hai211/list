# n = int(input(' '))
# if  n<=0:
#     print('no')
# else:
#     tong = 0
#     for i in range(n):
#         so = int(input(f'nhap{i+1}: '))
#         if so<0:
#             print('no')
#             so = int(input(f'nhap{i+1}: '))
#             tong+=so
#     trung_binh = tong/n
# print(f'tbcong cua {n} so tu nhien la:{trung_binh}')



# menu = ["man",'man','men']
# print(menu.index("men"))

s = "hellopjuh"
# print(s.index("o"))
# print(s)

for i in range(1,len(s)):
    if s[i] == "o":
        print(i)