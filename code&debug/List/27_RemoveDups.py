# arr = [1,1,1,2,3,4,4,7,9,9,9,10]
# n = len(arr)
# freq_map = {}

# for i in range(n):
#   freq_map[arr[i]] = 0
 
# j = 0
# for k in freq_map:
#   arr[j] = k
#   j += 1

# print(arr[:j])

arr = [1,1,1,2,3,4,4,7,9,9,9,10]
n = len(arr)
i = 0
for j in range(1,n):
  if arr[i] != arr[j]:
    i += 1
    arr[i] = arr[j]

print(arr[:i+1])


