;; Scheme ;;

(define (over-or-under x y)
  (cond 
    ((> x y) 1)
    ((< x y) -1)
    (else 0)
  )
)

;;; Tests
(over-or-under 1 2)
; expect -1
(over-or-under 2 1)
; expect 1
(over-or-under 1 1)
; expect 0

(define (filter-lst f lst)
  (if (null? lst)
    '()
    (if (f (car lst))
      (append (list (car lst)) (filter-lst f (cdr lst)))
      (filter-lst f (cdr lst))
    )
  )
)

;;; Tests
(define (even? x)
  (= (modulo x 2) 0))
(filter-lst even? '(0 1 1 2 3 5 8))
; expect (0 2 8)

(define (make-adder num)
  (lambda (x) (+ num x))
)

;;; Tests
(define adder (make-adder 5))
(adder 8)
; expect 13

;; Extra questions

(define lst
  (cons
    (cons 1 nil)
    (cons 2
      (cons
        (cons 3 (cons 4 nil))
        (cons 5 nil)
      )
    )
  )
)

(define (composed f g)
  (lambda (x) (f (g x)))
)

(define (remove item lst)
  (filter-lst (lambda (x) (not (equal? x item))) lst)
)


;;; Tests
(remove 3 nil)
; expect ()
(remove 3 '(1 3 5))
; expect (1 5)
(remove 5 '(5 3 5 5 1 4 5 4))
; expect (3 1 4 4)

(define (no-repeats s)
  (if (null? s) 
    '()
    (append (list(car s)) (no-repeats(filter-lst (lambda (x) (not (equal? x (car s)))) (cdr s))))
  )
)

(define (substitute s old new)
  (if (null? s)
    '()
    (if (pair? (car s))
      (append (list(substitute (car s) old new)) (substitute (cdr s) old new))
      (if (eq? (car s) old)
        (append (list new) (substitute (cdr s) old new))
        (append (list (car s)) (substitute (cdr s) old new))
      )
    )
  )
)


(define (sub-all s olds news)
  'YOUR-CODE-HERE
)