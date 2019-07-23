module Prog where
import Data.Function

{- sample of parametrically polymorphic function-}
getSecondFrom :: t2 -> t1 -> t -> t1
getSecondFrom x y z = y

{- multiplies the second elements of pairs with Data.Function
on :: (b -> b -> c) -> (a -> b) -> a -> a -> c
on op f x y = f x `op` f y -}
multSecond = (*) `on` (snd)

{- like on, but with function that takes three arguments -}
on3 :: (b -> b -> b -> c) -> (a -> b) -> a -> a -> a -> c
on3 op f x y z = op (f x) (f y) (f z)

{- selects the largest of the arguments and the number 42
then raises the result to the cube and 
calculates the logarithm of the base 2 of the received number-}
doItYourself = (logBase 2) . (^ 3) . (max 42)

{- class Printable with one method toString;
types Bool and () are instances of this class with following behavior -}
class Printable a where
    toString :: a -> [Char]
instance Printable Bool where
    toString True = "true"
    toString False = "false"
instance Printable () where
    toString () = "unit type"

{- Pairs are now instances of the class Printable -}
instance (Printable a, Printable b) => Printable (a, b) where
	toString a = "(" ++ toString (fst a) ++ "," ++ toString (snd a) ++ ")"