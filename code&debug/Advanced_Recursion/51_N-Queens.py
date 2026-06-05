# n =4 
# ans = []
# board = ["." * n for _ in range(n)]

# def isSafe(row, col):
#     duprow = row
#     dupcol = col

#     # upper-left diagonal
#     while row >= 0 and col >= 0:
#         if board[row][col] == "Q":
#             return False
#         row -= 1
#         col -= 1

#     # left side
#     row = duprow
#     col = dupcol
#     while col >= 0:
#         if board[row][col] == "Q":
#             return False
#         col -= 1

#     # lower-left diagonal
#     row = duprow
#     col = dupcol
#     while row < n and col >= 0:
#         if board[row][col] == "Q":
#             return False
#         row += 1
#         col -= 1

#     return True

# def solve(col):
#     if col == n:
#         ans.append(board.copy())
#         return

#     for row in range(n):
#         if isSafe(row, col):
#             board[row] = (
#                 board[row][:col] + "Q" + board[row][col + 1:]
#             )
#             solve(col + 1)
#             board[row] = (
#                 board[row][:col] + "." + board[row][col + 1:]
#             )


# solve(0)

# print(ans)

#~ TC: O(n! * n)
#~ SC: O(n^2) O(N)





#! —————— Optimal Solution ———————————————————————————————————————

def solve(col, board, ans, leftRow, upperDiagonal, lowerDiagonal, n):
  if col == n:
    ans.append(board.copy())
    return
  
  for row in range(n):
    if (
      leftRow[row] == 0
      and lowerDiagonal[row + col] == 0
      and upperDiagonal[n - 1 + col - row] == 0
    ):
      
      board[row] = board[row][:col] + "Q" + board[row][col+1:]
      leftRow[row] = 1
      lowerDiagonal [row + col] = 1
      upperDiagonal [ n - 1 + col - row ] = 1

      solve(col + 1, board, ans , leftRow, upperDiagonal, lowerDiagonal, n)

      board[row] = board[row][:col] + "." + board[row][col+1:]
      leftRow[row] = 0
      lowerDiagonal [row + col] = 0
      upperDiagonal [ n - 1 + col - row ] = 0

def solvedNQueens() :
  n = 4
  ans = []
  board = ["." * n for _ in range(n)]
  leftRow = [0] * n
  upperDiagonal = [0] * ( 2 * n - 1)
  lowerDiagonal = [0] * ( 2 * n - 1)
  solve(0, board, ans, leftRow, upperDiagonal, lowerDiagonal, n)
  return ans

print(solvedNQueens())