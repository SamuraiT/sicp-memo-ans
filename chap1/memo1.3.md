section 1.3 Formulating Abstractions with Higher-Order Procedures
-------------
```scheme
(define (cube x)(* x x x))
```
は三乗を得る方法であり，演算を抽象化している．
このように，よくあるパターンに名前をつけて抽象化し，それを利用するのは
powerfulな言語に求められる能力の１つである．

しかし，数値計算(numeriacal processing)でもパラメータを数値に制限することは，抽象化の能力を狭めることになる．

########## Higher-order procedure(高階手続き)
higher order procedureとは．手続きのパラメータに手続きをとり，返り値として手続きを返したり，値を返す手続きである．

1.3章では，このhigher order procedureがどのようにpowerfuleな抽象化メカニズムを提供でき，言語が力強くなるのかを見ていく．
