N = int(input())
A = list(map(int, input().split()))
Q = int(input())

sum_A = [0] * (N + 1)
for i in range (1, (N + 1)):
    sum_A[i] = sum_A[i - 1] + A[i - 1]

for _ in range(Q):
    L, R = map(int, input().split())
    if (sum_A[R] - sum_A[L - 1]) > (R - L + 1) / 2:
        print("win")
    elif (sum_A[R] - sum_A[L - 1]) == (R - L + 1) / 2:
        print("draw")
    else:
        print("lose")