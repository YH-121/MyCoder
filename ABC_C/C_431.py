N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))
H.sort()
B.sort()

i = j = 0
count = 0

# 2本ポインタ
while i < N and j < M:
    if H[i] <= B[j]:
        count += 1
        i += 1
        j += 1
    else:
        j += 1

if count >= K:
    print("Yes")
else:
    print("No")