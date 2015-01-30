sicp-memo-ans
=============

SICPの各セクションでのメモと解答を載せています．
SICPを勉強しているかたは参考にして下さい．


**注意**

もし，random関数をgauchで使いたい場合は

```
(use math.mt-random)
(define m (make <mersenne-twister> :seed (sys-time)))
(mt-random-integer m 1000)
(define (random n) (mt-random-integer m n))
```
を使用すること．

また，`runtime`を利用したい場合は
```
(define (runtime)
    (use srfi-11)
    (let-values (((a b) (sys-gettimeofday)))
    (+ (* a 1000000) b)))
```
を使用すればよい


ちなみに，SICPを勉強するのにおいて，
僕は`Petite Chez Scheme`という処理系を利用している．

**言語について**
僕はpythonが好きな理由から，pythonでも一部実装しているが，
基本は全てschemeで実装している．そのため，SICPの勉強目的であれば
`memo*.*.md`, `question*.*.md`だけを参照されたい．
