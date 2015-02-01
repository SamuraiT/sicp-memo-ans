Q1.9
----

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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

```
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


```
(define (square x) (* x x))
(define (fast-expt b n)
  (cond ((= n 0) 1)
        ((even? n) (fast-expt (square b) (/ n 2)))
        (else (* b (fast-expt b (- n 1))))))
```
を反復再帰にすればよい．ヒントとしてnが偶数（even）のとき，$b^n = (b^2)^{n/2}$が与えられている．
つまり，$b^n$は低(base)を$b^2$として$n/2$乗したものと同じになる．
従って，次のように解ける．
```
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

```
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

Q1.19
------
久しぶりに問題をとく
まず，問題で言及されているように，Tpqは変換器である
つまり，Transformerである．ここで，
Tpqが特殊なはp=0, q=1といっているまた，そのとき

```
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
```
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
```
> (smallest-divisior 199)
199
> (smallest-divisior 1999)
1999
> (smallest-divisior 19999)
7
```
