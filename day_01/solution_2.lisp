(defun get-file (filename)
    (with-open-file (stream filename)
        (loop for line = (read-line stream nil)
            while line
            collect (parse-integer line)
        )
    )
)

(defun get-fuel (mass)
    (cond 
        ((<= mass 0 ) 0)
        ((> mass 0)
            (+ mass (get-fuel (- (FLOOR( / mass 3)) 2)))
        )
    )
)

(print
    (apply '+ (loop 
        for mass in (get-file "input.txt")
        collect (- (get-fuel mass) mass)
    ))
)
