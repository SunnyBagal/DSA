arr = [1,2,3,4,5]
n = len(arr)
print(arr[-2])

d = int(input("Enter number of rotations: "))

temp = arr[0:d]
print(temp)


for i in range(d, n):
    arr[i-d] = arr[i]

for j in range(n-d, n):
    arr[j] = temp[j-(n-d)]

print(arr)