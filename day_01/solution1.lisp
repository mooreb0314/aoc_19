(defun get-file (filename)
    (with-open-file (stream filename)
        (loop for line = (read-line stream nil)
            while line
            collect (parse-integer line)
        )
    )
)

(defun get-fuel (mass)
    (- (FLOOR( / mass 3)) 2)
)

(print
    (apply '+ (loop 
        for mass in (get-file "/Users/aiuedg2/git/aoc_19/day_01/input.txt")
        collect (get-fuel mass)
    ))
)