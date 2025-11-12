X, Y = map(int, input().split())
print((X + Y - 1) % 12 + 1)

# Z = X + Y
# print(Z if Z <= 12 else Z - 12)

# if Z > 12:
#     print(Z - 12)
# else:
#     print(Z)