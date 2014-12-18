Q1.9
----
(define (+ a b)
  (if (= a 0)
      b
      (inc (+ (dec a) b))))

(define (+ a b)
  (if (= a 0)
      b
      (+ (dec a) (inc b))))

最初の手続きのsubstitution model:
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
従って，再帰プロセス

二番目:
(+ 4 5)
(+ 3 6)
(+ 2 7)
(+ 1 8)
(+ 0 9)
9
従って，反復プロセス
		