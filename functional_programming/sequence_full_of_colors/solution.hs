fullOfColors :: String -> String
fullOfColors s = aux s 0 0 0 0 -- R G B Y
  where aux [] r g b y
          | r == g && b == y = "True"
          | otherwise        = "False"
        aux (x:xs) r g b y
          | x == 'R' && (r+1) - g <= 1 && (r+1) - g >= -1 = aux xs (r+1) g b y
          | x == 'G' && (g+1) - r <= 1 && (g+1) - r >= -1 = aux xs r (g+1) b y
          | x == 'B' && (b+1) - y <= 1 && (b+1) - y >= -1 = aux xs r g (b+1) y
          | x == 'Y' && (y+1) - b <= 1 && (y+1) - b >= -1 = aux xs r g b (y+1)
          | otherwise                                     = "False"

solve 0 = return ()
solve t = do
  s <- getLine
  putStrLn $ fullOfColors s
  solve (t-1)

main = do
  t <- readLn :: IO Int
  solve t
