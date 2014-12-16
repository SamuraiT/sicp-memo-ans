序論
本書の目的：
    プログラミングに対する美的感覚を持つ事
    複雑で巨大なシステムを制御する力を持つ事

    複雑さを制御するのに抽象化して細部を隠す．
    複雑さを制御するのに
    そして，部品を取り替えして組み合わせ，システムが構築できるような
    インターフェイスを作る．
    この方法は工学設計全てに共通する


    数学は「何である」の概念を精密に扱う枠組を提供する. 
    計算機科学は「いかにして」の概念を精密に扱う枠組を提供する. 


    
1.1
------
プログラムの要素
    協力なプログラミング言語の特徴
        基本式（premitive expression）単純なもの
        組み合わせ法（means of　combination）複雑なもの（合成物）は単純なものから作られる合成物
        抽象化：合成物に名前をつけて，それを扱う

    データは処理したいもの
    手続きはデータの処理法の記述

    強力な言語はデータと手続きが記述できて，
    手続きとデータを組み合わせたり抽象化する手段を持つ

   
1.1.2
------
    プログラム言語の重要な点は,
名前を使って計算オブジェクトを指す手段を用意すること
である.これはまさに抽象化である．
このように抽象化されたオブジェクトを積み上げる事で，
より複雑なプログラムを作る事が出来る．
この抽象化には名前と値のペアを保持するメモリが必要である．
lispではこれを環境（enviornment）と読んでいる．


再帰は階層的な木構造のオブジェクトを扱うのに強力な技法
であることが分る.
 実際,評価規則の「値が上方へのぼる(stem from)」形は
木構造のため込み (tree accumulation)として知られている．

lispのようなインタラクティブな言語では(+ 1 2)のような
式の値を環境を無しに話すのは意味の無い事である．
それは，環境がSymbol(記号)に意味を与えているからだ．

1.1.4
-----
組み合わせた演算（compound operation）に名前を付けて，
１つのユニットとして扱う抽象化を手続きの定義(procedure definition))と呼ぶ．

defineのような記号は今での評価方法ではなく，違う評価方法を使う．
このような記号を特殊形式と呼ぶ．特殊形式は異なる評価方法を持つ．

(define (<name> <formal parameters>) <body>)

 The <name> is a symbol to be associated with the procedure definition in the environment.

1.1.5
-----
科学，エンジニアリングの現象をモデル化する場合は，
単純で不完全なモデルから始める．対象を調べていくうちに，
単純なモデルは不適切となり，洗練されたモデルで取り替えていく．
このプロセスを得ていき，適切なモデルを作成する．


完全に式を展開してから評価していく（reduce） 評価方法を
normal-order evaluation(正規順序と呼ぶ)

引数を評価してから手続きをoperandに作用（apply）させる
評価方法を：applicative-order evaluation（作用的順序）
と言う
ちなみに，lispはallicative-order evaluationを使ってる．
これは，重複評価を避けるためである．

1.1.6 Conditional Expressions and Predicates
------
場合分け（case analysis）
    絶対値を取るような手続きは，数値を評価して，
    返す値を決めるこのような仕組み(構造)をcase analysisという

    pairs of expressions (<p> <e>) is called clauses(節)
    <P> is predicate(述語): true/falseと解釈される式のこと
    （is an expression whose value is interpreted as either true or false）
    predicateという単語はtrue/falseを返す手続きや，true/false評価する式にも使われる
    (predicate is used for procedures that return true or false, as well as for expressions that evaluate to true or false)

    <e>is consequent expression(帰結式) 

1.1.7 example: square roots by newtons method
---------
これまでの手続きは通常の関数のように複数のパラメータから決まる値を定義するものであった．
しかし，数学の関数とコンピュータの手続きの間には重要な違いがある．
手続きは結果を生み出さないとならない．

数学では，なにをするかの記述に関心があるが(宣言的知識,declative knowledge)
コンピュータでは，どうするかの記述するに関心がある(imperative knowledge　命令的知識)

Newton’s method(Newton法):
目的:xを与えとき平方根√xを求めたい

```
√xの予測をyとする．
以下を十分な値が取れるまで繰り返す．
    1. xとyの商(quotient)を求めるQ = x/y
    2. 次に，商と予測の平均(average)を求める average = (Q+y)/2
    3. 平均を予測yとするy = average
十分な値とは√x=yの時，x - y^2 <= 0.001となるときである．
つまり，二乗誤差を取った時に0.001以下になればよしとする．
```
√xのxをradicand（被開平数）という


```
(define (next-guess y x)
    (average (Q y x) y))

(define (Q y x)
    (/ x y))

(define (average x y)
    (/ (+ x y) 2))

(define (sqr x)
    (* x x))

(define (good-enough? y x)
    (<= (abs (- (sqr y) x)) 0.001))

(define (sqrt-iter y x)
    (if (good-enough? y x)
        y
        (sqrt-iter (next-guess y x) x)))

(define (sqrt-newton x)
    (sqrt-iter 1.0 x))

(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
          (else else-clause)))

(define (sqrt-iter-new-if y x)
    (new-if (good-enough? y x)
        y
        (sqrt-iter-new-if (next-guess y x) x)))

(define (sqrt-new x)
    (sqrt-iter-new-if 1.0 x))


```

```
(define (sqrt-iter guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x)
    x)))

(define (improve guess x)
  (average guess (/ x guess)))

(define (average x y)
  (/ (+ x y) 2))

(define (good-enough? guess x)
   (< (abs (- (square guess) x)) 0.001))

(define (sqrt x)
    (sqrt-iter 1.0 x))

(define (square x)
    (* x x))
```


1.1.8 Procedures as Black-Box Abstractions
------
sqrtの手続きでは，問題を部分問題(subproblem)と分解(decompose)し手続きの束(procedure
of cluter)をした．
ここで，重要なのは部分問題を手続きで表現する事で，ブラックボックスとして扱えることである．
そうすることで，利用者はその実装を知らなくてよい．また，他の場所でも部品(module)として
扱う事ができる．また，それらの手続きをprocedual abstractionと呼ぶ．

局所名(local name)
手続きの仮パラメータ(formal prameter)は手続き定義中で束縛(bind)される．
そのため，それらの変数は束縛変数(a bound variable)と呼ばれる．
また，bound variableの有効である範囲をscopeと呼ぶ．
boudn variableに対して，手続きのscope内で束縛されていない変数をfree
と呼ぶ．

Internal definition and Block structure(内部定義とブロック構造)

今までは以下のように分けて手続きを定義してきた
```
(define (sqrt x)
  (sqrt-iter 1.0 x))
(define (sqrt-iter guess x)
  (if (good-enough? guess x)
      guess
      (sqrt-iter (improve guess x) x)))
(define (good-enough? guess x)
  (< (abs (- (square guess) x)) 0.001))
(define (improve guess x)
  (average guess (/ x guess)))
```

しかしながら，このsqrtを手続きとして利用する人にとっては，`good-enough?, improve`のような他の手続き(subprocedure)は利用者を悩ませるだけである．
例えば，同じように近似して何かを導く手続きを利用者は書くとき，既存の`good-enough?`と異なるが同じ名前を使いたい場合がでるかもしれない．
これは，システムが巨大になるほど深刻な問題となる．

そこで，このようなsubprocedureをsqrtの手続き中に定義することで（＝internal definition内部定義），上記のような問題を防げる．
手続きを内部定義すると以下のようになる．このように定義をネストさせる構造をブロック構造(Block Structure)と呼ぶ．
さらに，今まではxを書くsubprocesureの引数として取っていたのをsqrt内で束縛し，subprocedureからは自由変数と見せる事で引数として取る必要をなくした．こうすることでより単純化出来る．このような方法をlexical scoping or static scoping(静的スコープ)と呼ぶ．

```
(define (sqrt x)
    (define (square x)(* x x))
    (define (average x y)(/ (+ x y) 2))
  (define (good-enough? guess)
    (< (abs (- (square guess) x)) 0.001))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iter guess)
    (if (good-enough? guess)
        guess
        (sqrt-iter (improve guess))))
  (sqrt-iter 1.0))

```
このブロック構造を出来るだけ使うことで，巨大な問題を簡単に扱えるようする．この手法はクラスに似ているように思われる．また，ブロック構造はAlgo60から始まっているそうだ．
