H, W, N = map(int, input().split())
# 二次元累積和ではWとHを+2しておく
Z = [[0] * (W + 2) for _ in range(H + 2)]

for i in range(N):
    a, b, c, d = map(int, input().split())
    Z[a][b] += 1
    Z[a][d + 1] -= 1
    Z[c + 1][b] -= 1
    Z[c + 1][d + 1] += 1

for i in range(1, H + 1):
    for j in range(1, W + 1):
        Z[i][j] = Z[i][j] + Z[i][j - 1] + Z[i - 1][j] - Z[i - 1][j - 1]
        print(Z[i][j], end=" ")
    print()



# 計算量おおすぎかも　O(N*H*W)
# for i in range(N):
#     a, b, c, d = map(int, input().split())
#     for x in range(a, c + 1):
#         for y in range(b, d + 1):
#             Z[x][y] += 1

# for i in range(1, H + 1):
#     for j in range(1, W + 1):
#         print(Z[i][j], end=" ")
#     print()