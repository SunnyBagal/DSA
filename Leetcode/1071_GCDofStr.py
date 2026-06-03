str1 = "ABCABC" 
str2 = "ABC"

if str1 + str2 != str2 + str1:
   print()

def get_gcd(a: int, b: int) -> int:
  while b != 0:
      a, b = b, a % b
  return a
  
print(str1[:get_gcd(len(str1), len(str2))])