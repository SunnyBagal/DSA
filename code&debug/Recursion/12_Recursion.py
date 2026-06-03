def reverse(n):
  if n == 0:
    return
  print(n,end=" ")
  reverse (n-1)

reverse(5)