
n = 3

#* output = ["((()))","(()())","(())()","()(())","()()()"]


def backtrack(index, total, brackets, res):
  if index >= len(brackets):
    if total == 0:
      res.append("".join(brackets))
    return

  if total > len(brackets) // 2:
    return

  elif total < 0:
    return

  brackets[index] = "("
  sum = total + 1
  backtrack(index+1, sum, brackets, res)
  brackets[index] = ")"
  sum = total - 1

  backtrack(index+1, sum, brackets, res)

res = []
backtrack(0, 0, [""] * (2*n), res)
print(res)

#~ TC: O(2^n)
#~ SC: O(2N)