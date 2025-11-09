S = str(input())
char_count = len(S)
S_center = (char_count + 1) // 2

print(S[:S_center - 1] + S[S_center:])