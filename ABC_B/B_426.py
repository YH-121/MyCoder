S = input().strip()
set_S = list(set(S))

count_A = S.count(set_S[0])
count_B = S.count(set_S[1])

print(set_S[0] if count_A == 1 else set_S[1])