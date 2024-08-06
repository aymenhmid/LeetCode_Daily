
#problem link : https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description/
class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        unique_letters = list(set(word))
        
        # List of keys from 2 to 9
        keys = ['2', '3', '4', '5', '6', '7', '8', '9']
            
        # Initialize the dictionary with keys and empty lists as values
        mapping = {key: [] for key in keys}
        
        
        s = 0
        if len(unique_letters) < 9:
            for i in range (0,len(unique_letters)):
                s+= word.count(unique_letters[i])
            return s
        else:
            total = 0
            letter_counts = Counter(word)
    
            # Sort letters by decreasing order of occurrence
            sorted_letters = sorted(letter_counts.keys(), key=lambda x: (-letter_counts[x], x))
            
            # List of keys from 2 to 9
            keys = ['2', '3', '4', '5', '6', '7', '8', '9']
            
            # Initialize the dictionary with keys and empty lists as values
            mapping = {key: [] for key in keys}
            
            # Distribute the sorted letters to keys
            for i, letter in enumerate(sorted_letters):
                key = keys[i % len(keys)]
                mapping[key].append(letter)
            for value in mapping.values():
                for j in range(0,len(value)):
                    total += (value.index(value[j]) +1) * word.count(value[j])
            return total
            
