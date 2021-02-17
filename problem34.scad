/*
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
*/

function digit(s) =
    s == "0" ? 0 :
    s == "1" ? 1 :
    s == "2" ? 2 :
    s == "3" ? 3 :
    s == "4" ? 4 :
    s == "5" ? 5 :
    s == "6" ? 6 :
    s == "7" ? 7 :
    s == "8" ? 8 :
    s == "9" ? 9 : undef;

function sum(v, i = 0, r = 0) = 
    i < len(v) ? sum(v, i + 1, r+v[i]) : r;
    
function factorial(n) = 
    n == 0 ? 1 : n*factorial(n-1);
    
function digits(n) = 
    [for(s=str(n)) digit(s)];
        
function is_curious(n) = 
    n == sum([for (i=digits(n)) factorial(i)]);
    
echo(
sum([for (i=[3:100000]) is_curious(i)? i: 0])
);