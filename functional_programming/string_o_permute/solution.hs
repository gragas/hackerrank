permute (a:b:xs) = b:a:(permute xs)
permute []       = []

readAndPermute 0 = return ()
readAndPermute t = do
  s <- getLine
  putStrLn $ permute s
  readAndPermute (t-1)

main = do
  t <- readLn :: IO Int
  readAndPermute t

