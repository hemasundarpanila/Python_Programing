'''Write a program to find the Sum of all Alternative Prime Numbers between The Given Values.'''

# a=int(input())
# b=int(input())
# if a<=0 or b<=0:
#     print("Invalid Inputs")
# else:
#     if a>b:
#         a,b=b,a
#     d=0
#     sum=0
#     for i in range(a+1,b):
#         c=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 c=c+1
#         if c==2:
#             d=d+1
#             if d%2==1:
#                 sum=sum+i
                
#     if d==0:
#         print("No Prime Numbers")
#     else:
#         print(sum)
        
        
'''Write a program to print all factors of the Given Number.'''

# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=" ")

'''Write a program to print all Prime Factors of a Given Number?'''

# n=int(input()) 
# if n==0:
#     print("Invalid Input")
# else:
#     h=0
#     n=abs(n)
#     for i in range(1,n+1):
#         if n%i==0:
#             c=0
#             for j in range(1,i+1):
#                 if i%j==0:
#                     c=c+1
#             if c==2:
#                 h=h+1
#                 print(i,end=" ")
#     if h==0:
#         print("No Prime Factors")

'''Write a Program to print the first 50 prime Numbers without using Factors count?'''

# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     k=n
#     p=2
#     d=0
#     v=0
#     while(True):
#         b=True
#         for i in range(2,p):
#             if p%i==0:
#                 b=False
#                 break
#         if (b==True and n>1):
#             v=v+1
#             if(v>1):
#                 print(",",end=" ")
#             print(p,end="")
#             d=d+1
#             if d==n:
#                 break
#         p=p+1

'''Write a program to print Alternative Prime Numbers in the Given Range.'''

# a=int(input())
# b=int(input())
# if a<=0 or b<=0:
#     print("Invalid Inputs")
# else:
#     k=0
#     h=0
#     for i in range(a,b+1):
#         c=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 c=c+1
#         if c==2:
#             k=k+1
#             if k%2==1:
#                 h=h+1
#                 if h>1:
#                     print(end=", ")
#                 print(i,end="")
            
'''Write a program to find Sum of all the prime numbers between the Given values.'''

# n=int(input())
# n2=int(input())
# if n<=0 or n2<=0:
#     print("Invalid Inputs")
# else:
#     s=0
#     for i in range(n+1,n2):
#         c=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 c=c+1
#         if c==2:
#             s=s+i
#     print(s)

'''Write a program to check if the given number is a prime number or not.'''

# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     c=0
#     for i in range(1,n+1):
#         if n%i==0:
#             c=c+1
#     if c==2:
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")
            
'''Write a program to print All the Prime Numbers in the Given Range.'''

# n=int(input())
# n2=int(input())
# if n<=0 or n2<=0:
#     print("Invalid Inputs")
# else:
#     k=0
#     for i in range(n,n2+1):
#         c=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 c=c+1
#         if c==2:
#             k=k+1
#             if k>1:
#                 print(end=", ")
#             print(i,end="")

'''Write a Program to Print the Given Number is Prime or not without using count?
                '''
# n=int(input())
# if n<=0:
#     print("Invalid Input")
# else:
#     b=True
#     for i in range(2,n):
#         if n%i==0:
#             b=False
#             break
#     if (b and n>1):
#         print("Prime Number")
#     else:
#         print("Not a Prime Number")
        
        