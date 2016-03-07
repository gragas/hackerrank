-- Enter your code here. Read input from STDIN. Print output to STDOUT
import Data.List

pascalTriangle 0 = "1\n"
pascalTriangle k = pascalTriangle (k-1) ++ intercalate " " (map show [pascal k c | c <- [0..k]]) ++ "\n"

pascal 0 0 = 1
pascal r c
    | c == 0 = 1
    | c == r = 1
    | otherwise = pascal (r - 1) (c - 1)  + pascal (r - 1) c

pascalTriangleOneIndex k = pascalTriangle (k - 1)

main = do
    input <- getLine
    putStr . pascalTriangleOneIndex . (read :: String -> Int) $ input