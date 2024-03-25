class Solution:
    def toHex(self, num: int) -> str:
        conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 
                    4: '4', 5: '5', 6: '6', 7: '7', 
                    8: '8', 9: '9', 10: 'a', 11: 'b', 
                    12: 'c', 13: 'd', 14: 'e', 15: 'f'}
            
        def decToHexa(num):
            if num == 0:
                return ''
            elif num > 0:
                rem = num % 16
                return decToHexa(num//16) + conversion_table[rem]
            else:
                num = num & 0xffffffff
                rem = num % 16
                return decToHexa(num//16) +  conversion_table[rem]
        if num == 0:
            return "0"
        return decToHexa(num)
            