n = [1,2,2,3,2,4]
k = 2
dem = 0

for i in range(0,len(n)):
    if n[i] == k:
        dem += 1
print(dem)