class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        lowest = [e[0] for e in arrays]
        highest = [e[len(e) -1 ] for e in arrays]
        lowest.sort()
        highest.sort()
        for e in arrays:
            
            if lowest[0] == e[0] and highest[-1] == e[-1]:
                if abs(highest[-2]-lowest[0]) > abs(highest[-1]-lowest[1]):
                    return abs(highest[-2]-lowest[0])
                else:
                    return abs(highest[-1]-lowest[1])
            elif lowest[0] != e[0] and highest[-1] !=  e[-1]:
                continue  
            else:
                return abs(highest[-1] - lowest[0])
