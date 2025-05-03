#appraoch 1
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        D = {}

        for index, element in enumerate(tops):
            if element not in D:
                D[element] = {'tops': [], 'bottoms': []}
            D[element]['tops'].append(index)


        for index, element in enumerate(bottoms):
            if element not in D:
                D[element] = {'tops': [], 'bottoms': []}
            D[element]['bottoms'].append(index)
        for key,val in D.items():
            count = len(set(D[key]['tops'] + D[key]['bottoms']))
            print(count)
            if  count == len(tops):
                return min(len(tops) - len(D[key]['tops']),len(tops) - len(D[key]['bottoms']))
                
                
        return -1
