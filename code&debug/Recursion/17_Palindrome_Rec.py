
is_pal = True
def palindrome(s):
  if len(s) <= 1:
    return is_pal
  
  start = 0
  end = len(s) - 1 
  while start < end:
    if s[start] != s[end]:
      return not is_pal 
    start += 1
    end -= 1
  return is_pal

print(palindrome("NitiN"))

    
def pali(s):
  def helper(start, end):
    if start >= end:
      return True
    
    if s[start] != s[end]:
      return False

    return helper(start+1, end-1)
  return helper(0, len(s)-1)

print(pali("mom"))

  