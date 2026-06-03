# def three_Times(x, n):
#   if n == 0:
#     return
#   print(x, end= " ")
#   three_Times(x, n-1)

# three_Times(3, 4)

# print()
# def func(i, n):
#   if i > n:
#     return
#   print(i ,end=" ")
#   func(i+1,n)

# func(1,8)


def Sum_me(n):
  if n == 1:
    return 1
  return n + Sum_me(n-1)

print(Sum_me(4))

#~ TC = SC = O(N)
#~ Stack space 