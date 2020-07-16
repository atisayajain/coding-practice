t = input()
ad = list(map(int, t.split()))
#print(ad)
t = input()
ed = list(map(int, t.split()))
#print(ed)

if (ad[2] > ed [2]):
    print(10000)
elif (ad[2] == ed[2] and ad[1] > ed[1]):
    print((ad[1] - ed [1]) * 500)
elif (ad[2] == ed[2] and ad[1] == ed[1] and ad[0] > ed[0]):
    print((ad[0] - ed [0]) * 15)
else:
    print(0)
