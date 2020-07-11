t = int(input())

while(t > 0):
    s = input()
    o = ''
    e = ''
    for i in range(len(s)):
        if (i % 2 != 0):
            o += s[i]
        elif (i % 2 == 0):
            e += s[i]
        #print(e, o)
    
    print(e + " " + o)

    t -= 1
