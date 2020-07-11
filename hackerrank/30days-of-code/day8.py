import sys

t = int(input())
phone = {}

while (t > 0):
    n, p = input().split() 
    phone[n] = p
    t -= 1

for line in sys.stdin:
    line = line.rstrip()
    if line in phone:
        print(str(line) + "=" + str(phone[line]))
    else:
        print("Not found")
