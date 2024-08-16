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
#2nd_solution
class Solution(object):
    def maxDistance(self, arrays):
        smallest = arrays[0][0]
        biggest = arrays[0][-1]
        max_distance = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1] - smallest), abs(biggest - arr[0]))
            smallest = min(smallest, arr[0])
            biggest = max(biggest, arr[-1])

        return max_distance
