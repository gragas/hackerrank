--Only fill up the blanks for the function named len
--Do not modify the structure of the template in any other way
len :: [a] -> Int
len lst = aux lst 0
  where aux [] n = n
        aux (x:xs) n = aux xs (n+1)