A, B, C = map(int, input().split())
Z_1 = max(A, B, C)
Z_3 = min(A, B, C)
Z_2 = A + B + C - Z_1 - Z_3
ANS = (Z_1, Z_2, Z_3)

print(''.join(map(str, ANS)))