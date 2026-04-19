class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x==0:
            return True
        else:
            original_value=x
            reversed_value=0
            while x>0:
                n=x%10
                reversed_value=(reversed_value*10)+n
                x=x//10
            return original_value==reversed_value
          