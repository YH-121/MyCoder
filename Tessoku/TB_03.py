N = int(input())
A = list(map(int, input().split()))

for i in range(N):
	for j in range(i+1, N):
		for k in range(j+1, N):
			if A[i] + A[j] + A[k] == 1000:
				print("Yes")
				exit()

print("No")


# set_A = set(A)
# if any(a + b + c == 1000 for a in set_A for b in set_A for c in set_A):
#     print("Yes")
# else:
#     print("No")

# for a in set_A:
#     for b in set_A:
#         for c in set_A:
#             if a + b + c == 100:
#                 print("Yes")
#                 exit()
# print("No")