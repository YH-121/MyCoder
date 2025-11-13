X, Y = map(int, input().split())
A = [X] + [Y]
for _ in range(8):
    t = A[-1] + A[-2]
    if t >= 10:
        t = int(str(t)[::-1])
    A.append(t)
    
print(A[-1])