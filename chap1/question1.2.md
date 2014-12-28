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
