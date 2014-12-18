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
```￼
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




