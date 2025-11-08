N = int(input())
A = list(map(int, input().split()))




#早い＆簡潔



# 分かりやすい解答例
# count = 0
# # all→A の中のすべての要素が偶数なら True、ひとつでも奇数があれば False
# while all(a % 2 == 0 for a in A):
#     A = [a // 2 for a in A]
#     count += 1
# print(count)


# 自分で書いたやつ。ACだが冗長。
# count = 0
# flag = True
# while flag:
#     for i in range(N):
#         if A[i] % 2 != 0:
#             print(count)
#             flag = False
#             break
#         else:
#             A[i] = A[i] / 2
#     count += 1