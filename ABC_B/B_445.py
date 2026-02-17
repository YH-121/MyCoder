import sys

def main():
    try:
        input = sys.stdin.read().split()
    except Exception:
        return
    if not input:
        return
    
    iterator = iter(input)
    S = []
    N = int(next(iterator))
    for i in range(N):
        S.append(next(iterator))
    m = max(len(s) for s in S)
    for i in range(N):
        print(S[i].center(m, '.'))

if __name__ == '__main__':
    main()