def check_fermat(a,b,c,n):
    if ((a>0 and b>0) and (c>0 and n>2)):
        p=a**n+b**n
        q=c**n
        if p==q:
            print("Holy smokes,Fermat was wrong!!")
        else:
            print("No, that doesn't work")
n=int(input("Enter the exponential nuumber:"))
a=int(input("Enter a positive nuumber:"))
b=int(input("Enter a positive nuumber:"))
c=int(input("Enter a positive nuumber:"))
check_fermat(a,b,c,n)
