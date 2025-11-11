N = int(input())
A = list(map(int, input().split()))

# 最適化
ans = [-1] * N
used = set()

for i in range(N):
    if A[i] != -1:
        if A[i] in used:
            print("No")
            exit()
        ans[i] = A[i]
        used.add(A[i])

available = [i for i in range(1, N + 1) if i not in used]

for i in range(N):
    if ans[i] == -1:
        ans[i] = available.pop(0)

print("Yes")
print(*ans)





# 一回目
# ans = [-1] * N
# used = [None] * N

# for i in range(N):
#     if A[i] in used:
#         print("No")
#         exit()
#     elif A[i] != -1:
#         ans[i] = A[i]
#         used[i] = A[i]

# for i in range(N):
#     if ans[i] == -1:
#         for j in range(1, N + 1):
#             if j not in used:
#                 ans[i] = j
#                 used[i] = j
#                 break

# print("Yes")
# print(*ans)