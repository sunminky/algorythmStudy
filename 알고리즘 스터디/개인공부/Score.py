arr = []
arr2 = []

for i in range(8):
    arr.append([])
    arr[i].append(i)
    arr[i].append(int(input()))

arr.sort(key=lambda x:x[1])
arr.reverse()

sum = 0
for i in range(5):
    sum += arr[i][1]
    arr2.append(arr[i][0])
print(sum)
arr2.sort()
for i in range(5):
    print(arr2[i]+1,end=" ")