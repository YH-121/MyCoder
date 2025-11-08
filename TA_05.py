N, K = map(int, input().split())
count = 0

# for x in range(1, N + 1):
#     for y in range(1, N + 1):
#         for z in range(1, N + 1):
#             if x + y + z == K:
#                 count += 1

for x in range(1, N + 1):
    for y in range(1, N + 1):
        z = K - x - y
        if 1 <= z <= N:
            count += 1

print(count)