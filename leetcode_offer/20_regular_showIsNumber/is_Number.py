import  re
class Solution:
    def isNumber(self, s: str) -> bool:
        #((\+|-)?\d*(\.\d+)?)
        #((\+|-)?\d*(\.\d*)?)|((\+|-)?\d*(\.\d*)?(E|e)(\+|-)?\d+)
        #re.match('^(\+|-)?\d*(\.\d+)?([e](\+|-)?\d+$)?',s)
        #return re.match('^(\+|-)?\d*(\.\d+)?([e|E]-?\d+)?$',s)
        return  re.match('^ *(\+|-)?((\d+(\.\d*)?)|(\.\d+))([e|E](\+|-)?\d+)? *$',s)

su = Solution()
res = su.isNumber('3.')
print(res)