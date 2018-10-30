class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        max_int = 2147483647
        str = str.strip()
        if str == "":
            return 0
        
        rlt_num = 0
        first = str[0]
        is_negative = False
        if first == '-':
            str = str[1:]
            is_negative = True
        elif first == '+':
            str = str[1:]
        elif (first <'0' and first >'9'):
            return 0
        
        
        zero = ord('0')
        for c in str:
            if c >= '0' and c<= '9':
                rlt_num = rlt_num*10 + ord(c) - zero
            else:
                break
        
        if is_negative:
            return (-max_int -1) if rlt_num > max_int else -rlt_num
        else:
            return (max_int) if rlt_num >= max_int else rlt_num
    
    
c = Solution()
print(c.myAtoi("2147483648"))