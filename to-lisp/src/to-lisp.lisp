(in-package :to-lisp)
;; x: n x 1, y: n x 1
(defun _dot (x y &optional (acc 0))
  (assert (eq (length x) (length y)))
  (cond ((null x) acc)
	(t (_dot (cdr x) (cdr y) (+ acc (* (car x) (car y)))))))

(defun dot (x y &optional acc)
  (cond ((null x) acc)
	((atom (car x)) (append acc (list (_dot x y))))
	(t (dot (cdr x) y (append acc (dot (car x) y))))))

;; (defun exp (x)
;;   (exp x))


