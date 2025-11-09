X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())
P = [int(input()) for _ in range(Q)]

total = X
for i in P:
    idx = i - 1
    total += W[idx]
    W[idx] = -W[idx]
    print(total)