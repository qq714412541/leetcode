class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        return self.re(postorder)

    def re(self, arr):
        if not arr:
            return True
        else:
            tar = arr[-1]
            sign = 0
            itm = -1
            for i in range(len(arr[:-1])):
                if arr[i] > tar:
                    if sign == 0:
                        sign += 1
                        itm = i
                    else:
                        continue
                else:
                    if sign > 0:
                        return False
                    else:
                        continue
            if itm == -1:
                return self.re(arr[:-1]) and self.re([])
            l = arr[:itm]
            r = arr[itm:-1]
            return self.re(l) and self.re(r)

