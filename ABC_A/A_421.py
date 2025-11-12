N = int(input())
S = [input().strip() for _ in range(N)]
# for i in range(N):
#     S.append(input().strip())

X, Y = input().split()
X = int(X)

print("Yes" if S[X - 1] == Y else "No")

# if S[X - 1] == Y:
#     print("Yes")
# else:
#     print("No")