s = "aab"

ans = []
sol = []

def backtrack (start):
  if start == len(s):
    ans.append(sol.copy())
    return 
  
  for end in range( start + 1, len(s) + 1 ):
    chunk = s[start: end]
    if chunk == chunk[::-1]:
      sol.append(chunk)
      backtrack(end)
      sol.pop()

backtrack(0)
print(ans)