T = int(input())
N = int(input())
diff = [0] * (T + 1)
for _ in range(N):
    L, R = map(int, input().split())
    diff[L] += 1
    diff[R] -= 1

num = 0
for i in range(T):
    num += diff[i]
    print(num)