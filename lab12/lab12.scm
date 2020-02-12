(define (partial-sums stream)
  (define (helper n s)
    (if (null? s)
      nil
      (cons-stream (+ n (car s)) (helper (+ n (car s)) (cdr-stream s)))
    )
  )
  (helper 0 stream)
)