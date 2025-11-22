N = int(input())
X = [ None ] * N
Y = [ None ] * N
for i in range(N):
    X[i], Y[i] = map(int, input().split())
Q = int(input())

# 各座標にある点の数を数える
S = [[0] * 1501 for i in range(1501)]
for i in range(N):
    S[X[i]][Y[i]] += 1

#　累積和をとる
T = [[0] * 1501 for i in range(1501)]
for i in range(1, 1501):
    for j in range(1, 1501):
        T[i][j] = S[i][j] + T[i - 1][j] + T[i][j - 1] - T[i - 1][j - 1]

out = []
for i in range(Q):
    a, b, c, d = map(int, input().split())
    ans = T[c][d] - T[a - 1][d] - T[c][b - 1] + T[a - 1][b - 1]
    out.append(ans)

print("\n".join(map(str, out)))