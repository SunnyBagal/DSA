text = "loonbalxballpoon"
n = len(text)
want = 'balloon'

hash_map = {}

for i in range(n):
  hash_map[text[i]] = hash_map.get(text[i], 0 ) + 1

count = min (
  hash_map.get('b', 0),
  hash_map.get('a', 0),
  hash_map.get('l', 0) // 2,
  hash_map.get('o', 0) // 2,
  hash_map.get('n', 0),
)

print(count)