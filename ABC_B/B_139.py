A, B = map(int, input().split())
n, rim = divmod(B - 1, A - 1)
if rim == 0:
    print(n)
else:
    print(n + 1)