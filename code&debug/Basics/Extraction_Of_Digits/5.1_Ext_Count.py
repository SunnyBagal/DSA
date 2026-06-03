import math

n = 5873
num = n 
count = 0
while num > 0:
  count += 1
  num = num // 10
print(count)
print (math.floor(math.log10(n))+1)


#! TC: O(log10(N))
#! SC: O(1)