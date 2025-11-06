N, M = map(int, input().split())
grid = [input().strip() for _ in range(N)]
# print('\n'.join(grid[::-1]))

patterns = set()

for i in range(N - M + 1):
    for j in range(N - M + 1):
        block = tuple(row[j:j+M] for row in grid[i:i+M])
        patterns.add(block)
print(len(patterns))