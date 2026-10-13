'''Write a program to find Factorial of a Given Number?
'''

# a=int(input())
# if a<0:
#     print("Invalid InPut")
# else:
#     sum=1
#     for i in range(1,a+1):
#         sum=sum*i
#     print(sum)


'''Write a program to find sum of Factorials upto N Numbers like 0! + 1! + 2! + 3! + 4! + 5! +....upto n!?'''

# a=int(input())
# if a<0:
#     print("INvalid INput")
# else:
#     s=1
#     l=0
#     d=1
#     for i in range(1,a+1):
#         s=s*i
#         d=d+s
#         l=l+1
#         if l==1:
#             print("1+",end="")
#         if l>1:
#             print(end="+")
#         print(s,end="")
#     if a==0:
#         print(f"1={d}")
#     else:
#         print(f"={d}")

'''Write a program to print First N terms of Alternative Fibonacci Series?'''
# a=int(input())
# if a==0:
#     print("Invalid Input")
# else:
#     if a<0:
#         a=abs(a)
#     x=0
#     y=1
#     c=0
#     p=0
#     for i in range(1,(a*2)+1):
#         c=c+1
#         if c%2==1:
#             p=p+1
#             if p>1:
#                 print(end=",")
#             print("",x,end="")
#         z=x+y
#         x=y
#         y=z

'''Write a program to print the Average of the Alternative Fibonacci Series in the Given Range?'''

# a=int(input())
# b=int(input())
# if a<0 or b<0:
#     print("Invalid Inputs")
# else:
#     if a>b:
#         a,b=b,a
#     x=0
#     y=1
#     c=0
#     sum=0
#     l=0
#     while(x<=b):
#         if (x>=a):
#             c=c+1
#             if c%2==1:
#                 l=l+1
#                 sum=sum+x
#         z=x+y
#         x=y
#         y=z
#     if c==0:
#         print("No Fibonacci Series Values")
#     else:
#         print(f"{sum/l:.2f}")

'''Write a program to print Fibonacci Series in the Given Range.'''

# a=int(input())
# b=int(input())
# if a<0 or b<0:
#     print("Invalid Inputs")
# else:
#     if a>b:
#         a,b=b,a
#     x=0
#     y=1
#     p=0
#     while(x<=b):
#         if (x>=a):
#             p=p+1
#             print(x,end=" ")
#         z=x+y
#         x=y
#         y=z
#     if p==0:
#         print("No Fibonacci Series Values")

'''Write a program to print First N terms in the Fibonacci Series?'''

# a=int(input())
# if a==0:
#     print("Invalid Input")
# else:
#     if a<0:
#         a=abs(a)
#     x=0
#     y=1
#     for i in range(1,a+1):
#         print(x,end=" ")
#         z=x+y
#         x=y
#         y=z
        
'''Write a program to print the Sum of the Fibonacci Series of first N terms.'''

# a=int(input())
# if a<=0:
#     print("Invalid Input")
# else:
#     x=0
#     y=1
#     sum=0
#     for i in range(1,a+1):
#         sum=sum+x
#         z=x+y
#         x=y
#         y=z
#     print(sum)

'''Write a program to print the Average of the Fibonacci Series in Between the Given Range?'''

# a=int(input())
# b=int(input())
# if a<0 or b<0:
#     print("Invalid Inputs")
# else:
#     if a>b:
#         a,b=b,a
#     x=0
#     y=1
#     p=0
#     sum=0
#     while(x<=b):
#         if x>=a:
#             sum=sum+x
#             p=p+1
#         z=x+y
#         x=y
#         y=z
#     if p==0:
#         print("No Fibonacci Series Values")
#     else:
#         print(f"{sum/p:.2f}")

'''Write a Program to Find the result of the following expression -  
n
2
 + ........... 16 + 9 + 4 + 1=?  
'''

# a=int(input())
# if a==0:
#     print("Invalid Input")
# else:
#     if a<0:
#         a=abs(a)
#     l=0
#     sum=0
#     for i in range(a,0,-1):
#         l=l+1
#         if l>1:
#             print(end=" + ")
#         print(i*i,end="")
#         sum=sum+(i*i)
#     print(" =",sum)

'''Write a Program to Print the numbers in the following format  -   
n
3
,...........64,27,8,1. '''  

# a=int(input())
# if a==0:
#     print("Invalid Input.")
# else:
#     if a<0:
#         a=abs(a)
#     l=0
#     for i in range(a,0,-1):
#         l=l+1
#         if l>1:
#             print(end=",")
#         print("",i**3,end="")
#     print(".")

'''Write a program to check whether given number is even or odd. (Without dividing by 2)'''

# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     if ((n//2)*2==n):
#         print("Even")
#     else:
#         print("Odd")

'''Write a program to check whether Given Number is Even or Odd. (Without  % , / , + )'''

# a=int(input())
# if a<=0:
#     print("InvaliD InpuT")
# else:
#     while(a>1):
#         a=a-2
#     if a==0:
#         print("Even")
#     else:
#         print("Odd")

'''Write a program to check whether given number is even or odd. (Without  % , / , + ,* )'''

# a=int(input())
# if a<=0:
#     print("Invalid Input")
# else:
#     while(a>0):
#         a=a-2
#     if a==0:
#         print("Even")
#     else:
#         print("Odd")

