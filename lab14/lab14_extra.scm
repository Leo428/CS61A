
; (define-macro (switch expr cases)
  
;   (define-macro (create_case x)
;     ; (print `((eq? ,expr ,(car x)) ,(car (cdr x))))
;     ; `((eq? ,expr (quote ,(car x))) ,(car (cdr x)))
;     `(eq? ,expr (quote ,(car x)))
;   )
; ;   (print expr)
; ;   (print (car cases))
;   ; (if (null? cases)
;   ;   nil
;   ;   (if (null? (cdr cases))
;   ;     `(cond
;   ;       ,(create_case (car cases))
;   ;     )
;   ;     
;   ;     `(cond
;   ;       ,(create_case (car cases))
;   ;       ; (else ,(switch ,expr ,(cdr cases)))
;   ;       (else `,(switch ,expr ,(cdr cases)))
;   ;     )
;   ;   )
;   ; )
;   `(cond
;     (map ,create_case cases)
;   )
; )

(define-macro (switch expr cases)
  (cons 'cond
    (map
      (lambda (case) (cons `(equal? ,expr ',(car case)) (cdr case))) ;cons used to make ()
      cases
    )
  )
  ;(cond ((equal? ,expr )))
)