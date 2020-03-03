def longestsubstrsequene(word_a,word_b):       #dynamic planning
    cell = [[0]*len(word_b) for x in range(len(word_a))]
    temp = 0
    if word_a[0] == word_b[0]:
        cell[0][0] = 1
    else:
        cell[0][0] = 0
    for i in range(1,len(word_a)):
        cell[i][0] = cell[i - 1][0]
    for j in range(1,len(word_b)):
        #print(j)
        cell[0][j] = cell[0][j - 1]

    for i in range(1,len(word_a)):
        for j in range(1,len(word_b)):
            if word_a[i] == word_b[j]:
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                cell[i][j] = max(cell[i-1][j],cell[i][j-1])
            temp = cell[i][j]
            print(cell)
            print('###')

    return temp

print(longestsubstrsequene('fosh','fish'))

#tip:
#1 divide to conquer, the edge should be dealed alone, then we can do recursion with the edge.
#2 from graph to code
#3 find the law between up and down
#4 in python, to implement a list, we'd better use double range
# i j means   [[0]*len(j) for x in range(len(i))]