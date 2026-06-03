num = [7,2,1,5,6,4,8]


#! Brute Force 
n = len(num)
max_profit = 0
for i in range(n):
  for j in range(i+1, n):
    if num[j] > num[i]:
      currentSum = num[j] - num[i]
      max_profit = max(max_profit, currentSum)

print(max_profit) 

#~ TC : O(N(N-1)/2) ~ O(N^2)
#~ SC : O(1)

#* Optimal Solution

min = num[0]
maxi_profit = float('-inf')
for i in range(n):
  if num[i] < min :
    min = num[i]
  maxi_profit = max(maxi_profit, num[i] - min)

print(maxi_profit)

#~ TC : O(N)
#~ SC : O(1)