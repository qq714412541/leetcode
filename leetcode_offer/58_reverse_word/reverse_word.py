class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        print(s)
        ind = 0

        s.reverse()
        print(s)
        s = ' '.join(s)
        print(s)
        return s

###split will delete '' default. [::-1] can reverse





su = Solution()
su.reverseWords('   hello      world!')