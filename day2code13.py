s=input()
s1=s[0]  
for i in range (1,len(s)):
    if s[i-1]!=s[1]:
        s1+=s[i]
print(s1)        
 
