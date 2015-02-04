Q1.1
----
 Below is a sequence of expressions. What is the result printed by the interpreter in response to each expression? Assume that the sequence is to be evaluated in the order in which it is presented.


```scheme
10 -> 10
(+ 5 3 4) -> 12
(- 9 1) -> 8
(/ 6 2) -> 3
(+ (* 2 4) (- 4 6)) -> 6
(define a 3) -> none(a->3)
(define b (+ a 1)) -> (b-> a+1) b -> 4
(+ a b (* a b)) -> 19
(= a b) -> #f
(if (and (> b a) (< b (* a b)))
b
    a)
-> 4

(cond ((= a 4) 6)
      ((= b 4) (+ 6 7 a))
      (else 25))
-> 16
(+ 2 (if (> b a) b a))
-> 6

(* (cond ((> a b) a)
         ((< a b) b)
         (else -1))
   (+ a 1))

-> 16
```

Q1.2
----

```scheme
(/ (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5))))) (* 3 (- 6 2) (- 2 7)))
-> -37/150
```

Q1.3
----

Define a procedure that takes three numbers as arguments and returns the sum of the squares of the two larger numbers.


```scheme
(define (dist x y)(+ (sqr x) (sqr y)))
(define (max_dist x y z)
    (if (> x y)
            (if (> y z) (dist x y) (dist x z))
            (if (> x z) (dist x y) (dist y z))
     )
)

e.g
> (max_dist 1 2 3)
13
> (max_dist 4 2 3)
25
> (max_dist 4 20 4)
416
> (max_dist 4 20 5)
```

Q1.4
-----

if b > 0 then take the + operator and apply to a and b 
so that it returns the value of a + b
otherwise (if b < 0)  take the - operator and returns a + -b

b>0であれば，+演算子をa，bに適応させa+bを返し，
b<0であれば，a + -bを返す．

Q1.5
---------
もしapplicative-order evaluationであれば，operandから評価をしていく．
そのため，(test 0 (p))の0を評価したあとに(p)を評価するが，関数(p)は
永遠に再帰する関数のため，(test 0 (p))を実行するとループに入る．

もしnormal-order evaluationである場合は，実行順に評価さて行く．
従って，(if (= x 0))が評価されるとtrueを返し，0が評価され，(p)は評価される
ことなく，終わる．そのためnormal-order-evaluationであると(test 0 (p))の結果は
0となる．

Q1.6
-----
new-ifを使うと，applicative-order evaluationを利用するので，引数を
先に評価してしまう．new-ifの2番目の引数はsqrt-iterなので，再帰呼び出しを
繰り返し，プログラムは停止しない．
それに対して，ifはpredicateを評価した後，どちらかの式しか評価しない．
e.g (if (predicate) true-clause false-clause)
if predicate is true, steatement of if only evaluates true-clause.

Q1.7
-----

```scheme
e.g of fail
(sqrt 4444)
66.66333325000188)
should be like this
sqrt(4444)
66.66333324999583
math.sqrt(0.0004)
0.02
(sqrt 0.0004)
0.0354008825558513

math.sqrt(10000000000000)
3162277.6601683795
> (sqrt 10000000000000)
stopped
```

```scheme
(define (sqrt-iter guess x prev-guess)
  (if (good-enough? guess prev-guess)
      guess
      (sqrt-iter (improve guess x)
    x guess)))

(define (improve guess x)
  (average guess (/ x guess)))

(define (average x y)
  (/ (+ x y) 2))

(define (good-enough? guess prev)
   (< (abs (- guess prev)) 0.001)))

(define (sqrt x)
    (sqrt-iter 1.0 x 0))

(define (square x)
    (* x x))
上記のように修正し，
> (sqrt 0.0004)
0.020001426615330147
> (sqrt 4444)
66.66333325000188
が得られた
> (sqrt 10000000000000)
3162277.6601683795
```

もっと賢い奇麗な方法としてgood-enough?だけの変更もある．
これは，次にimproveしても同じ値であれば停止するようにしている．

```scheme
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
   (= (improve guess x) guess))

(define (sqrt x)
    (sqrt-iter 1.0 x))

(define (square x)
    (* x x))
```

Q1.8
cube root(立方根) is denoted as x^(1/3)

```scheme
(define (cube-iter guess x)
  (if (good-enough? guess x)
      guess
      (cube-iter (improve guess x)
    x)))

(define (improve guess x)
    (/ (+ (/ x (square guess)) (* 2 guess))
        3))

(define (average x y)
  (/ (+ x y) 2))

(define (good-enough? guess x)
   (< (abs (- (improve guess x) guess)) 0.0001))

(define (cube x)
    (cube-iter 1.0 x))

(define (square x)
    (* x x))
```

`(= (improve guess x) guess))`だと時間が掛かりすぎる．
ので，0.0001以内の差とした
他の回答としては

```scheme
 (define (improve guess x)
   (average3 (/ x (square guess)) guess guess))

 (define (average3 x y z)
   (/ (+ x y z) 3))
```

```
がある．
上記は
x/y2, y,y をaverage3に渡し
それらを平均する
(x/y2 + y + y)/3
```
