X, Y, Z = map(int, input().split())

for k in range(100):
    now_X = X + k
    now_Y = Y + k
    
    if now_X == now_Y * Z:
        print("Yes")
        exit()

print("No")