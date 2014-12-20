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
