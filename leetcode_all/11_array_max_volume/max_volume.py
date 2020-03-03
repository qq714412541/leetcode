def maxArea(height):
    leng = len(height)

    max_volume = 0
    for i in range(leng-1):
        for j in range(i+1,leng):
            print(i,j)
            width = j-i
            h = min(height[i],height[j])
            volume = width *h
            print(width,h)
            if volume >max_volume:
                max_volume = volume

    return max_volume


def maxArea2(height):
    leng = len(height)
    left = 0
    right = leng-1
    max_volume = (leng-1)*min(height[left],height[right])
    print(leng,left,right,max_volume)
    for i in range(leng):

        while left<right:
            if i%2==0:
                left+=1


            else:
                right+=1

            w = right - left
            h = min(height[right], height[left])
            volume = w * h

            if volume > max_volume:
                max_volume = volume

    return max_volume





def maxArea3(height):
    leng = len(height)
    left = 0
    right = leng-1
    max_volume = (leng-1)*min(height[left],height[right])

    while left < right:


        if height[left] > height[right]:
            right -=1
        else:
            left+=1
        volume = (right - left) * min(height[left], height[right])
        if volume > max_volume:
            max_volume = volume

    return max_volume

result = maxArea3([2,3,4,5,18,17,6])
print(result)