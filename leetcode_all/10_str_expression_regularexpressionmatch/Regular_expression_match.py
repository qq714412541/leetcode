class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == '' and p == '':
            return True
        elif s == '' or p == '':
            print('#####')
            return False
        else:
            while s and p:
                if len(s) >= 2 and len(p) >= 2:
                    if p[0:2] == '.*':
                        s, p = self.delete_point_star(s, p)
                    elif s[0] == p[0] and s[0] == s[1] and p[1] == '*':
                        s, p = self.delete_str_star(s, p)
                    elif p[0] == '.':
                        s, p = self.delete_point(s, p)
                    elif s[0] == p[0]:
                        s, p = self.delete_str(s, p)
                    else:
                        print('####')
                        return False
                elif len(s) >= 1 and len(p) >= 1:
                    if p[0] == '.':
                        s, p = self.delete_point(s, p)
                    elif s[0] == p[0]:
                        s, p = self.delete_str(s, p)
                    else:
                        print(s, p)
                        print('##')
                        return False
                elif s == '' and p == '':
                    return True
                else:
                    print('###')
                    return False
            if s == '' and p == '':
                return True
            else:
                return False

    def delete_point(self, s, p):
        return s[1:], p[1:]

    def delete_str_star(self, s, p):
        print('#')
        i = 1
        while i < len(s) - 1 and s[i] == s[0]:
            i += 1
        print(i)
        # print(s[2:]=='')
        return s[i:], p[i:]

    def delete_point_star(self, s, p):
        i = 1
        while i < len(s) - 1 and s[i] == s[0]:
            i += 1
        return s[i:], p[i:]

    def delete_str(self, s, p):
        return s[1:], p[1:]





