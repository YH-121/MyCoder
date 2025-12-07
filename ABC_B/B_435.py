N = int(input())
A = list(map(int, input().split()))

sum_A = [0] * (N + 1)
for i in range(N):
    sum_A[i + 1] = sum_A[i] + A[i]
# print(sum_A)

cnt = 0
for l in range(1, N):
    for r in range(l, N + 1):
        _A = sum_A[r] - sum_A[l - 1]
        for i in range(l, r + 1):
            if _A % A[i - 1] == 0:
                break
            if i == r:
                cnt += 1
                # print(l, r)
print(cnt)
