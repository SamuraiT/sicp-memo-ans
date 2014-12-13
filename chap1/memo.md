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


    
1.1　プログラムの要素
    協力なプログラミング言語の特徴
        基本式（premitive expression）単純なもの
        組み合わせ法（means of　combination）複雑なもの（合成物）は単純なものから作られる合成物
        抽象化：合成物に名前をつけて，それを扱う

    データは処理したいもの
    手続きはデータの処理法の記述

    強力な言語はデータと手続きが記述できて，
    手続きとデータを組み合わせたり抽象化する手段を持つ

   
1.1.2

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

組み合わせた演算（compound operation）に名前を付けて，
１つのユニットとして扱う抽象化を手続きの定義(procedure definition))と呼ぶ．

defineのような記号は今での評価方法ではなく，違う評価方法を使う．
このような記号を特殊形式と呼ぶ．特殊形式は異なる評価方法を持つ．

(define (<name> <formal parameters>) <body>)

 The <name> is a symbol to be associated with the procedure definition in the environment.

1.1.5

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

場合分け（case analysis）
    絶対値を取るような手続きは，数値を評価して，
    返す値を決めるこのような仕組み(構造)をcase analysisという

    pairs of expressions (<p> <e>) is called clauses(節)
    <P> is predicate(述語): true/falseと解釈される式のこと
    （is an expression whose value is interpreted as either true or false）
    predicateという単語はtrue/falseを返す手続きや，true/false評価する式にも使われる
    (predicate is used for procedures that return true or false, as well as for expressions that evaluate to true or false)

    <e>is consequent expression(帰結式) 


