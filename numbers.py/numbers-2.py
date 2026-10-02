'''Write a Program to Print The Sum of the Even Digits in a Given Number?'''

# a=int(input())
# if a<=0:
#     print("Invalid Input")
# else:
#     c=0
#     while(a>0):
#         r=a%10
#         if r%2==0:
#             c=c+r
#         a=a//10
#     print(c)

'''Write a Program to Print Count no of Digits in a Given Number?'''

# a=int(input())
# if a==0:
#     print("InvaliD Input")
# else:
#     if a<0:
#         a=abs(a)
#         c=0
#         while(a>0):
#             k=a%10
#             c=c+1
#             a=a//10
#         if c==1:
#             print(f"Given Number consists of only {c} Digit and it is Negative Value.")
#         else:
#             print(f"Given Number consists of {c} Digits and it is Negative Value.")
#     else:
#         l=0
#         while(a>0):
#             s=a%10
#             l=l+1
#             a=a//10
#         if l==1:
#             print(f"Given Number consists of only {l} Digit.")
#         else:
#             print(f"Given Number consists of {l} Digits.")
                

'''Write a program to find Sum of first 'n' Natural Numbers by Using formula?'''

# n=int(input())
# if n==0:
#     print("InvaLid Input.")
# else:
#     if n<0:
#         print("Sorry! you have Entered Negative Values.")
#     else:
#         a=int(((n*(n+1))/2))
#         print(f"Sum of 'N' Natural Numbers is {a}.")
            
'''Write a Program to check if the Given Number is Perfect Square or Not a perfect Square?'''

# n=int(input())
# if n<=0:
#     print("InvaliD Input")
# else:
#     for i in range(1,n+1):
#         if i**2==n:
#             print("Given Number is a Perfect Square.")
#             break
#     else:
#         print("Given Number is Not a Perfect Square.")

'''Write a Program to Print The Sum of all odd Positions in a Given Number?'''

# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     c=0
#     s=0
#     while(n>0):
#         c=c+1
#         r=n%10
#         if c%2==1:
#             s=s+r
#         n=n//10
#     print(s)

'''Write a Program to print the Highest digit in a Given Number?'''

# n=int(input())
# if n<=0:
#     print("Invalid Input.")
# else:
#     h=0
#     while(n>0):
#         r=n%10
#         if r>h:
#             h=r
#         n=n//10
#     print(f"Highest Digit in a Given Number is {h}.")
        
'''Write a program to Find Sum of Digits of a Given Number?'''

# n=int(input())
# if n<=0:
#     print("Invalid Input",end="")
# else:
#     rev=0
#     while(n>0):
#         r=n%10
#         rev=rev*10+r
#         n=n//10
#     d=0
#     while(rev>0):
#         s=rev%10
#         d=d+1
#         if d>1:
#             print(end=" + ")
#         print(s,end="")
#         rev=rev//10
# print(".")

'''Write a program to find Sum of first 'n' Natural Numbers Without Using formula?
'''

# n=int(input())
# if n==0:
#     print("InvaLid Input",end="")
# else:
#     if n>0:
#         c=0
#         s=0
#         l=0
#         for i in range(1,n+1):
#             s=s+i
#             c=c+1
#             l=l+1
#             if c==1:
#                 print("Sum of 'N' Natural Numbers is",end="")
#             if c>1:
#                 print(end=" +")
#             print("",i,end="")
#         print(" =",s,end="")
#     else:
#         print("Sorry! you have Entered Negative Values",end="")
# print(".")
        

'''Write a Program to print the smallest digit in a Given Number?'''

# n=int(input())
# if n<=0:
#     print("Invalid Input.")
# else:
#     l=n
#     while(n>0):
#         r=n%10
#         if(r<l):
#             l=r
#         n=n//10
#     print(f"Smallest Digit in a Given Number is {l}.")    
            
    