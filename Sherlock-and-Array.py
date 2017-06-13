#!/bin/python3

import sys

def solve(a):
    i,j=0,len(a)-1
    sumx,sumy=0,0
    sumx,sumy=a[i]+sumx,a[j]+sumy
    while(i<=j):
        if(i==j and sumx==sumy):
            return 'YES'
        if(sumx==sumy):
            i=i+1
            j=j-1
            sumx=a[i]+sumx
            sumy=a[j]+sumy
        elif(sumx<sumy):
            i=i+1
            sumx=a[i]+sumx
        elif(sumx>sumy):
            j=j-1
            sumy=a[j]+sumy
       
    return 'NO'
            
        

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
#!/bin/python3

import sys

def solve(a):
    i,j=0,len(a)-1
    sumx,sumy=0,0
    sumx,sumy=a[i]+sumx,a[j]+sumy
    while(i<=j):
        if(i==j and sumx==sumy):
            return 'YES'
        if(sumx==sumy):
            i=i+1
            j=j-1
            sumx=a[i]+sumx
            sumy=a[j]+sumy
        elif(sumx<sumy):
            i=i+1
            sumx=a[i]+sumx
        elif(sumx>sumy):
            j=j-1
            sumy=a[j]+sumy
       
    return 'NO'
            
        

T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = solve(a)
    print(result)
