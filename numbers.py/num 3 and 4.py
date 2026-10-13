'''Write a program to swap the two given numbers.'''

# a=int(input())
# b=int(input())
# a,b=b,a
# print(a)
# print(b)

'''Write a program to find Average of all Palindrome Numbers in the Range?'''

# a=int(input())
# b=int(input())
# if a==0 or b==0:
#     print("INVALID Inputs")
# else:
#     if a<0 or b<0:
#         a=abs(a)
#         b=abs(b)
#     if a>b:
#         #a,b=b,a
#         print("Given Inputs are Swapped")
#     else:
#         c=0
#         sum=0
#         for i in range(a,b+1):
#             rev=0
#             t=i
#             while(i>0):
#                 r=i%10
#                 rev=rev*10+r
#                 i=i//10
#             if rev==t:
#                 sum=sum+rev
#                 c=c+1
#         if c==0:
#             print("No Palindrome Values")
#         else:
#             d=sum/c
#             print(f"{d:.2f}")
            
            
'''Write a program to find Sum of all Palindrome Numbers between the Given Numbers?'''

# a=int(input())
# b=int(input())
# if a==0 or b==0:
#     print("INVALID Inputs")
# else:
#     if a<0 or b<0:
#         b=abs(b)
#         a=abs(a)
#     if a>b:
#         a,b=b,a
#     c=0
#     sum=0
#     for i in range(a+1,b):
#         rev=0
#         t=i
#         while(t>0):
#             r=t%10
#             rev=rev*10+r
#             t=t//10
#         if rev==i:
#             c=c+1
#             sum+=rev
#     if(c==0):
#         print("No Palindrome Values")
#     else:
#         print(sum)

'''Write a program to the check if the Given Number is a Palindrome or not and if it is a palindrome then Print PALINDROME, else Print the Reverse Value of a Given Number ?

                
 '''               
# a=int(input())
# if a<0:
#     print("Invalid Input")
# else:
#     if a>0:
#         t=a
#         rev=0
#         while(a>0):
#             r=a%10
#             rev=rev*10+r
#             a=a//10
#         if rev==t:
#             print("Given Number is Palindrome")
#         else:
#             print(f"Reverse of a Given Number is {rev}")
#     else:
#         if a==0:
#             print("Zero")
        
            
'''Write a program to check Given Number is Palindrome or Not.'''

# a=int(input())
# if a<=0:
#     print("InvAlid Input")
# else:
#     t=a
#     rev=0
#     while(a>0):
#         r=a%10
#         rev=rev*10+r
#         a=a//10
#     if rev==t:
#         print("Palindrome")
#     else:
#         print("Not a Palindrome")

'''Write A Program to check the Given Number is Perfect Square or not?'''

# a=int(input())
# if a==0:
#     print("Invalid Input")
# else:
#     if a<0:
#         a=abs(a)
#     for i in range(1,a+1):
#         if i*i==a:
#             print("Given Number is Perfect Square.")
#             break
#     else:
#         print("Given Number is Not a Perfect Square.")

'''Write a program to print Alternative Palindrome Numbers in the Given Range?

'''

# a=int(input())
# b=int(input())
# if a<0 or b<0:
#     print("InvAlid InPUts")
# else:
#     p=0
#     s=0
#     for i in range(a,b+1):
#         t=i
#         rev=0
#         while(t>0):
#             r=t%10
#             rev=rev*10+r
#             t=t//10
#         if rev==i:
#             p=p+1
#             if p%2==1:
#                 s=s+1
#                 if s>1:
#                     print(end=",")
#                 print("",i,end="")
#     if p==0:
#         print("No Palindrome Values")
#     else:
#         print(".")
            
'''Write a program to print all Palindrome Numbers between the Given Numbers?            
        '''
# a=int(input())
# b=int(input())
# if a<0 or b<0:
#     print("InvaliD InputS")
# else:
#     if a>b:
#         a,b=b,a
#     s=0
#     for i in range(a+1,b):
#         t=i
#         c=0
#         while(i>0):
#             r=i%10
#             c=c*10+r
#             i=i//10
#         if c==t:
#             s=s+1
#             print(t)
#     if s==0:
#         print("No Palindrome Values")
        
'''Write a program to print the Sum of all Alternative Palindrome Numbers Between the Given Numbers?'''

# a=int(input())
# b=int(input())
# if a==0 or b==0:
#     print("Invalid Inputs")
# else:
#     if a<0 or b<0:
#         a=abs(a)
#         b=abs(b)
#     if a>b:
#         a,b=b,a
#     sum=0
#     k=0
#     l=0
#     for i in range(a+1,b):
#         t=i
#         rev=0
#         while(i>0):
#             r=i%10
#             rev=rev*10+r
#             i=i//10
#         if rev==t:
#             k=k+1
#             if k%2==1:
#                 l=l+1
#                 if l==1:
#                     print(f"Sum of Alternative Palindrome Numbers between the {a} and {b} is ",end="")
#                 if l>1:
#                     print(end=" + ")
#                 sum=sum+t
#                 print(t,end="")
#     if k==0:
#         print("No Palindrome Values")
#     else:
#         print(" =",sum,end="")
#         print(".")
            
'''Write a program to Print the Reverse of a Given Number?'''

# a=int(input())
# if a<=0:
#     print("InValid Input")
# else:
#     rev=0
#     while(a>0):
#         r=a%10
#         rev=rev*10+r
#         a=a//10
#     print(rev)
    
'''Write a program to print the Sum of the Armstrong Numbers in the Given Range?'''

# a=int(input())
# b=int(input())
# if a==0 or b==0:
#     print("Invalid Inputs")
# else:
#     if a<0 or b<0:
#         a=abs(a)
#         b=abs(b)
#     if a>b:
#         a,b=b,a
#     sum=0
#     l=0
#     for i in range(a,b+1):
#         t=i
#         d=0
#         while(t>0):
#             r=t%10
#             d=d+1
#             t=t//10
#         t=i
#         s=0
#         while(t>0):
#             w=t%10
#             s=s+(w**d)
#             t=t//10
#         if s==i:
#             l=l+1
#             sum=sum+s
#             if l==1:
#                 print("Armstrong Numbers in the Given Range is ",end="")
#             if l>1:
#                 print(end=" + ")
#             print(s,end="")
#     if l==0:
#         print("No Armstrong Numbers in a Given Range.")
#     else:
#         print(" =",sum,end="")
#         print(".")

'''Write a program to print the Armstrong Numbers in the Given Range.'''

# a=int(input())
# b=int(input())
# if a<=0 or b<=0:
#     print("Invalid Inputs")
# else:
#     if a>b:
#         a,b=b,a
#     h=0
#     for i in range(a,b+1):
#         t=i
#         k=0
#         while(t>0):
#             r=t%10
#             k=k+1
#             t=t//10
#         t=i
#         s=0
#         while(t>0):
#             f=t%10
#             s=s+(f**k)
#             t=t//10
#         if s==i:
#             h=h+1
#             if h==1:
#                 print("Armstrong Numbers in the Given Range is",end="")
#             if h>1:
#                 print(end=",")
#             print("",s,end="")
#     if h==0:
#         print("No Armstrong Numbers")
#     else:
#         print(".")
       
'''Write a program to Count the Number of digits in a Given Number?
            '''

# a=int(input())
# if a<=10:
#     print("Invalid Input")
# else:
#     d=0
#     while(a>0):
#         r=a%10
#         d=d+1
#         a=a//10
#     print(d)
    
'''Write a program to print the Armstrong Numbers between the Given two values.'''

# a=int(input())
# b=int(input())
# if a==0 or b==0:
#     print("Invalid Inputs")
# else:
#     if a<0 or b<0:
#         a=abs(a)
#         b=abs(b)
#     if a>b:
#         a,b=b,a
#     h=0
#     for i in range(a+1,b):
#         t=i
#         d=0
#         while(t>0):
#             r=t%10
#             d=d+1
#             t=t//10
#         t=i
#         s=0
#         while(t>0):
#             w=t%10
#             s=s+(w**d)
#             t=t//10
#         if s==i:
#             h=h+1
#             if h==1:
#                 print("Armstrong Numbers between the Given Values is",end="")
#             if h>1:
#                 print(end=",")
#             print("",s,end="")
#     if h==0:
#         print("No Armstrong Numbers Between Given Values")
#     else:
#         print(".")
            
'''Write a program to print the Alternative Armstrong Numbers between the Given Values?
        '''   
# a=int(input())
# b=int(input())
# if a==0 or b==0:
#     print("Invalid Inputs")
# else:
#     if a<0 or b<0:
#         a=abs(a)
#         b=abs(b)
#     if a>b:
#         a,b=b,a
#     f=0
#     p=0
#     for i in range(a+1,b):
#         t=i
#         g=0
#         while(t>0):
#             e=t%10
#             g=g+1
#             t=t//10
#         t=i
#         r=0
#         while(t>0):
#             y=t%10
#             r=r+(y**g)
#             t=t//10
#         if r==i:
#             f=f+1
#             if f%2==1:
#                 p=p+1
#                 if p==1:
#                     print("Alternative Armstrong Numbers between the Given Values is",end="")
#                 if p>1:
#                     print(end=",")
#                 print("",r,end="")
#     if f==0:
#         print("No Armstrong Numbers Between Given Values.")
#     else:
#         print(".")
                 
'''Write a program to Calculate Power of a Number. (With Pre Defined Method)'''

# a=int(input())
# b=int(input())
# if a<=0 or b<=0:
#     print("Invalid Inputs")
# else:
#     print(f"{a} Power {b} value is {a**b}.")

'''Write a Program to Check if The given year is Leap Year or not?'''

# a=int(input())
# if a>0:
#     if(((a%4==0)and(a%100!=0))or(a%400==0)):
#         print("Leap Year.")
#     else:
#         print("Not a Leap Year.") 
        
# else:        
        
#     print("Given Year is Invalid Input.")

'''Write a program to check if the Given Number is Armstrong or not?'''

'''Write a program to check Whether the Given Number(any number of digits) is Armstrong or Not.'''
# a=int(input())
# if a<=0:
#     print("Invalid Input")
# else:
#     g=a
#     d=0
#     while(g>0):
#         r=g%10
#         d=d+1
#         g=g//10
#     g=a
#     s=0
#     while(g>0):
#         l=g%10
#         s=s+(l**d)
#         g=g//10
#     if s==a:
#         print(f"{a} is a Armstrong Number.")
#     else:
#         print(f"{a} is Not a Armstrong Number.")


