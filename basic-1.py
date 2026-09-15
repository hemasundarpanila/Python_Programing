
# Write a program to perform Addition, Subtraction, Multiplication and Division of 2 Numbers based on the user inputs by using Switch condition.(+ , - , * , /, %).

# a=int(input())
# b=int(input())
# c=input()
# if c=="+":
#     print(a+b)
# elif c=="-":
#     print(a-b)
# elif c=="*":
#     print(a*b)
# elif c=="//":
#     print(a//b)  
# else:
#     print(a%b)



# write a program to perform all these tasks

# a.     Store a number in a variable

# b.    If value is not in range (100-1000) prints WRONG NUMBER else follows the steps

# c.     Check even or odd

# d.    If even divide the number by 3 and print the remainder

# e.     If odd divide the number by 2 and print the remainder.



# n=int(input())
# if n<100 or n>1000:
#     print("WRONG NUMBER")
# else:
#     if n%2==0:
#         print(n%3)
#     else:
#         print(n%2)


# Write a program to find sum of all the numbers in given range if starting index is greater than ending index print INVALID RANGE



# a=int(input())
# b=int(input())
# sum=0
# if a>b:
#     print("INVALID RANGE")
# else:
#     for i in range(a,b+1):
#         sum=sum+i
#     print(sum)
    
# Write a program to print CVCORP for 'N' times



# a=int(input())
# if 10<a<100:
#     for i in range(a):
#         print("CVCORP")
# else:
#     print("Invalid Input")


# Write a program to print all even numbers in range .if starting range is greater than ending range print "INVALID RANGE"


# a=int(input())
# b=int(input())
# if a>b:
#     print("INVALID RANGE")
# else:
#     for i in range(a,b+1):
#         if i%2==0:
#             print(i,end=" ")


# Write a program to convert temperature from degree celcisu (C) to Farenheit (F).
# n=int(input())
# print(f"{(n*9/5)+32}F")


# write a progrm to perform given tasks

# Declare & initialize a number.

# Check whether the number is in range 0-100 or not.

# If not in range print INVALID INPUT

# Else – if the number is in range 91-100 then print SUPER SMART,

# 81-90 print SMART,

# 71-80 print SMART ENOUGH,

# 61-70 print JUST SMART,

# 36-60 print NO SMART,

# 0-35 print DUMB.

# n=int(input())
# print(f"{(n*9/5)+32}F")
# n=int(input())
# if 0<=n and n<=100:
#     if 91<= n <=100:
#         print("SUPER SMART")
#     elif 81<=n <= 90:
#         print("SMART")
#     elif 71<=n <=80:
#         print("SMART ENOUGH")
#     elif 61<=n <=70:
#         print("JUST SMART")
#     elif 36<=n<=60:
#         print("NO SMART")
#     else:
#         print("DUMB")
# else:
#     print("INVALID INPUT")




# n=float(input())
# m=int(n*1000)
# print(f"{m} Grams")

# a=int(input())
# b=int(input())
# c=int(input())
# if a>b and a>c:
#     print(a,"is a Biggest Number from the Given Numbers")
# elif b>a and b>c:
#     print(b,"is a Biggest Number from the Given Numbers")
# else:
#     print(c,"is a Biggest Number from the Given Numbers")

# a=int(input())
# b=int(input())
# if a>b:
#     print("INVALID RANGE")
# else:
#     c=0
#     for i in range(a,b+1):
#         if i%11==0:
#             print(i,end=" ")
#             c=c+1
#     if c==0:
#         print("NO NUMBERS")


