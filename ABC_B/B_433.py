N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(N):
    found = -1
    # i番目の人の左側(i-1から0まで)を逆順に探索
    for j in range(i - 1, -1, -1):
        if A[j] > A[i]:
            found = j + 1
            break
    ans.append(found)

print("\n".join(map(str, ans)))