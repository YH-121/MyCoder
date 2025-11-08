D = int(input())
N = int(input())
diff = [0] * (D + 1)
for _ in range(N):
    L, R = map(int, input().split())
    diff[L - 1] += 1
    diff[R] -= 1

sum = 0
for i in range(D):
    sum += diff[i]
    print(sum)