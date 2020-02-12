
; Tail recursion

(define (replicate x n)
  (define (helper n sofar)
    (if (= n 0)
      sofar
      (helper (- n 1) (cons x sofar))
    )
  )
  (helper n nil)
)

(define (accumulate combiner start n term)
  (if (= n 0)
    start
    (combiner start (accumulate combiner (term n) (- n 1) term))
  )
)

(define (accumulate-tail combiner start n term)
  (define (helper n sofar)
    (if (= n 0)
      sofar
      (helper (- n 1) (combiner sofar (term n)))
    )
  )
  (helper n start)
)

; Streams

(define (map-stream f s)
    (if (null? s)
    	nil
    	(cons-stream (f (car s)) (map-stream f (cdr-stream s)))))

(define multiples-of-three
  (cons-stream 3 (map-stream (lambda (x) (+ x 3)) multiples-of-three))
)


(define (nondecreastream s)
  ;obtaining the first list of nondecreasing nums from a stream
  (define (helper previous strm)
    (if (null? strm) nil
      (if (>= (car strm) previous)
        (if (null? (cdr-stream strm))
          (cons (car strm) nil)
          (cons (car strm) (helper (car strm) (cdr-stream strm)))
        )
        nil
      )
    )
  )
  ;obtaining the rest of the stream, starting from the first nondecreasing num
  (define (rest previous strm)
    (if (null? strm) nil
      (if (>= (car strm) previous)
        (if (null? (cdr-stream strm))
          nil
          (rest (car strm) (cdr-stream strm))
        )
        strm
      )
    )
  )
  ; (helper 0 s)
  ; (rest 0 s)
  ; (cons-stream (cons (car s) (helper (car s) (cdr-stream s))) (nondecreastream (rest 0 s)))
  (if (null? s) nil
    (cons-stream (helper 0 s) (nondecreastream (rest 0 s)))
  )
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))