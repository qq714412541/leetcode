def intToRoman(num:int):
    thousand = num//1000
    hundred = num%1000//100
    ten = num%100//10
    one = num%10


    thousand_str = thousand * 'M'

    if hundred ==9:
        hundred_str = 'CM'
    elif hundred ==4:
        hundred_str = 'CD'
    elif hundred<4:
        hundred_str = hundred * 'C'
    else:
        hundred_str = 'D' + 'C' *(hundred-5)

    if ten ==9:
        ten_str = 'XC'
    elif ten ==4:
        ten_str = 'XL'
    elif ten < 4:
        ten_str = ten*'X'
    else:
        ten_str = 'L' + 'X'*(ten-5)

    if one ==9:
        one_str = 'IX'
    elif one ==4:
        one_str = 'IV'
    elif one <4:
        one_str = one * 'I'
    else:
        one_str = 'V' + 'I' * (one-5)

    result = thousand_str + hundred_str + ten_str + one_str

    return result

x1 = 3
x2 = 4
x3 = 9
x4 =58
x5 = 1994
x6 = 1
y1 = intToRoman(x1)
y2 = intToRoman(x2)
y3 = intToRoman(x3)
y4 = intToRoman(x4)
y5 = intToRoman(x5)
y6 = intToRoman(x6)
print(y1,y2,y3,y4,y5,y6)
