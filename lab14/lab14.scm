; Lab 14: Final Review

(define (compose-all funcs)
  (if (null? funcs)
    (lambda (x) x)
    (lambda (x)
      ((compose-all (cdr funcs)) ((car funcs) x))
    )
  )
)

; (define (has-cycle? s)
;   (define (pair-tracker seen-so-far curr)
;     (cond (_________________ ____________)
;           (_________________ ____________)
;           (else _________________________))
;     )
;   ______________________________
; )
(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond 
      ((null? curr) #f)
      ((contains? seen-so-far (car curr)) #t)
      (else (pair-tracker (append (list (car curr)) seen-so-far) (cdr-stream curr)))
    )
  )
  (pair-tracker nil s)
)

(define (contains? lst s)
  (if (null? lst)
    #f
    (if (eq? (car lst) s) ;same location in memory
      #t
      (contains? (cdr lst) s)
    )
  )
)

