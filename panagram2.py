s1,s2=map(str,input().split())
print(sorted(list(s1)))
print(sorted(list(s2)))
if len(s1)== len(s2):
    if sorted(list(s1))==sorted(list(s2)):
        print("true")
    else:
        print("false")
else:
        print("false")    
                 
