import sys
import itertools

# 再帰の深さ制限を増やす（DFS用）
sys.setrecursionlimit(2000)

def solve():
    """
    LINE Algorithm Contest 2024 (想定) - 花火大会の席順問題
    
    問題の概要（推測）:
    - Nチームが花火大会に参加するかどうかを決める。
    - 参加する場合、チームiは人数 a_i 分の席（ブロック）を確保する必要がある。
    - ブロックには定員（1~9）があり、1つのブロックは1つのチームしか使えない（相席不可）。
    - 嬉しさ = (参加チームのスコア総和) - (不参加チームのペナルティ総和)
      - 参加チーム i: x * a_i - y * (使用ブロック数)
      - 不参加チーム i: -z * a_i
    
    アルゴリズムの解説:
    1. **チーム選択の探索**:
       - どのチームを参加させるかの組み合わせを全探索します（Nが小さいと仮定）。
       - 参加チームの集合が決まれば、得られる「基本スコア（x * a_i）」と「不参加ペナルティの回避」が確定します。
       
    2. **ブロック割り当て（貪欲法 + バックトラッキング）**:
       - コスト（y * 使用ブロック数）を最小化するためには、なるべく「容量の大きいブロック」を「少ない個数」使うのが有利です。
       - 利用可能なブロックを容量の大きい順にソートします。
       - 必要なブロック数 K を、理論上の最小値（総人数 / 最大容量など）から順に増やして試します。
       - 「上位 K 個のブロックを使って、選んだチーム全員の人数を賄えるか？」をバックトラッキング（DFS）で判定します。
       - 判定に成功した最小の K が、そのチーム集合における最小コストを与えます。
       
    3. **最適解の更新**:
       - 各チーム集合について計算したスコア（嬉しさ）が、これまでの最大値を更新すれば、その配置を記録します。
    """

    # 標準入力からデータを読み込む
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        N = int(next(iterator))
        H = int(next(iterator))
        W = int(next(iterator))
        X = int(next(iterator))
        Y = int(next(iterator))
        Z = int(next(iterator))
        
        A = []
        for _ in range(N):
            A.append(int(next(iterator)))
            
        grid_map = []
        for _ in range(H):
            grid_map.append(next(iterator))
            
    except StopIteration:
        return

    # グリッドから利用可能なブロックを抽出
    # ブロックは (容量, 行, 列, ID) で管理
    blocks = []
    for r in range(H):
        for c in range(W):
            char = grid_map[r][c]
            if char != '#' and char != '.':
                try:
                    cap = int(char)
                    blocks.append({'cap': cap, 'r': r, 'c': c, 'id': len(blocks)})
                except ValueError:
                    pass

    # 容量の大きい順にソート（貪欲戦略のため）
    blocks.sort(key=lambda x: x['cap'], reverse=True)
    
    total_blocks = len(blocks)
    
    # チーム情報（IDは1始まり）
    # benefit: 参加することで増えるスコア（不参加ペナルティの解消 + 参加ボーナス）
    # 不参加時のスコアは -z * a_i。参加時のスコアは x * a_i - y * blocks。
    # 差分は (x + z) * a_i - y * blocks。
    # ベーススコア（全員不参加）からスタートして、この差分を足していくと考えます。
    
    base_score = -sum(Z * a for a in A)
    teams_with_idx = []
    for i in range(N):
        teams_with_idx.append({'val': A[i], 'id': i + 1, 'benefit': (X + Z) * A[i]})
        
    # 探索の効率化のため、benefitが大きい順（あるいは人数が大きい順）にソートしても良いが、
    # ここでは組み合わせ全探索なので順序は本質的ではない。
    
    best_score = -float('inf')
    best_assignment_map = {} # block_idx -> team_id
    
    # ビンパッキング（ブロック割り当て）の判定関数
    def solve_bin_covering(current_demands, block_caps):
        """
        current_demands: [[残り人数, チームID], ...]
        block_caps: [[ブロック容量, ブロックID], ...]
        
        指定されたブロックセットですべてのチームの人数を満たせるか判定し、
        割り当て結果を返す。
        """
        if not current_demands:
            return {}
            
        # 満たされていないチームのみ抽出
        active_demands = [d for d in current_demands if d[0] > 0]
        if not active_demands:
            return {}
            
        if not block_caps:
            return None # ブロックが足りない
            
        # 枝刈り: 残りブロックの総容量が残り需要より少なければ不可
        if sum(b[0] for b in block_caps) < sum(d[0] for d in active_demands):
            return None
            
        # バックトラッキング
        # 最も大きいブロックを取り出す
        b_cap, b_idx = block_caps[0]
        rem_blocks = block_caps[1:]
        
        # 需要の大きいチーム順に試す（ヒューリスティック）
        active_demands.sort(key=lambda x: x[0], reverse=True)
        
        for i, (dem, t_id) in enumerate(active_demands):
            # このブロックをチーム t_id に割り当てる
            new_demands = []
            for j, other in enumerate(active_demands):
                if i == j:
                    if dem - b_cap > 0:
                        new_demands.append([dem - b_cap, t_id])
                else:
                    new_demands.append(other)
            
            res = solve_bin_covering(new_demands, rem_blocks)
            if res is not None:
                res[b_idx] = t_id
                return res
        
        return None

    # チームの組み合わせを全探索
    # itertools.combinations を使用
    for r in range(N + 1):
        for team_indices in itertools.combinations(range(N), r):
            current_teams = [teams_with_idx[i] for i in team_indices]
            
            current_benefit = sum(t['benefit'] for t in current_teams)
            total_demand = sum(t['val'] for t in current_teams)
            
            # 必要なブロック数の下限を見積もる
            needed_blocks_count = 0
            current_cap_sum = 0
            possible = False
            
            if total_demand == 0:
                possible = True
            else:
                for k in range(len(blocks)):
                    current_cap_sum += blocks[k]['cap']
                    if current_cap_sum >= total_demand:
                        needed_blocks_count = k + 1
                        possible = True
                        break
            
            if not possible:
                continue

            # スコアの上限チェック（枝刈り）
            # 最小ブロック数で済んだ場合のスコアが、現在の最高スコア以下ならスキップ
            potential_score = current_benefit - Y * needed_blocks_count + base_score
            if potential_score <= best_score:
                continue
                
            # ブロック数 K を増やしながら割り当てを試行
            for k in range(needed_blocks_count, total_blocks + 1):
                real_potential = current_benefit - Y * k + base_score
                if real_potential <= best_score:
                    break # これ以上ブロックを増やしても最高スコアを超えられない
                
                # 判定用データの準備
                demands_arg = [[t['val'], t['id']] for t in current_teams]
                blocks_arg = [[blocks[i]['cap'], i] for i in range(k)]
                
                assignment = solve_bin_covering(demands_arg, blocks_arg)
                if assignment is not None:
                    best_score = real_potential
                    best_assignment_map = assignment
                    break # このチーム構成での最小ブロック数が見つかったので終了
            
    # 結果の出力
    output_grid = list(grid_map)
    output_grid = [list(row) for row in output_grid]
    
    for b_idx, t_id in best_assignment_map.items():
        b_info = blocks[b_idx]
        r, c = b_info['r'], b_info['c']
        output_grid[r][c] = str(t_id)
        
    for row in output_grid:
        print("".join(row))

if __name__ == '__main__':
    solve()
