import random

 # -*- coding:utf-8 -*-

def quickSort(series,l,r):
    i = l
    j = r
    if i > j:
        return
    axis = series[i]
    while i < j:
        print(i,j,axis,'??')
        while i < j and series[j] >= axis:
            print('?')
            j -=1
        series[i] = series[j]

        print(series,i,j)
        while i < j and series[i] <= axis:
            i +=1
        series[j] = series[i]
        print(series,i,j,'#')

    series[i] = axis
    print(series,i,j,'###')
    quickSort(series,l,i-1)
    quickSort(series,i+1,r)


'''data = [5, 2, 8, 4, 7, 4, 3, 9, 2, 0,1,16]
quickSort(data,0,len(data)-1)
print(data)'''


arr = [2,1,2,1,1,0,0]
quickSort(arr,0,6)
print(arr)