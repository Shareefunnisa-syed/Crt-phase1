def printing(n):
    if n<1:
        return 1
    else:
         printing(n-1)
         print(n)
n=20
printing(n)
  
