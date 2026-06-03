
# words = s.split()
# print(words)
# res = []

# for i in range(len(words) - 1, -1, -1):
#   res.append(words[i])
#   if i!=0:
#     res.append(" ")

# print("".join(res))
s = "the sky is blue"
words = s.split()
n = len(words)
left = 0
right = n - 1

while left < right:
  words[left], words[right] = words[right], words[left]
  left += 1
  right -= 1

print(" ".join(words))