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

