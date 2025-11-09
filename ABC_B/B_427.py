N = int(input())

# 最適化されたコード
total = 0
A = [1] + [0] * N
for i in range(N):
    # strはイテラブルなのでmapで各文字をintに変換してsumで桁和を求める
    A[i+1] = sum(map(int, str(A[i]))) + total
    total = A[i+1]
print(A[N])

# 自分で書いたコード
# total = 0
# A =[1] + [0] * N
# for i in range(N):
#     char_A = str(A[i])
#     length = len(char_A)
#     for j in range(length):
#         A[i + 1] += int(char_A[j])
#     A[i + 1] += total
#     total = A[i + 1]
# print(A[N])