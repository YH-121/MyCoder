N, Q = map(int, input().split())
A = list(map(int, input().split()))
sum_A = [0] * (N + 1)
for i in range (1, (N + 1)):
    sum_A[i] = sum_A[i - 1] + A[i - 1]
    
for i in range(Q):
    L, R = map(int, input().split())
    print(sum_A[R] - sum_A[L - 1])