#https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

t = int(input())

while (t > 0):
    n, s = map(int, input().split())
    
    A = list(map(int,input().split()))
    
    #print(n, s, A)
    
    i = 0
    j = 0
    f = 0
    cursum = 0
    
    for j in range(n):
        #print('pre: ', cursum, A[j], i+1, j+1)
        if (cursum == s):
            j -= 1
            f = 1
            #print('post: ', cursum)
            break
        elif (cursum > s):
            cursum -= A[i]
            i += 1
            if (cursum == s):
                j -= 1
                f = 1
                #print('post: ', cursum)
                break
        cursum += A[j]
        if (cursum == s):
            f = 1
            #print('post: ', cursum)
            break
        elif (cursum > s):
            cursum -= A[i]
            i += 1
            if (cursum == s):
                f = 1
                #print('post: ', cursum)
                break
        #print('post: ', cursum)
    
    if (cursum > s):
        for i in range(i, n):
            #print('pre: ', cursum, i, j)
            cursum -= A[i]
            if (cursum == s):
                i += 1
                f = 1
                #print('post: ', cursum)
                break
            #print('post: ', cursum)

    #if (sum == s):
        #break
    
    if (cursum == s):
        print(i + 1, j + 1)
    else:
        print(-1)
    
    
    t -= 1
