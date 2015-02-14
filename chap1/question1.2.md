Q1.9
----

```scheme
(define (+ a b)
  (if (= a 0)
      b
      (inc (+ (dec a) b))))

(define (+ a b)
  (if (= a 0)
      b
      (+ (dec a) (inc b))))
```

最初の手続きのsubstitution model:

```scheme
(+ 4 5)
(inc (+ 3 5))
(inc (inc (+ 2 5)))
(inc (inc (inc (+ 1 5))))
(inc (inc (inc (inc (+ 0 5))))
(inc (inc (inc (inc 5))
(inc (inc (inc 6))
(inc (inc 7))
(inc 8)
9
```

従って，再帰プロセス

二番目:

```scheme
(+ 4 5)
(+ 3 6)
(+ 2 7)
(+ 1 8)
(+ 0 9)
9
```

従って，反復プロセス

Q1.10
-------

```scheme
> (A 1 10)
1024
> (A 2 4)
65536
> (A 3 3)
65536

(define (f n)(A 0 n))
->  2n
(define (g n)(A 1 n))
<s> ->  4*2^(n-2)</s>
-> 2^{n}

(define (h n)(A 2 n))
-> 2^2^...*n times
```

Exercise 1.11.
------------
A function f is defined by the rule that

```
f(n) = n if n<3 and
f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3) if n> 3.
```

Write a procedure that computes f by means of a recursive process. Write a procedure that computes f by means of an iterative process.

recursive process

```scheme
(define (f n)
	(if (< n 3)
		n
	    (+ (f (- n 1)) (* (f (- n 2)) 2) (* 3 (f (- n 3))) )
	)
)

> (f 1)
1
> (f 2)
2
> (f 3)
4
> (f 4)
11
> (f 5)
25
> (f 6)
59
> (f 7)
142
```

iterative process

```scheme
(define (f n)
    (define (iter a b c counter)
      (if (< counter 3)
          c
          (iter b c (+ c (* b 2) (* a 3)) (- counter 1))))
    (iter 0 1 2 n))
> (f 3)
4
> (f 4)
11
> (f 5)
25
> (f 6)
59
> (f 7)
142
```

iterative processの考え方としては，もともとの木構造をよく見て，
更新した時に，初期の状態(a, b, c)がどのように遷移するのかを考えれば良い．
従って，反復プロセスを考える際はまず，tree recursionをから状態変数を決め
その状態変数がどのように遷移するかを考えれば良い．

[reference](http://www.billthelizard.com/2009/11/sicp-exercise-111.html)

Q1.12
-------

```scheme
(define (pascal-triangle row col)
      (cond ((> col row) 0)
          ((< col 0) 0)
          ((= col 1) 1)
          ((+ (pascal-triangle (- row 1) (- col 1)) (pascal-triangle (- row 1) col)))))

(pascal-triangle 3 2)
2

this counts num from 1 either for col and row.
```

another answer by using pascals triangle equation.
(binominal coeffient)

```scheme
(define (factorial n)
  (fact-iter 1 1 n))
(define (fact-iter product counter max-count)
  (if (> counter max-count)
      product
      (fact-iter (* counter product)
                 (+ counter 1)
                 max-count)))

(define (comb n m)
    (/ (factorial n) (* (factorial m) (factorial (- n m)))))

(define (pascal n)
  (define (display-line n m)
    (display (comb n m))
    (display " ")
    (if (> n m)
        (display-line n (+ m 1))))
  (define (iter N)
    (display-line N 0)
    (newline)
    (if (< N n)
        (iter (+ N 1))
        )
    )
  (iter 0))

this is used as a following:

> (pascal 5)
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
```
Q1.13
-----

http://www.kendyck.com/math/sicp/ex1-13.xml

上記のサイトを参考．

```scheme
Fib(0) = 0
Fib(n) = Fib(n-1) + Fib(n+2)
       = (φ^n - ψ^n) / √5

Fib(n+1) = Fib(n) + Fib(n-1)
       = ((φ^n - ψ^n) / √5) + ((φ^n-1 - ψ^n-1) / √5)
       = 頑張ると
       = (φ^n+1 - ψ^n+1) / √5
       になるらしい
```

Q1.14
-------
プロセスの木については， ![tree](http://telegraphics.com.au/~toby/sicp/ex1-14.svg)
を参考．実際に書いてみて，これと同じになった．

次に，n（number of amount）が増加した場合は

スペースが: `O(n)`

計算量は: `O(n^5)`

となる．
スペースは木の深さに依存する，プロセスの木より深さがおおよそnのためO(n)とわかる．

計算量は，少し複雑でである．
まず，cc(n,1)の場合を考える．プロセスの木より，`cc(n,1) = 2n+1`とわかる．
したがって，`O(cc(n,1) = O(n)`

次に，再帰的にcc(n, 5)はどうなるかを考える．

```
1. cc(n, 1) = O(n)
2. cc(n, 2) = cc(n, 1) + cc(n-5, 2)
3. cc(n, 3) = cc(n, 2) + cc(n-10, 2)
4. cc(n, 4) = cc(n, 3) + cc(n-25, 3)
5. cc(n, 5) = cc(n, 4) + cc(n-50, 4)
```
さて，`cc(n, 2)`のときは`cc(n,1) = O(n)`で，
`cc(n-5, 2)`は`n/5回`,nが0になるまで繰り返されるのと，`cc(n-5,1)(= O(n))`が実行されるので，
`O(n)*O(n/5)`となり計算量は`O(n^2)`となる．となり，全体は`O(n) + O(n^2) = O(n^2)`となる．

同様に，`cc(n, 3)`のときは，`cc(n, 2) = O(n^2)`で，
`cc(n-10, 2)`は`n/10回`，nが0になるまで繰り返されるまた，`cc(n-10, 2)`が実行されるので，
計算量は`O(n^2)*O(n/10)`となり．全体としては`O(n^2) + O(n^3) = O(n^3)`となる．

同様に，`O(cc(n,4)) = O(n^4)`, `cc(n, 5) = O(n^5)`となる．


```
note:
n=10ならば，n-5のステップは
10-5 = 5
5 - 5 = 0
よって，2回

if n = 20 then
20 - 5 = 15
15 - 5 = 10
10 - 5 = 5
5 - 5 = 0
よって，4回

つまり，n-5を繰り返すステップは
n/5回実行される．
```

Q1.15
------

a. 5回．

```scheme
(sine 12.15)
(p (sine 4.05))
(p (p (sine 1.35)))
(p (p (p (sine 0.45))))
(p (p (p (p (sine 0.15)))))
(p (p (p (p (p (sine 0.05))))))
(p (p (p (p (p 0.05)))))
...

b. angleが0.1以下になるまで再帰的にsineを計算する．
aが与えられた時に，0.1になるまで1/3されていく．
nすてっぷで0.1になるとすると．

今，公比rとすると．aは初項であり，つまりsineに入力する値である．

a_n = ar^{n}
となる．r = 1/3なので，
r^-1 = 3とすると

a_n = ar^-n
が得られる．今，a_n <= 0.1とする時のnの値が知りたいので，
n =の形にするために，対数を取る．

log(a_n) = log(a) - nlog(r)
nlog(r) = log(a) - log(a_n)
nlog(r) = log(a/a_n)
n = log(a/a_n)/log(r)
n = log_r(a/a_n)
今，r=3, a_nは0.1以下なので
n = log3(a/0.1)
従って，ステップ数はlog3(a)である．
*** ステップ数はO(log(n))，
スペースも同様に増加するためO(log(n))である．
```

Q1.16
--------


```scheme
(define (square x) (* x x))
(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even? n) (fast-expt (square b) (/ n 2)))
        (else (* b (fast-expt b (- n 1))))))
```
を反復再帰にすればよい．ヒントとしてnが偶数（even）のとき，$b^n = (b^2)^{n/2}$が与えられている．
つまり，$b^n$は低(base)を$b^2$として$n/2$乗したものと同じになる．
従って，次のように解ける．
```scheme
(define (square x) (* x x))

(define (even? x)
  (= (remainder x 2) 0))

(define (fast-expt b n)
  (define (iter a b n)
    (cond ((= n 0) a)
          ((even? n) (iter a (square b) (/ n 2)))
          (else (iter (* a b) b (- n 1) )))
          )
  (iter 1 b n))

```

Q 1.17
------
```
if b is even -> a*b = 2*(a*b/2)
else -> a*b = a*(b-1)+a
```

上記を表現すれば良いだけ

```scheme
(define (double x) (+ x x))
(define (halve x) (/ x 2))
(define (even? x)
(= (remainder x 2) 0))
(define (mul a b)
  (cond ((= b 0) 0)
     ((= b 1) a)
     ((even? b) (double (mul a (halve b))))
     (else (+ a (mul a (- b 1))))
    )
  )
(mul 2 3)
6
(mul 4 8)
32
(mul 4 8)
32
```

Q1.18
-------
```scheme
(define (double x) (+ x x))
(define (halve x) (/ x 2))
(define (even? x)
(= (remainder x 2) 0))
(define (mul a b)
  (define (iter ans a b)
      (cond ((= b 0) 0)
         ((= b 1) ans)
         ((even? b) (iter (double ans) a (halve b)))
         (else (iter (+ a ans) a (- b 1)))
        )
    )
    (iter ans a b)
  )
```

Q1.19
------
久しぶりに問題をとく
まず，問題で言及されているように，Tpqは変換器である
つまり，Transformerである．ここで，
Tpqが特殊なはp=0, q=1といっているまた，そのとき

```scheme
a = a + b
b = a
行列で表すと

(1 1)(a)
(1 0)(b)

この左側の行列をp, qで表すと
(p+q q)
(q   p)

となる．ただし，a = fib(n+1), b = fib(n)であるこに注意
今，ベクトルvk= (fib(n+1), fib(n))を考えるつまり vk = (a,b)である
vk+1は
vk+1 = T*vk
と表現できる．さらにvk+2は
vk+2 = T*vk+1 = T^2 * vk
よって，今回はT^2を求めればよい．
また，
T = (p+q q)
    (q   q)
なので，
T^2 = ( (p+q)^2+q  q^2 + 2pq)
      ( pq+2q^2    q^2 + p^2)
Tと比べると，
q = q^2 + 2pq
p = q^2 + p^2
となる．

これを問題で提示された式にいれれば良い
(define (square x) (* x x))
(define (fib n) (fib-iter 1 0 0 1 n))
(define (fib-iter a b p q count) (cond ((= count 0) b)
        ((even? count)
         (fib-iter a
                   b
                  (+ (square q) (square p))
                  (+ (square q) (* 2 (* p q)))
              (/ count 2)))
              (else (fib-iter (+ (* b q) (* a q) (* a p)) (+ (* b p) (* a q))
                                p
                                q
                                (- count 1)))))

```
Q1.20
-----
gcdのプロセスをnormal-order-evaluationで処理した場合を図示
```scheme
(define (gcd a b)
  (if (= b 0)
      a
  (gcd b (remainder a b))))

if文が来た時に，値を評価し，式を評価する．
そのため，都度ifでは値が評価されるが，gcdでは，最後まで式が評価されないため
modのネストとなる．よって，modが評価される回数は18回である．
（今回は，remainderが長いためmodを利用した）

(gcd 206 40)
  (if (= 40 0))
  (gcd 40 (mod 206 40))
    (if ( = (mod 206 40)  0))
    (gcd (mod 206 40) (mod (mod 206 40) 40))

  evaluated
  (if (= 6 0))
  (gcd (mod 206 40) (mod (mod 206 40) 40))
      (if (= (mod (mod 206 40) 40) 0)
      (gcd (mod 40 (mod 206 40)) (mod (mod 206 40) (mod 40 (mod 206 40))))
  evaluated
  (if (= 4 0))
  (gcd (mod 40 (mod 206 40)) (mod (mod 206 40) (mod 40 (mod 206 40))))
    (if (= (mod (mod 206 40) (mod 40 (mod 206 40))) 0)
    (gcd (mod (mod 206 40) (mod 40 (mod 206 40))) (mod (mod 40 (mod 206 40)) (mod (mod 206 40) (mod 40 (mod 206 40))))

  evaluated
  (if (= 2 0))
   (gcd (mod (mod 40 (mod 206 40)) (mod (mod 206 40) (mod 40 (mod 206 40)))
   (mod (mod (mod 40 (mod 206 40)) (mod (mod 206 40) (mod 40 (mod 206 40))) (mod (mod 206 40) (mod 40 (mod 206 40))))
   (if ( = (mod (mod (mod 40 (mod 206 40)) (mod (mod 206 40) (mod 40 (mod 206 40))) (mod (mod 206 40) (mod 40 (mod 206 40))) 0))
   2



applicative order-evaluation

applicative-order-evaluationは引数を受け取るたびに，式（mod）を評価するため，
実行される回数は少ない．そのため，評価は4回しかされない

(gcd 206 40)
(gcd 40 (mod 206 40))
  (gcd 40 6)
(gcd 6 (mod 40 6))
  (gcd 6 4)
(gcd 4 (mod 6 4))
  (gcd 4 2)
(gcd 2 (mod 4 2))
  (gcd 2 0)
2
```

exercise 1.21
--------------
results:
```scheme
> (smallest-divisior 199)
199
> (smallest-divisior 1999)
1999
> (smallest-divisior 19999)
7
```

exercise 1.22
------------

(runtime)を利用するために，この問題では処理系gauchを利用する
```scheme
(define (smallest-divisior n)
  (find-divisor n 2))

(define (divides? a b)
  (= (remainder b a) 0))

(define (square x)
  (* x x))

(define (find-divisor n test-divisor )
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (+ test-divisor 1)))
  ))

(define (prime? n)
  (= n (smallest-divisior  n)))

(define (runtime)
    (use srfi-11)
    (let-values (((a b) (sys-gettimeofday)))
    (+ (* a 1000000) b)))

(define (search-for-primes n)
  (define (inc-by-odd adder num)
    (+ (* adder 2) 1 num))
  (define (search-for-prime n counter adder)
    (define prime-candidate (inc-by-odd adder n))
    (define start (runtime))
    (if (not (= counter 3))
        (cond ((prime? prime-candidate)
                (display "prime: ")
                (display prime-candidate)
                (display " *** ")
                (display (- (runtime) start))
                (newline)
                (search-for-prime n (+ 1 counter) (+ 1 adder)))
              (else (search-for-prime n counter (+ 1 adder)))
          )
        )
    )

  (search-for-prime n 0 0)
)
```
結果は以下の通りとなる．
```scheme
gosh> (search-for-primes 1000)
prime: 1009 *** 21
prime: 1013 *** 20
prime: 1019 *** 20
#<undef>
gosh> (search-for-primes 10000)
prime: 10007 *** 53
prime: 10009 *** 26
prime: 10037 *** 25
#<undef>
gosh> (search-for-primes 100000)
prime: 100003 *** 136
prime: 100019 *** 107
prime: 100043 *** 107
#<undef>
gosh> (search-for-primes 1000000)
prime: 1000003 *** 286
prime: 1000033 *** 265
prime: 1000037 *** 243
#<undef>
```
`prime?`のアルゴリズムはO(√n)で，
nが10倍されるごとに計算量は√10倍増えるはずである．
以下，それを考察する．

まず`√10= 3.1622776601683795`である．
よって，nが10倍されるごとに大体3倍増えれば良い事になる．
ばらつきがあるものの，大体３倍程度の増加と見られる．

exercise 1.23
-------------
smallest-divisorでfind-divisorは2の後は奇数のみを考慮すべきなので，
```scheme
(next test-divisor)は
if 2 -> 3
else test-divisor + 2
を返せばよい
```

```scheme
(define (smallest-divisior n)
  (find-divisor n 2))

(define (divides? a b)
  (= (remainder b a) 0))

(define (square x)
  (* x x))

(define (find-divisor n test-divisor )
  (cond ((> (square test-divisor) n) n)
        ((divides? test-divisor n) test-divisor)
        (else (find-divisor n (next test-divisor)))
  ))

(define (next n)
  (if (= n 2)
      3
    (+ n 2))
  )
(define (prime? n)
  (= n (smallest-divisior  n)))

(define (runtime)
    (use srfi-11)
    (let-values (((a b) (sys-gettimeofday)))
    (+ (* a 1000000) b)))

(define (search-for-primes n)
  (define (inc-by-odd adder num)
    (+ (* adder 2) 1 num))
  (define (search-for-prime n counter adder)
    (define prime-candidate (inc-by-odd adder n))
    (define start (runtime))
    (if (not (= counter 3))
        (cond ((prime? prime-candidate)
                (display "prime: ")
                (display prime-candidate)
                (display " *** ")
                (display (- (runtime) start))
                (newline)
                (search-for-prime n (+ 1 counter) (+ 1 adder)))
              (else (search-for-prime n counter (+ 1 adder)))
          )
        )
    )

  (search-for-prime n 0 0)
)
```
結果は以下の通りである．
```scheme
gosh> (search-for-primes 1000)
prime: 1009 *** 30
prime: 1013 *** 11
prime: 1019 *** 8
#<undef>
gosh> (search-for-primes 10000)
prime: 10007 *** 44
prime: 10009 *** 20
prime: 10037 *** 18
#<undef>
gosh> (search-for-primes 100000)
prime: 100003 *** 115
prime: 100019 *** 68
prime: 100043 *** 64
#<undef>
gosh> (search-for-primes 1000000)
prime: 1000003 *** 292
prime: 1000033 *** 230
prime: 1000037 *** 232
#<undef>
```
前回の結果はこちら
```scheme
gosh> (search-for-primes 1000)
prime: 1009 *** 21
prime: 1013 *** 20
prime: 1019 *** 20
#<undef>
gosh> (search-for-primes 10000)
prime: 10007 *** 53
prime: 10009 *** 26
prime: 10037 *** 25
#<undef>
gosh> (search-for-primes 100000)
prime: 100003 *** 136
prime: 100019 *** 107
prime: 100043 *** 107
#<undef>
gosh> (search-for-primes 1000000)
prime: 1000003 *** 286
prime: 1000033 *** 265
prime: 1000037 *** 243
#<undef>
```

前回と比較するとステップが確かに多少小さくなっているが，半分まではいかないように見られる．

###### 考察
理由としては，O(√n)だと/2は定数で，nが大きくならないと余り意味をなさない可能性がある．
n~=1000000にしろ1000ステップ程度しか必要ない．それが500になっても計算速度的にあまりかわないと思われる．
もう少し大きな値だと違いが出るかもしれない．

そこで，値を大きくしてみた
```scheme
;; nextを使った場合
gosh> (search-for-primes 10000)
prime: 10007 *** 39
prime: 10009 *** 21
prime: 10037 *** 21
#<undef>
gosh> (search-for-primes 100000)
prime: 100003 *** 120
prime: 100019 *** 76
prime: 100043 *** 94
#<undef>
gosh> (search-for-primes 1000000)
prime: 1000003 *** 164
prime: 1000033 *** 137
prime: 1000037 *** 138
#<undef>
gosh> (search-for-primes 10000000)
prime: 10000019 *** 505
prime: 10000079 *** 494
prime: 10000103 *** 494
#<undef>
gosh> (search-for-primes 100000000)
prime: 100000007 *** 1731
prime: 100000037 *** 1527
prime: 100000039 *** 1262
#<undef>
gosh> (search-for-primes 1000000000)
prime: 1000000007 *** 4415
prime: 1000000009 *** 3258
prime: 1000000021 *** 3116
#<undef>
gosh> (search-for-primes 10000000000)
prime: 10000000019 *** 13114
prime: 10000000033 *** 16093
prime: 10000000061 *** 13632
#<undef>
gosh> (search-for-primes 100000000000)
prime: 100000000003 *** 37946
prime: 100000000019 *** 39128
prime: 100000000057 *** 39868
#<undef>
gosh> (search-for-primes 1000000000000)
prime: 1000000000039 *** 120502
prime: 1000000000061 *** 120939
prime: 1000000000063 *** 132627
#<undef>
gosh> (search-for-primes 10000000000000)
prime: 10000000000037 *** 364994
prime: 10000000000051 *** 315310
prime: 10000000000099 *** 377923
#<undef>
gosh> (search-for-primes 100000000000000)
prime: 100000000000031 *** 1213539
prime: 100000000000067 *** 1182575
prime: 100000000000097 *** 1258980
```
古いバージョンの場合
```scheme
gosh> (search-for-primes 10000)
prime: 10007 *** 77
prime: 10009 *** 32
prime: 10037 *** 30
#<undef>
gosh> (search-for-primes 100000)
prime: 100003 *** 158
prime: 100019 *** 93
prime: 100043 *** 92
#<undef>
gosh> (search-for-primes 1000000)
prime: 1000003 *** 288
prime: 1000033 *** 257
prime: 1000037 *** 223
#<undef>
gosh> (search-for-primes 10000000)
prime: 10000019 *** 881
prime: 10000079 *** 695
prime: 10000103 *** 640
#<undef>
gosh> (search-for-primes 100000000)
prime: 100000007 *** 2472
prime: 100000037 *** 1627
prime: 100000039 *** 1669
#<undef>
gosh> (search-for-primes 1000000000)
prime: 1000000007 *** 8216
prime: 1000000009 *** 5620
prime: 1000000021 *** 5130
#<undef>
gosh> (search-for-primes 10000000000)
prime: 10000000019 *** 16116
prime: 10000000033 *** 16893
prime: 10000000061 *** 19742
#<undef>
gosh> (search-for-primes 100000000000)
prime: 100000000003 *** 59237
prime: 100000000019 *** 60923
prime: 100000000057 *** 60863
#<undef>
gosh> (search-for-primes 1000000000000)
prime: 1000000000039 *** 205850
prime: 1000000000061 *** 175359
prime: 1000000000063 *** 180902
#<undef>
gosh> (search-for-primes 10000000000000)
prime: 10000000000037 *** 563074
prime: 10000000000051 *** 581707
prime: 10000000000099 *** 531112
#<undef>
gosh> (search-for-primes 100000000000000)
prime: 100000000000031 *** 1681545
prime: 100000000000067 *** 1745277
prime: 100000000000097 *** 1651683
#<undef>
```
値が大きくなるほど，1/2に近づいていることが分かる．よって，nextを使う事により
ステップ数が半分になることが得られた．

が，下記の解答が素晴らしい
> We're seeing a clear improvement in the new procedure, but it's not quite as fast as we expected. The first thing that needs to be explained in this data is the fact that the first three values shows very little performance gain, the next three a little more, then fairly consistent results for the remaining data. I think this can be explained by other processes running on the computer. Measuring shorter runs of the procedure (those in the 100-500 millisecond range) is going to be much more sensitive to measurement error due to being interrupted by background processes. These errors will be a less significant proportion of the total run time for longer runs of the procedure.

> We're also seeing that the procedure is only running approximately 1.85 times as fast, instead of the expected factor of 2. This may be explained by the fact that we replaced a primitive operation, (+ test-divisor 1), by a user-defined operation, (next test-divisor). Each time that user-defined operation is called, an extra if must be evaluated (to check if the input is 2). Other than this small discrepancy, I think the improvement is quite good for such a small change to the code.

このURLから引用: [http://www.billthelizard.com/2010/02/sicp-exercise-123-improved-prime-test.html](http://www.billthelizard.com/2010/02/sicp-exercise-123-improved-prime-test.html)

exercise 1.24
------------
```scheme
(use math.mt-random)
(define m (make <mersenne-twister> :seed (sys-time)))
(mt-random-integer m 1000)
(define (random n) (mt-random-integer m n))

(define (square x) (* x x))

(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder (square (expmod base (/ exp 2) m))
m)) (else
         (remainder (* base (expmod base (- exp 1) m))
                    m))))

(define (fermat-test n)
  (define (try-it a)
    (= (expmod a n n) a))
  (try-it (+ 1 (random (- n 1)))))

(define (fast-prime? n times)
  (cond ((= times 0) #t)
        ((fermat-test n) (fast-prime? n (- times 1)))
        (else #f)))

(define (runtime)
    (use srfi-11)
    (let-values (((a b) (sys-gettimeofday)))
    (+ (* a 1000000) b)))

(define (search-for-primes n)
  (define (inc-by-odd adder num)
    (+ (* adder 2) 1 num))
  (define (search-for-prime n counter adder)
    (define prime-candidate (inc-by-odd adder n))
    (define start (runtime))
    (if (not (= counter 3))
        (cond ((fast-prime? prime-candidate 7)
                (display "prime: ")
                (display prime-candidate)
                (display " *** ")
                (display (- (runtime) start))
                (newline)
                (search-for-prime n (+ 1 counter) (+ 1 adder)))
              (else (search-for-prime n counter (+ 1 adder)))
          )
        )
    )

  (search-for-prime n 0 0)
)
```
結果は以下の通りである
```scheme
gosh>  (search-for-primes 10000)
prime: 10007 *** 144
prime: 10009 *** 188
prime: 10037 *** 110
#<undef>
gosh>  (search-for-primes 100000)
prime: 100003 *** 211
prime: 100019 *** 221
prime: 100043 *** 138
#<undef>
gosh>  (search-for-primes 1000000)
prime: 1000003 *** 188
prime: 1000033 *** 297
prime: 1000037 *** 307
#<undef>
gosh>  (search-for-primes 10000000)
prime: 10000019 *** 9304
prime: 10000079 *** 333
prime: 10000103 *** 284
#<undef>
gosh>  (search-for-primes 100000000)
prime: 100000007 *** 289
prime: 100000037 *** 232
prime: 100000039 *** 233
#<undef>
gosh>  (search-for-primes 1000000000)
prime: 1000000007 *** 268
prime: 1000000009 *** 256
prime: 1000000021 *** 254
#<undef>
gosh>  (search-for-primes 10000000000)
prime: 10000000019 *** 731
prime: 10000000033 *** 493
prime: 10000000061 *** 413
#<undef>
gosh>  (search-for-primes 100000000000)
prime: 100000000003 *** 549
prime: 100000000019 *** 582
prime: 100000000057 *** 1069
#<undef>
gosh>  (search-for-primes 1000000000000)
prime: 1000000000039 *** 491
prime: 1000000000061 *** 497
prime: 1000000000063 *** 494
#<undef>
gosh>  (search-for-primes 10000000000000)
prime: 10000000000037 *** 560
prime: 10000000000051 *** 553
prime: 10000000000099 *** 548
#<undef>
gosh>  (search-for-primes 100000000000000)
prime: 100000000000031 *** 905
prime: 100000000000067 *** 804
prime: 100000000000097 *** 6140
```

checkする回数を15 -> 7にした場合．
```scheme
gosh>
(search-for-primes 10000)
prime: 10007 *** 100
prime: 10009 *** 79
prime: 10037 *** 66
#<undef>
gosh> (search-for-primes 100000)
prime: 100003 *** 75
prime: 100019 *** 63
prime: 100043 *** 62
#<undef>
gosh> (search-for-primes 1000000)
prime: 1000003 *** 123
prime: 1000033 *** 89
prime: 1000037 *** 91
gosh> (search-for-primes 100000000000000)
prime: 100000000000031 *** 299
prime: 100000000000067 *** 278
prime: 100000000000097 *** 484
```
prime?を使った場合
```scheme
gosh> (search-for-primes 1000)
prime: 1009 *** 21
prime: 1013 *** 20
prime: 1019 *** 20
```
比較した場合は，もちろんfast-primeの方が圧倒的に速いが
log(n)/(√n)の比まではならない．１つの理由として，fast-primeは`O(t*log(n)) | t :testする回数t`
であるからである．それでも多少大きいのは関数呼び出しなどが起因していると考えられる.

また，fast-prime?のorder of growthを見ると
```
10000 -> 100000000000000
log(10000000000)/log(10000) = 3倍
```
よって，3倍程度増えているので，logarithmaticに増えていると言える．



10倍ごとに約log(10)=2.3倍あがっていることが見受けられる

exercise 1.25
-----------

```scheme
(use math.mt-random)
(define m (make <mersenne-twister> :seed (sys-time)))
(mt-random-integer m 1000)
(define (random n) (mt-random-integer m n))

(define (square x) (* x x))

(define (even? x)
  (= (remainder x 2) 0))

(define (fast-expt b n)
  (define (iter a b n)
    (cond ((= n 0) a)
          ((even? n) (iter a (square b) (/ n 2)))
          (else (iter (* a b) b (- n 1) )))
          )
  (iter 1 b n))

(define (expmod base exp m)
  (remainder (fast-expt base exp) m))

(define (fermat-test n)
  (define (try-it a)
    (= (expmod a n n) a))
  (try-it (+ 1 (random (- n 1)))))

(define (fast-prime? n times)
  (cond ((= times 0) #t)
        ((fermat-test n) (fast-prime? n (- times 1)))
        (else #f)))

```
expmodを変更したらfast prime testerのように高速ではなくなった．
その理由は
expmodであれば，再帰的に得られたexpmodに2乗か，base倍し，その値のremainderを取り，値はm以下になる．
それを再帰的に繰り返す．よって，operandの値は比較的小さくすむ．

対して，fast-exptを利用する場合は，入力nの値が大きいと，operandが多くなる．したがって，値を格納しているサイズを変更しないといけなくなる．
e.g int -> longそのため，値が大きくなると計算量がかかり，遅くなってしまう．

今回の例は，log(n) でも対象となる値が大きくなれば，値の変換等により計算不能になることである．

exercise 1.26
------------
変更をしたことにより，(exmod base (/exp 2) m)が一度につき2度行われる．本来ならevenで，計算を半分にしていくのに対して，
2回行ってしまうため，O(n)に戻ってしまう．（再帰的に呼ばれるものが2回，4回と増えていく）

この図を見るとより意味がわかる

![](http://3.bp.blogspot.com/_PnLYRqe0k9g/S4RADXPrAXI/AAAAAAAAARk/yJESpD2zwhQ/s1600/expmod-mult-diagram.png)

[sicp-exercise-126-explicit.htmlより参照](http://www.billthelizard.com/2010/02/sicp-exercise-126-explicit.html)

exercise 1.27
----------
tests whether an is congruent to a modulo n for every a < n
algo
```python
def is_congruent(n):
  for a in 2..n-1
    if a^n mod n != a:
      return false
  return true
```
以下，scheme
```scheme
(define (square x) (* x x))
(define (even? x)
  (= (remainder x 2) 0))

(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (remainder (square (expmod base (/ exp 2) m)) m))
         (else (remainder (* base (expmod base (- exp 1) m)) m))))

(define (congruent? n)
    (define (try-it a)
      (cond ((= a (- n 1)) #t)
            ((not (= (expmod a n n) a)) #f)
            (else (try-it (+ a 1)))
        )
      )
  (try-it 2)
  )

(congruent? 561)
(congruent? 1105)
(congruent? 1729)
(congruent? 2465)
(congruent? 2821)
(congruent? 6601)
```
結果は以下の通りになり，Carmichael　number nはa^n is congruent a modulo n for all a < n.
carmicheal number n は全てのa < nに対してnをほうとしてa^n はaに合同であることがわかる．
```
> (congruent? 561)
#t
> (congruent? 561)
#t
> (congruent? 1105)
#t
> (congruent? 1729)
#t
> (congruent? 2465)
#t
> (congruent? 2821)
#t
> (congruent? 6601)
#t
> (congruent? 2)
#f
> (congruent? 4)
#f
> (congruent? 8)
#f
> (congruent? 3)
#t
````

better solution

```
fermat-testを再利用し，fermat-fullでのロジックも見やすく成っている．
fermat-testが通らなければ，というふうに

(define (fermat-test n a)
   (= (expmod a n n) a))

(define (fermat-full n)
   (define (iter a)
     (cond ((= a 1) #t)
           ((not (fermat-test n a)) #f)
           (else (iter (- a 1)))))
   (iter (- n 1)))

```
exercise 1.28
------------
miler rabin test
a^(n-1) ≡ 1 modulo n

```python
test n
if a^(n - 1) ≡ modulo n

if even?
  if num^2 moudlo n = 1 s.t num != n or n-1
    num is not prime
```

```scheme
(use math.mt-random)
(define m (make <mersenne-twister> :seed (sys-time)))
(mt-random-integer m 1000)
(define (random n) (mt-random-integer m n))

(define (square x) (* x x))
(define (not-one? n)
  (= n 1))
(define (different? n x)
  (= n x))
(define (nontrivial-square-root? n m)
  (= (remainder (square m) m) 1))

(define (square-check n m)
  (if (and (not-one? n) (different? n (- m 1)) (nontrivial-square-root? n m))
  0
  (remainder (square n) m)))


(define (expmod base exp m)
  (cond ((= exp 0) 1)
        ((even? exp)
         (square-check (expmod base (/ exp 2) m) m))
        (else (remainder (* base (expmod base (- exp 1) m)) m))))

(define (miler-rabin-test n)
  (define (try-it a)
    (= (expmod a (- n 1) n) 1))
  (try-it (+ 1 (random (- n 1)))))

(define (fast-prime? n times)
  (cond ((= times 0) #t)
        ((miler-rabin-test n) (fast-prime? n (- times 1)))
        (else #f)))
(define (prime? n)
  (fast-prime? n 10))


(prime? 561)
(prime? 1105)
(prime? 1729)
(prime? 2465)
(prime? 2821)
(prime? 6601)
```
結果
```
(prime? 561)
#f
(prime? 1105)
#f
(prime? 1729)
#f
(prime? 2465)
#f
(prime? 2821)
#f
gosh> (prime? 6601)
#f
```
