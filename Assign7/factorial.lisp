;;factorial prog without recurssion 

(setf f 1) 
(princ "Enter number :")
(setf num (read))

(if (< num 0)
    (exit))
    
 (loop for i from 1 to num 
     do (setf f (* f i)))
(princ f)
