N = int(input())
A = list(map(int, input().split()))

ans = 1
for i in range(1, N + 1):
    if i > ans:
        break
    ans = max(ans, i + A[i-1] - 1)
    if ans >= N:
        ans = N
        break
print(ans)
