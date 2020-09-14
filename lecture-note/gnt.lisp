;;;; gnt.lisp -- genetic algorithm.

;;; outline of genetic algorithm

;; args
;; ((:type functionp state1 state2 )..)
(srl '(1) :combine #'append :result #'car
     #'(lambda (s) (eq 15 s))
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

;; (defstruct (group (:type list))
;;    function states)

;; args: ((compare-function state1 state2 ...) ..), compare function in args: (lambda (s))


(defun srl (states goalp successors &key
				      (combine #'append)
				      (result #'car)
				      (selector #'car)
				      (post-process #'identity)
				      (generate-new-states #'(lambda (s c a) (declare (ignore s a)) c)))
  "Generic search function."
  (lambda (&rest args)
    (if (null states)
	(error "starved states.")
	(let ((state (funcall selector states)))
	  (if (funcall goalp (funcall selector states))
	      (funcall result states)
	      (let* ((candidate-states (funcall successors state))
		     (filtered-states (funcall state generate-new-states candidate-states args))
		     (new-states (funcall combine
					  ;; pick candidate-states satisfied group justifying
					  ;; if need, post processing (ex. order filtered states
					  (funcall post-process filtered-states)
					  (cdr states))))
		;; TODO: how to treat current state?
		;; find proper group and update the group with the state.
		(apply (funcall #'srl new-states goalp successors
			 :result result :selector selector :combine combine
			 :post-process post-process :generate-new-states generate-new-states)
		       args)))))))

(defstruct (filters (:type list))
  type compare-fn update-fn states)

;; reference args may be many, how to decide new-states's compare-function
;; as it is

;; group: ((type1 c-fn1 u-fn1 states) (type2 c-fn1 u-fn1 states) ...)

;; selector choose one of states. (car states)
;; cf. when use &rest and &key parameter, use &allow-other-keys
(defun generate-new-states (state candidate-states filters &optional passed) ; passed is acc
  ""
  ;; TODO: assert type is struct of filters
  (cond ((null candidate-states) passed)
	((justify-state state (car candidate-states) filters)
	 (generate-new-states state (cdr candidate-states) filters passed))
	(t (generate-new-states state (cdr candidate-states) filters
				(append passed (list (car candidate-states)))))))

;; must visit groups
;; return what? if result is nil, nil. otherwise, trivial, no meaning result for now.
(defun justify-state (state c-state filters &optional result)
  (cond ((null filters) result)
	
	((null result) (justify-state state c-state (cdr filters)
				      (funcall %justify-state state c-state (car filters))))
	(t (justify-state state c-state (cdr filters)
			  (cons (funcall %justify-state state c-state (car filters)) result)))))

;; specific
(defun %justify-state (state c-state filter)
  )

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;; application

(defun prepend (x y)
  (append y x))

;; state: '(1 2 3 4 5 ..)
;; breath-first-search of tree
(defun breath-first-search (states goalp)
  (srl states goalp #'prepend result))

