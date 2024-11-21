'''
1071. Greatest Common Divisor of Strings

Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

'''

import math
def gcdOfStrings(str1, str2):
    n1=len(str1)
    n2=len(str2)
    if (str1+str2) != (str2+str1):
        return ""
    else:
        return str1[0:math.gcd(n1,n2)]
    
    
print(gcdOfStrings("LEET","CODE"))
print(gcdOfStrings("ABCABC","ABC"))
print(gcdOfStrings("ABABAB","ABAB"))