(define quine
    (
        (lambda (x) 
            `(,x ',x)
        )
        '(lambda (x) `(,x ',x))
    )
)