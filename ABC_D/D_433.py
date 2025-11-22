import sys
from collections import defaultdict

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    # --- O(N^2) 解法 (TLE) ---
    # count = 0
    # for i in range(N):
    #     for j in range(N):
    #         if int(str(A[i]) + str(A[j])) % M == 0:
    #             count += 1
    # print(count)

    # --- O(N) 解法 ---
    # A[i] と A[j] を連結した値は A[i] * 10^(len(A[j])) + A[j]
    # これが M で割り切れる条件は:
    # (A[i] * 10^(len(A[j])) + A[j]) % M == 0
    # => A[j] % M == -(A[i] * 10^(len(A[j]))) % M
    
    # 1. 前処理: 「桁数」と「余り」ごとに個数をカウント
    # cnt[d][r] := 桁数が d で、M で割った余りが r である数の個数
    cnt = defaultdict(lambda: defaultdict(int))
    
    for x in A:
        d = len(str(x))
        r = x % M
        cnt[d][r] += 1
        
    ans = 0
    
    # 2. 各 A[i] について、ペアとなる A[j] の個数を足し合わせる
    for x in A:
        # A[j] の桁数 len_j を 1 から 10 まで試す (A[i] <= 10^9 なので最大10桁)
        # ※問題文の制約によっては桁数がもっと大きい可能性もあるが、
        #   A[i] が整数として与えられるなら len(str(x)) で取得した桁数だけ見ればOK
        #   ここでは cnt に存在する桁数だけ見れば十分
        
        for len_j in cnt.keys():
            # 条件を満たす A[j] の余り target_r を計算
            # target_r = -(x * 10^len_j) % M
            # Pythonの % 演算子は負の数に対しても正の余りを返すのでそのまま計算可能
            target_r = -(x * pow(10, len_j, M)) % M
            
            # その条件を満たす A[j] の個数を加算
            ans += cnt[len_j][target_r]
            
    print(ans)

if __name__ == "__main__":
    main()