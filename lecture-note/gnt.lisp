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


(defun srl (states fgoalp fsuccessors &key
					(fcombine #'append)
					(fresult #'car)
					(fselector #'car)
					(f-post-process #'identity)
					(ffilterer #'(lambda (s c f)
						       (declare (ignore s c f)))))
  "Generic search function."
  (lambda (&rest args)
    (if (null states)
	(error "starved states.")
	(let ((state (funcall fselector states)))
	  (if (funcall fgoalp (funcall fselector states))
	      (funcall fresult states)
	      (let* ((candidate-states (funcall fsuccessors state))
		     (filtered-states (generate-new-states state candidate-states args ffilterer))
		     (new-states (funcall fcombine
					  ;; pick candidate-states satisfied group justifying
					  ;; if need, post processing (ex. order filtered states
					  (funcall f-post-process filtered-states)
					  (cdr states))))
		;; TODO: how to treat current state?
		;; find proper group and update the group with the state.
		(apply (funcall #'srl new-states fgoalp fsuccessors
				:fresult fresult :fselector fselector :fcombine fcombine
				:f-post-process f-post-process :ffilterer ffilterer)
		       args)))))))

(defstruct (filter (:type list))
  type fcompare fupdate states)

;; reference args may be many, how to decide new-states's compare-function
;; as it is

;; group: ((type1 c-fn1 u-fn1 states) (type2 c-fn1 u-fn1 states) ...)

;; selector choose one of states. (car states)
;; cf. when use &rest and &key parameter, use &allow-other-keys
;; filters: '((1 2 3..) (3 4 5).. ),
;;          '((:t1 #'eq #'adjoin '(1 2 3..)), (:t2 #'eql #'append '(10 9 8..))..)
;; passed is acc
;; TODO: how to return updated filters with others.
(defun generate-new-states (state candidate-states filters ffilterer &optional passed) 
  ""
  ;; TODO: assert type is struct of filters
  (cond ((null candidate-states) passed)
	((justify-state state (car candidate-states) filters ffilterer)
	 (generate-new-states state (cdr candidate-states) filters passed))
	(t (generate-new-states state (cdr candidate-states) filters
				(append passed (list (car candidate-states)))))))

;; must visit groups
;; return what? if result is nil, nil. otherwise, trivial, no meaning result for now.
;; fprocess return a function which have 3 arguments(state c-state states)
(defun justify-state (state c-state filters ffilterer &optional result)
  (cond ((null filters) result)
	((null result) (justify-state state c-state (cdr filters)
				      (funcall ffilterer state c-state (car filters))))
	(t (justify-state state c-state (cdr filters)
			  (cons (funcall ffilterer state c-state (car filters)) result)))))

;; specific filterer
;; case: normal or using filter structure
;; normal:
;;   filter: '(1 2 3 4.. )
;; filter structure
;;   filter: '(type fcompare fupdate states)
(defun fmake-filterer (&key (fget-states #'identity) (fcompare #'eq) (fupdate #'adjoin))
  (lambda (state c-state filter)
    (let ((old-states (funcall fget-states filter))
	  (updated-states (funcall fupdate state (funcall fget-states filter)))
	  (r nil)) ; r need for removeing c-state. That time, r is non-nil.
      (dolist (old old-states (values r updated-states))
		   (setf r (or r (funcall fcompare old c-state)))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;; application

(defun prepend (x y)
  (append y x))

;; state: '(1 2 3 4 5 ..)
;; breath-first-search of tree
(defun breath-first-search (states goalp)
  (srl states goalp #'prepend result))

