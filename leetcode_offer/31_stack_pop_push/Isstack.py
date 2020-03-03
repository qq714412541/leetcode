class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        while popped:
            #print(pushed,popped,stack)
            x = popped[0]
            popped = popped[1:]
            if x in pushed:
                while pushed:
                    if pushed[0] == x:
                        pushed = pushed[1:]
                        break
                    else:
                        stack.append(pushed[0])
                        pushed=pushed[1:]
                if not pushed and not popped:
                    return True
            else:
                if not stack:
                    return False
                y = stack.pop()
                if y != x:
                    #print('??')
                    return False
                else:
                    continue
        return True

class Solution:#simplify the code
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        while stack or popped:
            #print(stack,popped,pushed)
            if stack:
                if not popped:
                    return True
                if stack[-1] ==popped[0]:
                    stack.pop()
                    popped=popped[1:]
                    continue
            if not pushed:
                return False
            stack.append(pushed[0])
            pushed = pushed[1:]
        return True


su = Solution()
a = []
b = [1]
res = su.validateStackSequences(a,b)
print(res)