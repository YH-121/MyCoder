import sys

def main():
    try:
        input = sys.stdin.read().split()
    except Exception:
        return
    if not input:
        return
    
    ans = 0
    count = 0
    iterator = iter(input)
    N = int(next(iterator))
    K = int(next(iterator))
    
    for i in range(N, K + 1):
        if ans < K:
            ans += i
            count += 1
        else:
            break
    print(count - 1)

if __name__ == '__main__':
    main()