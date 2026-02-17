import sys

def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    N = int(next(it))
    A = [int(next(it)) for _ in range(N)]
    
    memo = [0] * (N + 1)
    
    def find(x):
        path = []
        while memo[x] == 0:
            path.append(x)
            nx = A[x - 1]
            if nx == x:
                memo[x] = x
                break
            x = nx

        root = memo[x] if memo[x] else x
        for v in path:
            memo[v] = root
        return root
    
    ans = [find(i + 1) for i in range(N)]
    print(*ans)
    
if __name__ == '__main__':
    main()