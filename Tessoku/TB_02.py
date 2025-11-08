A, B = map(int, input().split())

if any(100 % i == 0 for i in range(A, B + 1)):
    print("Yes")
else:
    print("No")