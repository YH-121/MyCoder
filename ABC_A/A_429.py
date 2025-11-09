N, M = map(int, input().split())
for i in range(N):
    if i <= M - 1:
        print("OK")
    else:
        print("Too Many Requests")