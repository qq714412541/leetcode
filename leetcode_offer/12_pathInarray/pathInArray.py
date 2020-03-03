class Solution:
    def exist(self, board, word: str) -> bool:
        global rec
        rec = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    p = board[i][j]
                    board[i][j]='#'
                    if self.re(board, [i, j], word[1:], word[0]):
                        return True
                    else:
                        board[i][j] = p
                        continue

        return False

    def re(self, arr, pos, resi, last):
        #print(arr,pos,last,resi)
        global rec
        if resi == '':
            return True
        #print(resi,pos)
        if (resi,pos[0],pos[1]) in rec:
            #print('???')
            return False
        x, y = pos[0], pos[1]
        z = arr[x][y]
        arr[x][y]='#'

        temp = self.go(arr, pos, resi[0])
        #print(temp)
        arr[x][y] = z
        if not temp:
            #print('###')
            return False
        else:

            for t in temp:
                z = arr[x][y]
                arr[x][y] = '#'
                if not self.re(arr, t, resi[1:], last + resi[0]):
                    rec.add((last + resi[0], t[0],t[1]))
                    arr[x][y] = z
                    continue

                else:
                    return True



    def go(self, arr, pos, tar):
        res = []
        x, y = pos[0], pos[1]
        if x < len(arr) - 1:
            if arr[x + 1][y] == tar:
                res.append([x + 1, y])
        if x > 0:
            if arr[x - 1][y] == tar:
                res.append([x - 1, y])
        if y < len(arr[0]) - 1:
            if arr[x][y + 1] == tar:
                res.append([x, y + 1])
        if y > 0:
            if arr[x][y - 1] == tar:
                res.append([x, y - 1])
        return res


su = Solution()
arr = [["C","A","A"],["A","A","A"],["B","C","D"]]
tar = "AACAAAA"
res = su.exist(arr,tar)
print(res)