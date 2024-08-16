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

#2nd approach
class Solution(object):
    def lemonadeChange(self, bills):
        if bills[0] != 5:
            return False
        
        five_dollers = 0
        ten_dollers = 0

        for x in bills:
            if x == 5:
                five_dollers += 1
            elif x == 10:
                if five_dollers > 0:
                    five_dollers -= 1
                else:
                    return False
                ten_dollers += 1
            else:
                if five_dollers > 0 and ten_dollers > 0:
                    five_dollers -= 1
                    ten_dollers -= 1
                elif five_dollers > 2 :
                    five_dollers -= 3
                else:
                    return False
            print(five_dollers, ten_dollers)
        return True

                        
                


                    
