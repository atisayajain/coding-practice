# Enter your code here. Read input from STDIN. Print output to STDOUT
import random

def power(a, n, p):
    res = 1
    a = a % p
    #print(a)

    while (n > 0):
        if(n % 2 != 0):
            res = (res * a) % p
        a = (a * a) % p
        n = int(n/2)
        #print(a, n, p)
    #print(res)
    return res

def gcd(a, b):
    if (a < b):
        return gcd(b, a)
    elif (a % b == 0):
        return b
    else:
        return gcd(b, a%b)

def prime(n, k):
    #print('n = ' + str(n))
    if (n == 2 or n == 3):
        #print('1if')
        return 'Prime'
    elif (n <= 1 or n % 2 == 0):
        #print('2if')
        return 'Not prime'

    while (k > 0):
        #print('k = ' + str(k))
        a = random.randint(2, n-2)
        #print('a = ' + str(a))

        if (gcd(n, a) != 1):
            #print('gcd')
            return 'Not prime'

        if (power(a, n-1, n) != 1):
            #print('pow')
            return 'Not prime'
        
        k -= 1
        
    #print('last')
    return 'Prime'

T = int(input())

for i in range(T):
    n = int(input())
    print(prime(n, 3))
