def intToRoman(num):
    res = ""
    res += 'M'*(num//1000)
    num %= 1000
    res += 'D'*(num//500)
    num %= 500
    res += 'C'*(num//100)
    num %= 100
    res += 'L'*(num//50)
    num %= 50
    res += 'X'*(num//10)
    num %= 10
    res += 'V'*(num//5)
    num %= 5
    res += 'I'*num
    res = res.replace('MCCCC','CM')
    res = res.replace('DCCCC','CD')
    res = res.replace('CXXXX','XC')
    res = res.replace('LXXXX','XL')
    res = res.replace('XIIII','IX')
    res = res.replace('VIIII','IV')
    return res

print(intToRoman(1999))
