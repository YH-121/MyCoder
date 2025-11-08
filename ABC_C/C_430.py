# N, A, B = map(int, input().split())
# S = input().strip()
# count = 0
# for l in range(N-A+1):
#     for r in range(A, N):
#         sub = S[l:r+1]
#         if sub.count("a") >= A and sub.count("b") < B:
#             count += 1
# print(count)


#上でも動く！でも計算量O(N^3)でTLEする
#累積和だとO(N^2)でいける？かも
N, A, B = map(int, input().split())
S = input().strip()
count = 0
count_a = [0] * (N + 1)
count_b = [0] * (N + 1)
for i in range(1, N + 1):
    count_a[i] = count_a[i - 1] + (1 if S[i - 1] == 'a' else 0)
    count_b[i] = count_b[i - 1] + (1 if S[i - 1] == 'b' else 0)
for l in range(N-A+1):
    for r in range(A, N):
        if count_a[r + 1] - count_a[l] >= A and count_b[r + 1] - count_b[l] < B:
            count += 1
print(count)