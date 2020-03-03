class Solution:
    def spiralOrder(self, matrix):
        res = []
        startx = 0
        starty = 0
        endx = len(matrix) - 1
        endy = len(matrix[0]) - 1
        while startx <= endx or starty <= endy:
            #print(startx,starty,endx,endy)
            i = startx
            j = starty
            #print(i,j,'-')
            while j <= endy:
                res.append(matrix[i][j])
                j += 1
            startx += 1
            j = endy
            i = startx
            if startx>endx or starty>endy:
                break
            #print(startx, starty, endx, endy,'???')
            #print(i, j,'|')
            while i <= endx:
                res.append(matrix[i][j])
                i += 1
            endy -= 1
            i = endx
            j = endy
            if startx>endx or starty>endy:
                break
            #print(i, j,'__')
            while j >= starty:
                res.append(matrix[i][j])
                j -= 1
            endx -= 1
            j = starty
            i = endx
            if startx>endx or starty>endy:
                break
            #print(i, j,'||')
            while i >= startx:
                res.append(matrix[i][j])
                i-=1
            starty += 1

            #print(i, j)
            #print(startx,starty,endx,endy)
            if startx>endx or starty>endy:
                break
        return res
su  =Solution()
arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
res = su.spiralOrder(arr)
print(res)


