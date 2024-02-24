#To find given string is panagram or not
import string
s=input()
s1="a"
s=s.lower()
s1=string.ascii_lowercase
if set(s)==set(s1):
   print("panagram")
else:
   print("not a panagram")
