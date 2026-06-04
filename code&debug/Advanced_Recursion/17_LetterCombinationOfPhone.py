numMap = {
  "2" : ['a', 'b', 'c'],
  "3" : ['d','e','f'],
  "4" : ['g','h','i'],
  "5" : ['l', 'm', 'n'],
  "6" : ['o','p','q'],
  "7" : ['r','s','t'],
  "8" : ['u','v','w'],
  "9" : ['x', 'y', 'z']
}

#&        digits = "23"
#&        ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def numToLetter(digits):
  if len(digits) == 1:
    print(numMap[digits])
  
  def backtrack(digits):
     for i in range("")


