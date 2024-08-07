# problem link : https://leetcode.com/problems/integer-to-english-words/description/
class Solution(object):
    
    @staticmethod
    def number_words_mapping(n):
        # Words for 0-19
        ones_and_teens = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]
        
        # Words for tens multiples (20, 30, ..., 90)
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        
        if 1 <= n < 20:
            return ones_and_teens[n]
        elif 20 <= n < 100:
            ten_part = n // 10
            one_part = n % 10
            return tens[ten_part] + ("" if one_part == 0 else " " + ones_and_teens[one_part])
        else:
            return "Number out of range"

    @staticmethod
    def get_hundreds(ch):
        # Access the static method number_words_mapping
        number_to_words_map = {i: Solution.number_words_mapping(i) for i in range(1, 100)}
        if ch == '000':
            return ""
        elif len(ch) == 1 and ch !='0':
            return number_to_words_map.get(int(ch), "")
        elif len(ch) == 2 and int(ch) < 100:
            return number_to_words_map.get(int(ch), "")
        elif len(ch) == 3 and ch != '000':
            x = int(ch)//100
            if x > 0:
                firstWord = number_to_words_map.get(x) + ' Hundred'
            else:
                firstWord = ""
   
            y = int(ch[1:])
            if y < 100:
                secondWord = number_to_words_map.get(y, "")
            else:
                secondWord = number_to_words_map.get(int(ch[1:]), "")

            finalWord = (firstWord + ' ' + secondWord).strip()
            return finalWord

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        words = []
        
        cleaned_str = str(num).lstrip('0')
        substrings = [cleaned_str[max(i-3, 0):i] for i in range(len(cleaned_str), 0, -3)]
        substrings.reverse()
        
        if len(substrings) == 1:
            return self.get_hundreds(substrings[0]).strip()
        elif len(substrings) == 2:
            firstWord = self.get_hundreds(substrings[0]) + ' Thousand'
            secondWord = self.get_hundreds(substrings[1])
            result = firstWord + ' ' + secondWord
            return result.strip()
        elif len(substrings) == 3:
            words = []
            firstWord = self.get_hundreds(substrings[0])
            if firstWord != "":
                firstWord = self.get_hundreds(substrings[0]) + ' Million'
            else:
                firstWord = ""
            
            words.append(firstWord)
            secondWord = self.get_hundreds(substrings[1])
            if secondWord != "":
                secondWord = self.get_hundreds(substrings[1]) + ' Thousand'
            else:
                secondWord = ""
            words.append(secondWord)
            thirdWord = self.get_hundreds(substrings[2])
            words.append(thirdWord)
            words = [s for s in words if s.strip()]
            return " ".join(words).strip()
        elif len(substrings) == 4:
            words = []
            firstWord = self.get_hundreds(substrings[0])
            if firstWord != "":
                firstWord = self.get_hundreds(substrings[0]) + ' Billion'
            else:
                firstWord = ""
            
            words.append(firstWord)
            secondWord = self.get_hundreds(substrings[1])
            if secondWord != "":
                secondWord = self.get_hundreds(substrings[1]) + ' Million'
            else:
                secondWord = ""
            
            words.append(secondWord)
            thirdWord = self.get_hundreds(substrings[2])
            if thirdWord != "":
                thirdWord = self.get_hundreds(substrings[2]) + ' Thousand'
            else:
                thirdWord = ""
            
            words.append(thirdWord)
            fourthWord = self.get_hundreds(substrings[3])
            if fourthWord != "":
                fourthWord = self.get_hundreds(substrings[3])
            else:
                fourthWord = ""
            words.append(fourthWord)
            words = [s for s in words if s.strip()]
            return " ".join(words).strip().replace('  ',' ')
