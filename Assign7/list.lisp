(defparameter list '(A B C D E F G))
(princ " LIST CONTENTS : A   B   C   D   E   F   G ")
(terpri)
(princ "Enter value of n :")
(setq num (read))

(if (<= num 0)
    (exit))

(format t "~a" (nth (- num 1) list))