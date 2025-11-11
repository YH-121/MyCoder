N = int(input())

print(sum(i**3 if i % 2 == 0 else -i**3 for i in range(1, N + 1)))

# total = 0
# for i in range(1, N + 1):
#   if i % 2 == 0:
#     total += i**3
#   else:
#     total -= i**3
# print(total)