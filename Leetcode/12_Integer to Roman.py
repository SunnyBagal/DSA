num = 3749
#* output : ~ MMMDCCXLIX
#& M = 1000 + 1000 + 1000 = 3000
#& DCC = 500 + 100 + 100 = 700
#& 40 = XL as 10 less than 50
#& 9 = IX 1 less than 10


values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4 , 1]
symbol = ["M", "CM", "D", "CD", "C" , "XC" , "L", "XL", "X", "IX", "V", "IV", "I" ]

roman = []

for v, sym in zip(values, symbol):
  while num >= v:
    num = num - v
    roman.append(sym)


print("".join(roman))
