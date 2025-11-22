# 競プロ用 Pythonライブラリ・テンプレートまとめ

AtCoderとかでよく使う標準ライブラリとメモ

## 1. テンプレート (高速入出力・再帰上限)
```python
import sys

# 再帰上限を増やす (デフォルト1000だと深いDFSで死ぬので)
sys.setrecursionlimit(10**6)

# input() は遅いので速度が必要なら sys.stdin.readline を使う
input = sys.stdin.readline

def solve():
    # 入力例: N = int(input())
    # 文字列の改行文字削除: S = input().strip()
    pass

if __name__ == "__main__":
    solve()
```

## 2. math (数学系)

```python
import math

# 最大公約数 (GCD)
print(math.gcd(12, 18))  # 6

# 最小公倍数 (LCM) (Python 3.9以降)
print(math.lcm(12, 18))  # 36

# 組み合わせ (nCr)
# 自作関数書かなくていいので楽
print(math.comb(5, 2))   # 10 (5C2)

# 切り上げ / 切り捨て
print(math.ceil(3.14))   # 4
print(math.floor(3.14))  # 3

# 平方根
# 整数判定したいときは誤差怖いので int(sqrt(x))**2 == x で確認する
x = 16
if int(math.sqrt(x))**2 == x:
    print("平方数")
```

## 3. collections (データ構造)

### deque (両端キュー)
リストの `pop(0)` は $O(N)$ かかって遅いので、先頭操作するならこっちを使う。BFSの必須装備

```python
from collections import deque

d = deque()
d.append(1)      # 末尾に追加
d.appendleft(2)  # 先頭に追加
x = d.pop()      # 末尾を取り出す
y = d.popleft()  # 先頭を取り出す
```

### Counter (要素のカウント)
「何が何個あるか」を辞書形式で数えてくれる。for文で回すより断然早い

```python
from collections import Counter

A = [1, 1, 2, 3, 3, 3]
c = Counter(A)
print(c[3])        # 3 (3の個数)
print(c.most_common()) # [(3, 3), (1, 2), (2, 1)] (多い順にソートもしてくれる)
```

### defaultdict (デフォルト値付き辞書)
キーがない時にエラーにならず、勝手に初期値入れてくれるやつ。グラフの隣接リスト作るときとかに便利。

```python
from collections import defaultdict

# intなら0で初期化される
d = defaultdict(int)
d["a"] += 1
print(d["b"])  # 0 (エラーにならない)

# リストなら空リスト[]で初期化
adj = defaultdict(list)
adj[0].append(1) 

# 複数の値で初期化
cnt = defaultdict(lambda: defaultdict(int))
```

## 4. itertools (順列・組み合わせ・累積和)

```python
from itertools import permutations, combinations, product, accumulate, groupby

# 順列 (Permutations)
# (1, 2, 3) の並び替え全列挙
for p in permutations([1, 2, 3]):
    print(p)

# 組み合わせ (Combinations)
# 3つから2つ選ぶ
for c in combinations([1, 2, 3], 2):
    print(c)

# 直積 (Product)
# bit全探索 (2^N) とかで使う。ネスト深いfor文書かなくて済む
for bits in product([0, 1], repeat=3):
    print(bits)

# 累積和 (Accumulate)
# C実装なので手書きループより爆速。initial=0 を忘れずに
A = [1, 2, 3]
S = list(accumulate(A, initial=0)) # [0, 1, 3, 6]

# ランレングス圧縮 (Groupby)
# 連続する文字をまとめる
S = "AAABBC"
groups = [(k, len(list(g))) for k, g in groupby(S)]
# [('A', 3), ('B', 2), ('C', 1)]
```

## 5. heapq (優先度付きキュー)
最小値を $O(\log N)$ で取り出せる。ダイクストラ法とか、常に一番小さいやつを知りたい時に。

```python
import heapq

q = []
heapq.heappush(q, 5)
heapq.heappush(q, 1)
heapq.heappush(q, 3)

print(heapq.heappop(q)) # 1 (最小値が出てくる)
print(heapq.heappop(q)) # 3
```

> [!TIP]
> 最大値を取り出したい時は、値を `-1` 倍して入れて、取り出す時にまた `-1` 倍して戻すのが定石。

## 6. bisect (二分探索)
ソート済みのリストに「どこに入れたら順序崩れないか」を探すやつ。
`lower_bound` とか `upper_bound` 的な操作。

```python
import bisect

A = [1, 2, 4, 4, 6]

# bisect_left: x以上の最初の場所 (lower_bound)
idx = bisect.bisect_left(A, 4)
print(idx) # 2

# bisect_right: xより大きい最初の場所 (upper_bound)
idx = bisect.bisect_right(A, 4)
print(idx) # 4
```

## 7. functools (メモ化再帰)
再帰関数の結果をキャッシュしてくれるデコレータ。
これ付けるだけでTLE回避できるDP問題も結構ある。

```python
from functools import lru_cache

# maxsize=None にしないとキャッシュ数制限されるので注意
@lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

print(fib(100)) 
```
