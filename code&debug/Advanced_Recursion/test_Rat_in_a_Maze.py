from Rat_in_a_Maze import ratMaze


def test_classic_4x4():
  maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1],
  ]
  assert sorted(ratMaze(maze)) == ['DDRDRR', 'DRDDRR']


def test_no_path_exists():
  maze = [
    [1, 0],
    [0, 1],
  ]
  assert ratMaze(maze) == []


def test_single_cell_start_is_end():
  assert ratMaze([[1]]) == ['']


def test_start_blocked():
  maze = [
    [0, 1],
    [1, 1],
  ]
  assert ratMaze(maze) == []


def test_path_requires_left_and_up_moves():
  maze = [
    [1, 1, 1],
    [0, 0, 1],
    [0, 0, 1],
  ]
  assert ratMaze(maze) == ['RRDD']


if __name__ == "__main__":
  for name, fn in list(globals().items()):
    if name.startswith("test_"):
      fn()
      print(f"PASS: {name}")
