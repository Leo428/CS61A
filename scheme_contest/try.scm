;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: Orient
;;;
;;; Description:
;;;   A distant journey
;;;   And a glimpse of beauty
;;;   All in a single frame

; Flowers
(define (flower x y size)
  (define (petal angle)
    (penup)
    (setposition x y)
    (setheading angle)
    (pendown)
    (color "#f4afa6")
    ;(color "#ff8790")
  
    (begin_fill)
    (right 70)
    (circle (* size 1.5) 130)
    (left 100)
    (forward (* size 0.5))
    (right 150)
    (forward (* size 0.5))
    (left 120)
    (circle (* size 1.8) 98)
    (setposition x y)
    (end_fill))

  (define (shadow angle)
    (setheading angle)
    (color "#b2867e")
    (begin_fill)
    (right 88)
    (circle size 89)
    (left 90)
    (circle size 82)
    (setposition x y)
    (end_fill))

  (define (stamen angle)
    (penup)
    (color "#ffeadd")
    (setheading angle)
    (pendown)
    (begin_fill)
    (circle (* size 2) 30)
    (right 90)
    (circle (/ size 10))
    (end_fill)
    (setposition x y))


  (define (repeat-draw p params)
    (if (not (null? params))
      (begin 
        (p (car params))
        (repeat-draw p (cdr params)))))

  (repeat-draw petal '(0 72 144 216 288))  
  (repeat-draw shadow '(0 72 144 216 288))
  (repeat-draw stamen (list (- 72) (- 52) 0 20 40 72 102 132 252)))

(define (flowers)
  (flower (- 120) (- 100) 25)
  (flower 0 (- 100) 15)
  (flower 150 (- 120) 20))

; Branches
(define (branches)
  (define (leaf)
    (color "#ffbe47")
    (right 60)
    (begin_fill)
    (circle 30 120)
    (left 60)
    (circle 30 120)
    (end_fill)
    (right 60))
  
  (define (draw-leaf)
    (forward 20)
    (leaf)
    (color "#281c18")
    (forward 20))
  
  (define (draw-level)
    (right 30)
    (draw-leaf)
    (right 80)
    (draw-leaf)

    ; change the angle...
    (left 110)
    (circle 400 7))

  (define (branch depth) 
    (if (> depth 0)
      (begin 
        (draw-level)
        (branch (- depth 1)))
      (leaf)))

  (penup)
  (setposition 245 200)
  (setheading 270)
  (color "#281c18")
  (pendown)
  (circle 400 6)
  (branch 5))

; Background frame
(define (square x y size c)
  (define (repeat-line times) 
    (if (> times 0)
      (begin 
        (forward size) 
        (left 90) 
        (repeat-line (- times 1)))))

  (penup)
  (setposition x y)
  (color c)
  (pendown)
  (begin_fill)
  (repeat-line 4)
  (end_fill))

(define (frame)
  (square 285 (- 286) 512 "#282828")
  (square 255 (- 256) 512 "black")
  (square 245 (- 246) 492 "#ba2621"))

; Mountain
(define (yama) 
  (penup)
  (color "#282b1d")
  (setposition 245 (- 100))
  (setheading (- 60))
  (pendown)
  (begin_fill)
  (circle 492 60)
  (setposition (- 247) (- 246))
  (setposition 245 (- 246))
  (setposition 245 (- 100))
  (end_fill)

  (color "black")

  (define (repeat-curve params)
    (if (not (null? params))
      (begin
        (penup)
        (setposition 245 (car params))
        (setheading (- 60))
        (pendown)
        (circle 492 60)
        (repeat-curve (cdr params)))))

  (repeat-curve (list (- 120) (- 140) (- 160) (- 190) (- 220) (- 250))))

; Sun
(define (sun)
  (penup)
  (color "white")
  (setposition (- 140) 200)
  (pendown)
  (begin_fill)
  (circle 100)
  (end_fill))

(define (draw)
  (speed 10)
  
  (bgcolor "#505e3f")
  (frame)
  (yama)
  (sun)
  (branches)
  (flowers)

  (hideturtle)
  (exitonclick))

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)