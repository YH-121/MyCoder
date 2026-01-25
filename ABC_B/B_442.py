Q = int(input())
A = []
for _ in range(Q):
    A.append(int(input()))

volume = 0
music = False

for a in A:
    if a == 1:
        volume += 1 
    if a == 2 and volume > 0:
        volume -= 1
    if a == 3:
        music = not music
    
    if music and volume >= 3:
        print("Yes")
    else:
        print("No")
