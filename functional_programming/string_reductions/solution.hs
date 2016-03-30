import Data.Set

removeDuplicates s = aux (fromList s) s
  where aux set []     = []
        aux set (x:xs)
          | member x set = x : aux (delete x set) xs
          | otherwise    = aux set xs
        
main = do
  s <- getLine
  putStrLn $ removeDuplicates s
