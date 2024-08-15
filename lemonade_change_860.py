class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
       
        change = [5]
        if bills[0] != 5:
            return False
        else:
            for i in range(1,len(bills)):
                if bills[i] == 5:
                    change.append(5)
                elif bills[i] == 10:
                    if 5 not in change:
                        return False
                    change.remove(5)
                    change.append(10)
                elif bills[i] == 20:
                    if (5 not in change) or ((change.count(5) < 3 and 10 not in change)):
                        return False
                    elif 10 not in change:
                        change.remove(5)
                        change.remove(5)
                        change.remove(5)
                    else:
                        change.remove(5)
                        change.remove(10)
                    
        return True



                        
                


                    
