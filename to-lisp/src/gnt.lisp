;;;; gnt.lisp -- genetic algorithm.

;;; outline of genetic algorithm

;; args
;; ((:type functionp state1 state2 )..)
(funcall (srl '(1) 
	    #'(lambda (x) (eq 15 x))
	    #'(lambda (x) (list (+ 1 x) x)))
	 '((1 2 3) '(-1 -2 -3)))

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
					;; fupdate: need to treat nil case. (make filters or not)
					;; if nil, there aren't filters to refer. 
					(fupdate #'%update-each) 
					(f-post-process #'identity)
					(ffilterer #'(lambda (c f &optional s)
						       (or (member c (cdr s))
							   (member c f)))))
  "Generic search function."
  ;; NOTE: If use &rest, can't deal nil case. Because apply function need 1 arg at least.
  ;; So, If use &optional, it must use funcall. And args must be list.
  
  (lambda (&optional args)
    (if (null states)
	(error "starved states.")
	;; state is best choice
	(let ((state (funcall fselector states)))
	  (if (funcall fgoalp state)
	      (funcall fresult states)
	      ;; (....) select 1 state
	      ;; (1 2 3 4 5 6 7) -> (2 3 4 5 6 7) is candidated states
	      (let* ((candidate-states (funcall fsuccessors state))
		     ;; Update visited cur state to filters
		     ;; TODO: If args nil, make filters or not.
		     
		     ;; ex. args is old-path-list
		     (updated-filters (if (null fupdate) args (updater state args fupdate)))
                                      ;; (and fupdate (updater state args fupdate)))
		     
		     (filtered-states (generate-new-states states candidate-states
							   updated-filters ffilterer))
		     
		     (new-states (funcall fcombine
					  ;; pick candidate-states satisfied group justifying
					  ;; if need, post processing (ex. order filtered states
					  (funcall f-post-process filtered-states)
					  (cdr states))))
		(format t
			"states ~a~%c-states ~a~%updated-filters ~a ~%filtered ~a~%new-states~a ~%"
			states candidate-states updated-filters filtered-states new-states)
		(funcall (srl new-states fgoalp fsuccessors
				:fresult fresult :fselector fselector :fcombine fcombine
				:fupdate fupdate
				:f-post-process f-post-process :ffilterer ffilterer)
		       updated-filters)))))))

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
;;       need to update old-filters with THE state argument and filter with c-states.
;;       update, here.
(defun generate-new-states (states candidate-states filters ffilterer &optional passed) 
  ""
  ;; TODO: assert type is struct of filters
  (format t "states ~a~%c-states ~a~%filters ~a~% ffilterer ~a~%passed ~a~%" states candidate-states filters ffilterer passed)
  (cond ((null candidate-states) passed)
	((justify-state states (car candidate-states) filters ffilterer) ; filtered
	 (generate-new-states states (cdr candidate-states) filters ffilterer passed))
	(t (generate-new-states states (cdr candidate-states) filters ffilterer
				(append passed (list (car candidate-states)))))))

;; must visit groups
;; return what? if result is nil, nil. otherwise, trivial, no meaning result for now.
;; fprocess return a function which have 3 arguments(state c-state states)
(defun justify-state (states c-state filters ffilterer &optional result)
  (cond ((null filters) result)
	((null result) (justify-state states c-state (cdr filters) ffilterer
				      (funcall ffilterer c-state (car filters) states)))
	(t (justify-state states c-state (cdr filters) ffilterer
			  (cons (funcall ffilterer c-state (car filters) states) result)))))

;; specific filterer
;; case: normal or using filter structure
;; normal:
;;   filter: '(1 2 3 4.. )
;; filter structure
;;   filter: '(type fcompare fupdate states)
;; (defun fmake-filterer (&key (fget-states #'identity) (fcompare #'eq) (fupdate #'adjoin))
;;   (lambda (state c-state filter)
;;     (let ((old-states (funcall fget-states filter))
;; 	  (updated-states (funcall fupdate state (funcall fget-states filter)))
;; 	  (r nil)) ; r need for removeing c-state. That time, r is non-nil.
;;       (dolist (old old-states (values r updated-states))
;; 		   (setf r (or r (funcall fcompare old c-state)))))))

;; how to distinguish finishing loop and null case?
;; %updater: iterate filters
;; (defun updater (state filters fupdate)
;;   (labels ((%updater (state filters fupdate &optional updated)
;; 	     (if (null filters)
;; 		 updated
;; 		 (%updater state (cdr filters) fupdate
;; 			   (append updated (list (funcall fupdate state (car filters))))))))
;;     (if (null filters)        
;; 	(list (funcall fupdate state))
;; 	(%updater state filters fupdate))))

(defun %update-each (s f)
  (mapcar (lambda (each)
	    (let ((type (filter-type f))
		  (fcompare (filter-fcompare f))
		  (fupdate (filter-fupdate f)))
	      (declare (ignore type))
	      (if (funcall fcompare s each)
		  (funcall fupdate f)
		  nil)))
	  (filter-states f)))

(defun updater (state filters fupdate &optional updated-filters)
  (if (null filters)
      updated-filters
      (updater state (cdr filters) fupdate
	       (append updated-filters (list (funcall fupdate state (car filters)))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;; application

(defun prepend (x y)
  (append y x))

;; state: '(1 2 3 4 5 ..)
;; breath-first-search of tree
(defun breath-first-search (states goalp)
  (srl states goalp #'prepend result))

