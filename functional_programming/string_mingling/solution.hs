import Data.List

mingle :: [Char] -> [Char] -> [Char]
mingle (x:xs) (y:ys) = x:y:(mingle xs ys)
mingle _ _ = []
       

main :: IO()
main = do
    line1 <- getLine
    line2 <- getLine
    putStrLn $ mingle line1 line2
