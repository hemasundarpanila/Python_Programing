'''Find the nth term value in the Harmonic progression series by taking input of 1st term(a), common difference(d) and nth term ?'''
a=int(input())
d=int(input())
n=int(input())
if n<=0:
    print("InvaliD InPut")
else:
    h=1/(a+((n-1)*d))
    print(f"{h:.2f}")

'''Write a Program to Print first 'n' Numbers by taking input of 
1
s
t
 term(a), common difference(d) and no of terms(n) in the Arithmetic progression series?'''

s=int(input())
d=int(input())
n=int(input())
if n<=0:
    print("Invalid Input.")
else:
    p=0
    for i in range(n):
        p=p+1
        if p>1:
            print(end=",")
        print("",s+i*d,end="")
    print(".")

'''Write a program to print the GCD of given two numbers?'''

# a=int(input())
# b=int(input())
# if a<=0 and b<=0:
#     print("Invalid Inputs")
# elif a<=0:
#     print("Invalid First Input")
# elif b<=0:
#     print("Invalid Second Input.")
# else:
#     l=min(a,b)
#     for i in range(l,0,-1):
#         if a%i==0 and b%i==0:
#             print(i)
#             break

'''Write a Program to Print sum of the first 'n' terms by taking input of 1st term(a), common difference(d) and No of terms(n) in the Harmonic progression series? 

'''

# a=int(input())
# d=int(input())
# n=int(input())
# if n<=0:
#     print("Invalid Input.")
# else:
#     sum=0
#     for i in range(n):
#         h=(1/(a+(i*d)))
#         sum=sum+h
#     print(f"{sum:.2f}")

'''Write a program to print the LCM of given three numbers.'''

a=int(input())
b=int(input())
c=int(input())
if (a<=0 and b<=0) or ((b<=0)and(c<=0))or ((a<=0)and(c<=0)):
    print("Sorry Invalid Inputs!")
elif b<=0:
    print("Invalid Second Input")
elif c<=0:
    print("InvaliD ThirD Input")
elif a<=0:
    print("InvalId First Input")
else:
    l=max(a,b,c)
    h=l
    while(True):
        if (l%a==0 and l%b==0 and l%c==0):
            print(l)
            break
        l=l+h

'''Find and Print the 
n
t
h
 term value in the Arithmetic progression series by taking input of 1st term(a), common difference(d) and 
n
t
h
 term ?'''

# s=int(input())
# d=int(input())
# n=int(input())
# if n<=0:
#     print("InValid Input.")
# else:
#     print(f"Last term value is : {s+(n-1)*d}.")

'''Find the nth term value in the geometric progression series by taking input of 1st term(a), common Ratio(r) and nth term ?'''

# a=int(input())
# r=int(input())
# n=int(input())
# if n<=0:
#     print("InValid Input.")
# else:
#     print(f"Last term value is : {(a*(r**(n-1)))}.")

# Write '''a Program to Print first 'n' Numbers by taking input of 1st term(a), common Ratio(r) and No of terms(n) in the geometric progression series ?'''

# a=int(input())
# r=int(input())
# n=int(input())
# if n<=0:
#     print("Invalid Input.")
# else:
#     c=0
#     for i in range(n):
#         c=c+1
#         if c>1:
#             print(end=",")
#         print("",a*(r**i),end="")
#     print(".")

'''Write a Program to Print sum of the first 'n' terms by taking input of 1st term(a), common ratio(r) and No of terms(n) in the Geometric progression series? '''

# a=int(input())
# r=int(input())
# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     sum=0
#     for i in range(n):
#         h=(a*(r**i))
#         sum=sum+h
#     print(sum)

'''Write a Program to Print sum of the first 'n' terms by taking input of 1st term(a), common difference(d) and No of terms(n) in the Arithmetic progression series? '''

# a=int(input())
# d=int(input())
# n=int(input())
# if n<=0:
#     print("Invalid input.")
# else:
#     sum=l=0
#     for i in range(n):
#         h=(a+(i*d))
#         l=l+1
#         if l>1:
#             print(end="+")
#         print("",h,end=" ")
#         sum=sum+h
#     print("=",sum,end=".")
        

'''Write a Program to Print first 'n' Numbers by taking input of 1st term(a), common difference(d) and no of terms(n) in the Harmonic progression series?'''

# a=int(input())
# d=int(input())
# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     p=0
#     for i in range(n):
#         p=p+1
#         if p>1:
#             print(end=",")
#         h=(1/(a+(i*d)))
#         print(f" {h:.2f}",end="")

'''Write a program to print the GCD of given three numbers?
'''

# a=int(input())
# b=int(input())
# c=int(input())
# if ((a<=0 and b<=0) or (b<=0 and c<=0) or (c<=0 and a<=0)):
#     print("Invalid Inputs")
# elif a<=0:
#     print("Invalid First Input")
# elif b<=0:
#     print("Invalid Second Input")
# elif c<=0:
#     print("Invalid Third Input")
# else:
#     l=min(a,b,c)
#     for i in range(l,0,-1):
#         if (a%i==0 and b%i==0 and c%i==0):
#             print(i)
#             break

'''Write a program to print the LCM of given two numbers'''

# a=int(input())
# b=int(input())
# if a<=0 and b<=0:
#     print("Invalid Inputs.")
# elif a<=0:
#     print("Invalid First Input")
# elif b<=0:
#     print("InValid Second Input")
# else:
#     l=max(a,b)
#     h=l
#     while(True):
#         if (l%a==0 and l%b==0):
#             print(l)
#             break
#         l=l+h