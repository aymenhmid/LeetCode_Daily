from fractions import Fraction
import re
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def parse_expression(expression):
            # Use regex to find all matches of fractions with optional signs
            matches = re.findall(r'([+-]?)(\d+/\d+)', expression)
            
            # Create the dictionary to store fractions and their cumulative signs
            fraction_dict = {}
            
            for sign, fraction in matches:
                # Determine the value based on the sign
                value = -1 if sign == '-' else 1
                
                # Update the dictionary, summing values if the fraction already exists
                if fraction in fraction_dict:
                    fraction_dict[fraction] += value
                else:
                    fraction_dict[fraction] = value
            
            return fraction_dict
        
        if len(expression) <= 4:
            return expression
        fraction_dict = parse_expression(expression)
        s = 0
        for c in fraction_dict.keys():
            s += fraction_dict[c] * Fraction(c)
        if len(str(s)) == 1:
            return str(s) + "/1"
        else:
            return str(s)
#2nd approach
from fractions import Fraction

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        result = Fraction(0, 1)
        i = 0
        n = len(expression)
        
        while i < n:
            # Determine the sign of the current fraction
            sign = 1
            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1
            
            # Extract the numerator
            j = i
            while j < n and expression[j].isdigit():
                j += 1
            numerator = sign * int(expression[i:j])
            
            # Move past the '/' character
            i = j + 1
            
            # Extract the denominator
            j = i
            while j < n and expression[j].isdigit():
                j += 1
            denominator = int(expression[i:j])
            
            # Update the result using the current fraction
            result += Fraction(numerator, denominator)
            
            # Move to the next part of the expression
            i = j
        
        # Return the result as a string in the form of "numerator/denominator"
        return str(result.numerator) + "/" + str(result.denominator)
#third approach
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numerator = 0
        denominator = 1
        
        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i + 1]
            numerator = numerator * den + num * denominator
            denominator *= den
        
        common_divisor = gcd(numerator, denominator)
        return f"{numerator // common_divisor}/{denominator // common_divisor}"


