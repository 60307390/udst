def CommsDecoder(s):
    i = 0
    res = ""
    while i < len(s):
        n = int(s[i+1])
        if n % 2 == 0:
            res += s[i]*(n-1)
        else:
            res += s[i]*(n+1)
        i += 2
    return res


message = input("Enter the encoded message to be sent into space: ")

decoded_message = CommsDecoder(message)

print(decoded_message)