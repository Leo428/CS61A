;;; Scheme Recursive Art Contest Entry
;;;
;;; Please do not include your name or personal info in this file.
;;;
;;; Title: <Your title here>
;;;
;;; Description:
;;;   <It's your masterpiece.
;;;    Use these three lines to describe
;;;    its inner meaning.>

(define (drawcircle radius x y)
  (penup)
  (setposition x y)
  (pendown)
  ; (begin_fill)
  (circle radius)
  ; (end_fill)
  (penup)
)

(define (draw)
  (print (screen_width))
  (print (screen_height))
  (bgcolor "#ffc0c0")
  (speed 0)

  (pendown)
  (forward 100)
  (drawcircle 100 100 100)
  (exitonclick)
)

; Please leave this last line alone.  You may add additional procedures above
; this line.
(draw)