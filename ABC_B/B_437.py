# import sys

# def main():    
#     input = sys.stdin.read
#     data = input().split()
    
#     if not data:
#         return

#     iterator = iter(data)
    
#     try:
#         H = int(next(iterator))
#         W = int(next(iterator))
#         N = int(next(iterator))
        
#         A = []
#         for _ in range(H):
#             row = []
#             for _ in range(W):
#                 row.append(int(next(iterator)))
#             A.append(row)
            
#         B_set = set()
#         for _ in range(N):
#             B_set.add(int(next(iterator)))
            
#         ans = 0
#         for r in range(H):
#             row_count = 0
#             for val in A[r]:
#                 if val in B_set:
#                     row_count += 1
#             if row_count > ans:
#                 ans = row_count
        
#         print(ans)
        
#     except StopIteration:
#         pass

# if __name__ == '__main__':
#     main()

H, W, N = map(int, input().split())
A = []
for _ in range(H):
    row = []
    for _ in range(W):
        row = list(map(int, input().split()))
    A.append(row)
            
B_set = set()
for _ in range(N):
    B_set.add(int(input()))
            
ans = 0
for r in range(H):
    row_count = 0
    for val in A[r]:
        if val in B_set:
            row_count += 1
    if row_count > ans:
        ans = row_count
        
print(ans)