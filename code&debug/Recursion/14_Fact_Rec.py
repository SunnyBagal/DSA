def Fact(n):
  if n == 1 or n == 0:
    return n
  return n * Fact(n-1)

print(Fact(5))

#~ TC: O(N)
#~ SC: O(N)

