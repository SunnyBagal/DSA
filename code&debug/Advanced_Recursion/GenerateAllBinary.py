
def solve(index, flag, number, result):
  if index >= len(number):
    result.append("".join(number))
    return
  number[index] = "0"
  solve(index+1, True, number, result)
  if flag == True:
    number[index] = "1"
    solve(index+1, False, number, result)
    number[index] = "0"


def generateBinary(n):
  number = ["0"] * n
  result = []
  solve(0, True, number, result)
  return result


print(generateBinary(3))

