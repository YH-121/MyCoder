N, L, R = map(int, input().split())
S = input()

print("No" if "x" in S[L-1:R] else "Yes")


# for i in range(L, R + 1):
#     if S[i - 1] == 'x':
#         print("No")
#         exit()
# print("Yes")