numMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

#&        digits = "23"
#&        ["ad","ae","af","bd","be","bf","cd","ce","cf"]


digits = "23"

def generateAll(digits):

  if len(digits) == 0:
    return []
  
  numMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
  
  res = []

  def backtrack(combination, new_digit):
    if not new_digit:
      res.append(combination)
      return

    for letter in numMap[new_digit[0]]:
      backtrack(combination + letter, new_digit[1:])


  backtrack("", digits)
  return res

print(generateAll(digits))