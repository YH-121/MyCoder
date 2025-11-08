N, X = map(int, input().split())
A = list(map(int, input().split()))

if any(a == X for a in A): # if X in Aでも可
    print("Yes")
else:
    print("No")
    
# 最短
# print("Yes" if X in A else "No")