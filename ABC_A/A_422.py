a, b = map(int, input().split('-'))
if b == 8:
    a += 1
    b = 1
else:
    b += 1
print(f"{a}-{b}")



# S = list(input())

# if S[2] == "8":
#     S[0] = str(int(S[0]) + 1)
#     S[2] = "1"
# else:
#     S[2] = str(int(S[2]) + 1)


# print(*S, sep="")