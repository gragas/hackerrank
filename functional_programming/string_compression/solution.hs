import Data.Char

compress "" = ""
compress s = aux s 'z' 0
  where aux [] c n
          | n == 1 = []
          | n < 10 = [intToDigit n]
          | n > 9  = show n
        aux (x:xs) c n
          | n == 0           = x : aux xs x 1
          | c == x           = aux xs x (n+1)
          | c /= x && n == 1 = x : aux xs x 1
          | c /= x && n < 10 = intToDigit n : x : aux xs x 1
          | c /= x && n > 9  = show n ++ (x : aux xs x 1)

main = do
  s <- getLine
  putStrLn $ compress s
