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


# 計算量O(N)
# # 早期終了（和が絶対に作れない場合）
# if K < 3 or K > 3 * N:
#     print(0)
#     exit()

# count = 0
# for x in range(1, N + 1):
#     lo = max(1, K - x - N)
#     hi = min(N, K - x - 1)
#     if lo <= hi:
#         count += (hi - lo + 1)


print(count)