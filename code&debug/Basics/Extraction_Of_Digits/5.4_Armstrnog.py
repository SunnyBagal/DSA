
#& => 153 = 1^3 + 5^3 + 3^3
#&        = 153

n = 153 
num = n
nod = len(str(n))
total = 0 
while num > 0:
  id = num % 10
  total = total + (id**nod)
  num = num//10

print(total == n)

#! TC: O(Log10(N))
#! SC: O(1)