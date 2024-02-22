def intToRoman(num: int) -> str:
    res = ""
    res += 'M'*(num//1000)
    thousands = num%10000//1000
    hundreths = num%1000//100
    tens = num%100//10
    ones = num%10

    syms = ['I','V','X','L','C','D','M']
    syms = syms[:-1]

    while num != 0:
        for i in range(len(syms)):
            if i%2:
                if num%5*(10**((6-i)//2))==0:
                #if (num%5 == 0) or (num%50 == 0) or (num%500==0):
                    res += syms[i]
                    num = num//5*(10**((6-i)//2))
                    print(res, num)
            else:
                if num%10**((6-i)//2)==0:
                #if (num%1 == 0) or (num%10==0) or (num%100==0) or (num%1000==0):
                    print('here')
                    res += syms[i]
                    num = num//(10**((6-i)//2))
    return res

print(intToRoman(2))
