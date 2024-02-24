def rev(n):
    if n<0:
        return 1
    else:
        d=n%10
        print(d)
        return d+10*rev(n//10)
n=int(input())
print(rev(n))
        
