solve :: Double -> Double
solve x = aux 0 1 1 x 0
  where aux acc xacc divacc x 9 = acc + xacc * x / (divacc * 9)
        aux acc xacc divacc x 0  = aux 1 1 1 x 1
        aux acc xacc divacc x n  = aux (acc + xacc * x / (divacc * n)) (xacc * x) (divacc * n) x (n+1)

main :: IO ()
main = getContents >>= mapM_ print. map solve. map (read::String->Double). tail. words
