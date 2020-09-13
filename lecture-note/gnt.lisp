;;;; gnt.lisp -- genetic algorithm.

;;; outline of genetic algorithm

;; args
;; ((:type functionp state1 state2 )..)
(srl-search '(1)
	    #'(lambda (s) (eq 15 s))
	    #'append
	    #'(lambda (states) (print (car states)))
	    #'(lambda (s) (list (+ 1 s) s))
	    #'car
	    #'exist-in-group-p
	    #'identity
	    #'generate-new-states
	    '(eq 1 2 3) '(eq -1 -2 -3) '(eq 10 11 12) '(eq 17 18 19))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 

;; function
;; combine: combine filtered states and rest states like merging and sorting.
;; post-process: 
;; args: ((:type compare-function state1 state2 ...) ..), compare function in args: (lambda (s))
(defun srl-search (states goalp
		   combine result successors selector group-fn post-process generate-new-states
		   &rest args)
  "Generic search function."
  (if (null states)
      (error "starved states.")
      (let ((state (funcall selector states)))
	(if (funcall goalp (funcall selector states))
	    (funcall result states)
	    (let* ((candidate-states (funcall successors state))
		   (filtered-state (apply (funcall generate-new-states
						   candidate-states :group-fn group-fn)
					  args))
		   (new-states (funcall combine
					;; pick candidate-states satisfied group justifying
					;; if need, post processing (ex. order filtered states
					(funcall post-process filtered-state)
					(cdr states))))
	      ;; TODO: how to treat current state?
	      (apply #'srl-search 
		     new-states goalp combine result
		     successors selector group-fn post-process generate-new-states args))))))

;; reference args may be many, how to decide new-states's compare-function
;; as it is
;; group: ((c-fn1 . (s11 s12 s13 ..)) (c-fn2 . (s21 s22 s23 ..)))
;; selector choose one of states. (car states)
;; cf. when use &rest and &key parameter, use &allow-other-keys
(defun generate-new-states (candidate-states &key group-fn)
  "Cause of various data type, set how to apply group function, where group-fn in data."
  (lambda (&rest group)
    (apply #'%generate-new-states candidate-states group-fn group)))

;; test all args(=compare group) and if found in group, remove from candidate
(defun %generate-new-states (candidate-states group-fn &rest args)
  (remove-if (funcall group-fn args) candidate-states))

(defun exist-in-group-p (group)
  (labels ((iterate-states (fn s states)
	     (if (null states)
		 nil
		 (or (funcall fn s (car states)) (iterate-states fn s (cdr states)))))
	   (apply-each-group (s g)
	     (iterate-states (car g) s (cdr g)))
	   (iterate-group (s g)
	     (if (null g)
		 nil
		 (or (apply-each-group s (car g)) (iterate-group s (cdr g))))))
    (lambda (s)
      (iterate-group s group))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

