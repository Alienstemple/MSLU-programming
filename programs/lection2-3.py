
# 9 Palindrome number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # краевой случай
        if x < 0:
            return False
        
        # ищем перевернутое число
        # разбить на разряды, записать в обратном порядке

        rev = 0
        n = x
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        
        return rev == x

# 509 Fibonacci Number

class Solution:
    def fib(self, n: int) -> int:
        a, b = 0 , 1
       
        for _ in range(n):
            a, b = b, a+b
        return a

# 344 Reverse String

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            # s[left], s[right] = s[right], s[left]
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1