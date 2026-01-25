import sys

def main():
    try:
        input_str = sys.stdin.read().split()
    except Exception:
        return
    if not input_str:
        return

    ans = []
    iterator = iter(input_str)
    N = int(next(iterator))
    M = int(next(iterator))

    degree = [0] * (N + 1)

    for _ in range(M):
        u = int(next(iterator))
        v = int(next(iterator))
        degree[u] += 1
        degree[v] += 1

    for i in range(1, N + 1):
        candidate_count = (N - 1) - degree[i]

        if candidate_count < 3:
            ans.append(0)
        else:
            ans.append(candidate_count * (candidate_count - 1) * (candidate_count - 2) // 6)

    for a in ans:
        print(a, end=" ")

if __name__ == '__main__':
    main()
