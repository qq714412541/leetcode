
def longestsubstr(word_a,word_b):
    cell = dict
    temp = 0
    for i in range(len(word_a)):
        for j in range(len(word_b)):

            if word_a[i] == word_b[j]:
                cell[i][j] = cell[i-1][j-1] + 1
                if cell[i][j] > temp:
                    temp = cell[i][j]
            else:
                cell[i][j] = 0

    return temp


print(longestsubstr('abshcuggsmc','jgbvjsauasvas'))