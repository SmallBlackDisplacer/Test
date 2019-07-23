module Intro where
import Data.Char

{- length of three-dimentional vector -}
lenVec3 x y z =  sqrt (x ^ 2 + y ^ 2 + z ^ 2)

{- returns 1 for positive, -1 for negative and 0 for 0 -}
sign x = if x > 0 then 1 else if x < 0 then (-1) else 0

{- operator that calculates the module of difference -}
x |-| y = if x - y > 0 then x - y else (x - y) * (-1)

{- partial application of the function -}
discount :: Double -> Double -> Double -> Double
discount limit proc sum = if sum >= limit then sum * (100 - proc) / 100 else sum

standardDiscount :: Double -> Double
standardDiscount = discount 1000 5

{- one number from two with Data.Char -}
twoDigits2Int :: Char -> Char -> Int
twoDigits2Int x y = if isDigit x && isDigit y then digitToInt x * 10 + digitToInt y else 100

{- distance between two points -}
dist :: (Double, Double) -> (Double, Double) -> Double
dist p1 p2 = sqrt ((fst p1 - fst p2) ^ 2 + (snd p1 - snd p2) ^ 2) 

{- double factorial recursion -}
doubleFact :: Integer -> Integer
doubleFact 1 = 1
doubleFact 2 = 2
doubleFact n = n * doubleFact (n - 2)

{- fibonacci with negative numbers -}
fibonacci :: Integer -> Integer
fibonacci n | n == 0 = 0
        | n == 1 = 1
        | n > 1 = fibonacci (n - 1) + fibonacci (n - 2)
        | otherwise = fibonacci (n + 2) - fibonacci (n +1)

{- fibonacci with negative numbers for O(n) -}
fibonacciFast :: Integer -> Integer
fibonacciFast n = fibonacciSmall 0 1 n

fibonacciSmall x y 0 = 0
fibonacciSmall x y 1 = 1
fibonacciSmall x y z | z == 2 = x+y
		| z > 2 = fibonacciSmall y (x+y) (z-1)
		| otherwise = if z < (-1) then fibonacciSmall (y-x) x (z+1) else y-x

{- element of sequince a0 = 1, a1 = 2, a2 = 3, 
a(k+3)=a(k+2)+a(k+1)−2ak -}
seqA :: Integer -> Integer
seqA n = let
		helper x y z 0 = 1
		helper x y z 1 = 2
		helper x y z 2 = z
		helper x y z n = helper y z (z + y - 2 * x) (n-1)
		in helper 1 2 3 n

{- number of digits in number and they amount -}
sum'n'count :: Integer -> (Integer, Integer)
sum'n'count x 
		| x == 0 = (0, 1)
		| otherwise = helper 0 0 x
		where 
			helper s c 0 = (abs s, c)
			helper s c x = helper (s + rem x 10) (c + 1) (quot x 10)

{- the value of a definite integral of a given function f 
on a given interval [a, b] by the method of trapeziums-}
integration :: (Double -> Double) -> Double -> Double -> Double
integration f a b | a == b = 0
		| a > b = integration f b a * (-1)
		| otherwise = h * (((f a) + (f b)) / 2 + sumF a b 0) where
    		h = (b - a) / 100000
    		sumF a b s 
      			| a >= b = s
      			| otherwise = sumF (a + h) (b) (s + f a)
