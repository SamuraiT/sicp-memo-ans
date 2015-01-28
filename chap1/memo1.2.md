1.2 Procedures and the Processes they generate
----------------------
ここまで，四則演算を使い，またそれらを組み合わせて使ったり，組み合わせて続き（compound procedure）を定義して抽象化したりして，プログラムの要素技術を見てきた．
しかしながら，これだけでは，どの手続きが定義するに値するか，手続きの実行結果を予測する経験が足りない．

結果を脳内で可視化し，予測する能力は創造性等のようにエキスパートプログラマになるのには欠かせない．


エキスパートになるには，様々な手続きにより生成された処理（processes）を視覚化	できる必要がある．このようなスキルを伸ばして初めて，思っていた動作をするプログラムを構築できるようになる．

このセクションでは，単純な手続きによって生成されたプロセスの共通する形を見ていく．また，手続きはどの程度，計算機的資源（computational resources）である時間や空間（メモリ）を消費するのかを見ていく．


1.2.1 Linear Recursion and Iteration
------
nの階乗n!を考える．
n!はn*(n -1), 1 if n ==1 と考えることができる．
これをそのまま表し，置換置き換えもモデルで表現した物が，
figure 1.3である．

次に，6!は1*2*3*4*5*6と1からnまでの積(product)で表現出来る．
そこで，積とカウンターを使って表現してみる．

```
counter = product = 1
loop until counter > 6
    product = product * counter
    counter = counter + 1
```
￼
これを実装して，置換置き換えモデルで表現したのがfigure 1.4となる．

これと1.3を比較すると，1.3では処理が進みにつれて，膨張しているのが分かる．
これは，deferred operations(chain of multiplications)(遅延演算)が原因で起こっている．
このようにdeferred operationsでの処理をrecursive process（再帰的処理）という．この処理を行うには，
interpreterは後で実行される演算を記憶しておかなくてはならない．
deffered operationsの鎖の長さを記憶するのは，nに比例しておおきくなる．
このようなプロセスをliner recursive process（線形再帰的プロセス）

1.4の方は，膨張したりはしない．各ステップごとに覚えておくのはnと
counter，productだけだ．このようなプロセスをiterative process(反復的プロセス)と呼ぶ．一般的に，interative processというのは
いくつかの固定された状態変数（state variable）を持っている．また，状態が変わる時に，どのように状態変数を更新してくかのルールも規定する．さらに，終了条件を付け加える場合もある．
n!にはnのステップを要し，反復プロセスを使う場合はliner recursive process線形反復プロセスと呼ぶ．


iterative processはどの状態でも完全な状態を保持する．つまり，途中で計算をおわらしても，その時の状態(状態変数)
を利用すればすぐに再開できる．

recursive processとrecursive procedureは違うものである．
再帰的プロセスはプロセスがどう進むかであり，recursive procedureは
手続きを自分で定義するという定義である．

例えば，c, pascal, adaなどは，再帰を使うとiterative processでも手続きを呼び出すたびにメモリを消費する．
したがって，そのような言語ではiterative processはloop（while, for, until）等の処理を使って表現しないとならない．

しかし，shcemeは再帰を使ったiterative processでも一定のメモリしか消費しない．この実装をtail recursive（末尾再帰）という．



1.2.2 Tree Recursion(木構造再帰)
--------
fibonacci数では，Tree Recursionが表現できる．
しかし，fibonacci数では入力に対して，プロセスのステップ数は指数関数的に，スペース（メモリ）は線形的に増加する（今いるノードの親を覚えているだけで良いから）．

一般的に，ステップの数は木のノードの数に比例し，
スペースは木の最大深さに比例する．

もちろん，fibonacciを反復プロセス（iterative process）に置き換える事はできる．
それは同時に以下の式を更新することで可能となる．（ただし初期値はa = fib(1) b = fib(0）とする）

```
a <- a + b
b <- a
```

例を使うと，fib(6)だと上記の式を6回適応すればよい

```
1:	1 = a <- 1 + 0
	1 = b <- 1
2: 	2 = a <- 1 + 1
	1 = b <- 1
3:	3 = a <- 2 + 1
	2 = b <- 2
4:  5 = a <- 3 + 2
	3 = b <- 3
5: 	8 = a <- 5 + 3
	5 = b <- 5
6: 	13 = a <- 8 + 5
	8 = b <- 8
```

六回目のbは8なので，fib(n=6)のときb(=8)を返せば良い．
これをlispで表すと

```
(define (fib n)
    (define (iter a b counter)
      (if (= counter 0)
          b
          (iter (+ a b) a (- counter 1))))
    (iter 1 0 n))
```

これは，上記で説明してわかるように，ステップ数がnに比例する．

普通にtree recursionを扱うと使えないと思うかもしれないが，階層構造のデータを扱うプロセスを考えるとき，tree Recursionは自然でとても力強いものである．
なぜなら，簡単にイメージ（数式）通りにlispに変換できるからである．
数値計算（numerical operations）でも，tree recursionはプログラムを理解するのと設計するのにとても役立つ．

tree recursionを有効に活用する（＝iterative processにするには）にはここでは，3つの状態変数を持つようにすればよい．


#### 例, counting Change(両替)

tree recursion(木構造再帰)は非効率だが，理解するのは簡単である．木構造から同じ結果を計算するより効率的な手続きに
変換する「smart compiler」(スマート解釈系)を設計する事で良書の長所だけをとる方法がある．
それは，計算出来たところはテーブルを作成し，計算する際にその値がテーブルにあるかを調べて，冗長な計算を
減らす方法である．これをテーブルか（tabulation），メモ化(memoization)とよぶ．
これは，木構造を使いつつ，メモリを利用する事で計算スピードを早める事ができる．

1.2.3 Order of Growth
------
プロセスによって計算資源（computational　resources）を消費する割合（速度）が違う．
これを記述するのにorder of growthというのを使うと便利になる．
*order of growthは入力が大きくなった時に，大体の必要となる資源を見積もるのに役立つ．*


nを問題の大きさとする
R(n)は大きさnの問題に対して,プロセスが必要とする資源の量(amount of resources)とする

R(n)は内部のレジスタがどれだけ使われたかを測ったり,
実行された機械演算の数だったりする．

一度に決められた数の演算(operations)しかできないコンピュータであれば，
必要となる時間は実行された機械演算数(number of elementary machine operations)に比例する．

```
k1*f(n) <= R(n) <= k2*f(n)

のとき，R(n)はθ（f(n)）の程度の増加と言い．
R(n) = θ（f(n)）と書く．(theta of f(n))
```

1.2.4 Exponentiation
---------------------

$$b^n$$を求めるための１つの方法として再帰を使う方法がある．
それは．下記の定義から導ける．

```
b^n = b * b^n-1
b^0 = 1
```

つまり，

```
b^0 = 1
b^1 = b * b^0
b^2 = b * b^1
b^3 = b * b^2
b^n = b * b^n-1
```
なので，

```
(define (expt b n)
  (if (= n 0)
      1
      (* b (expt b (- n 1)))))
```

とかけ，

さらに，

```
bn = (bn/2)2 if n is even,
bn =b·bn−1 if n is odd.
```
を適用すると，

```
(define (fast-expt b n) (cond ((= n 0) 1)
((even? n) (square (fast-expt b (/ n 2)))) (else (* b (fast-expt b (- n 1))))))
```
のようにステップ数が，log(n), スペースlog(n)で実行できる関数が出来る．

```
note:
nがoddであれば，
n-1して
偶数になる．
nが偶数であれば，n/2づつ次の計算がされる．
つまり，公比が1/2である．an = a*r^nを解くと．
n = log2(a)となる．従って，ステップ数がlog(n)となる．
これは，前章のQ1.15を参照．

```

1.2.5 Great Common divisor 
-------
great common divisor （最大公約数）は整数a,bが合ったとき，
両方の値を剰余0で割り切れる最大のdivisor(約数)を求める事である．

gcdは簡単に求められ，
```
gcd(a, b) = gcd(b, a%b)
```
をb==0になるまで繰り返せば良い．
また，このアルゴリズムはeuclidのアルゴリズムとしても知られている．
