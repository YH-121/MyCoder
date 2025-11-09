N, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
for i in range(N):
    if total - A[i] == M:
        print("Yes")
        exit()
print("No")