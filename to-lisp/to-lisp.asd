;; Usual Lisp comments are allowed here

(defsystem "to-lisp"
  :description "to-lisp: a Lisp system."
  :version "0.0.1"
  :author "srolisp <srolisp@gmail.com>"
  ;; :licence "Public Domain"
  ;; :depends-on ("optima.ppcre" "command-line-arguments")
  :pathname "src"
  :serial t
  :components ((:file "package")
               (:file "to-lisp")))



