'''Write a Program to Print the following Basic Pattern?

If Input is 5 4 then Print 

* * * *

* * * *

* * * *

* * * *

* * * *'''

a=int(input())
b=int(input())
if a<=0 or b<=0:
    print("Invalid Inputs")
else:
    for i in range(1,a+1):
        for j in range(1,b+1):
            print("*",end=" ")
        print()

'''Write a Program to Print the following Basic Pattern?

If Input is 5 and 6 then Print 

* * * * * *

* $ $ $ $ *

* $ $ $ $ *

* $ $ $ $ *

* * * * * *'''

n=int(input())
n2=int(input())
if n<=0 or n2<=0:
    print("Invalid Inputs")
else:
    for i in range(1,n+1):
        for j in range(1,n2+1):
            if i==1 or i==n or j==1 or j==n2:
                print("*",end=" ")
            else:
                print("$",end=" ")
        print()


'''Write a Program to Print the following Basic Pattern?

If Input is 5 then Print 

* * * * *

* * * * *

* * * * *

* * * * *

* * * * *'''

n=int(input())
if n>0:
    for i in range(1,n+1):
        for j in range(1,n+1):
            print("*",end=" ")
        print()

'''Write a Program to Print the following Basic Pattern?

If Input is 5 then Print 

1 0 1 0 1

1 0 1 0 1

1 0 1 0 1

1 0 1 0 1

1 0 1 0 1'''

n=int(input())
if n<=0:
    print("Invalid Input")
else:
    if n%2==1:
        for i in range(1,n+1):
            c=0
            for j in range(1,n+1):
                c=c+1
                if c%2==0:
                    print(0,end=" ")
                else:
                    print(1,end=" ")
            print()
    else:

        for i in range(1,n+1):
            for j in range(1,n+1):
                if (i+j)%2==0:
                    print(1,end=" ")
                else:
                    print(0,end=" ")
            print()
'''                
Write a Program to Print the following Basic Pattern?

If Input is 5 and 5 then Print 

1*2*3*4*5

6*7*8*9*10

11*12*13*14*15

16*17*18*19*20

21*22*23*24*25'''

n=int(input())
n2=int(input())
if n<=0 and n2<=0:
    print("Invalid Row and Column Values")
elif n<=0:
    print("Invalid Row Value")
elif n2<=0:
    print("Invalid Column Value")
else:
    a=1
    for i in range(1,n+1):
        k=0
        for j in range(1,n2+1):
            k=k+1
            if k>1:
                print("*",end="")
            print(a,end="")
            a=a+1
        print()
'''
Write a Program to Print the following Basic Pattern?

If Input is 5 then Print 

1 1 1 1 1

2 2 2 2 2

3 3 3 3 3

4 4 4 4 4

5 5 5 5 5
            '''

n=int(input())
if n<=0:
    print("InValid InPut")
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(i,end=" ")
        print()

'''Write a Program to Print the following Basic Pattern?

If Input is 6 then Print 

1 1 1 1 1 1

1 1 1 1 2 2

1 1 1 3 3 3

1 1 4 4 4 4

1 5 5 5 5 5

6 6 6 6 6 6'''

n=int(input())
if n<=0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i+j)>(n+1) or (i+j)==(n+1):
                print(i,end=" ")
            else:
                print(1,end=" ")
        print()

'''Write a Program to Print the following Basic Pattern?

If Input is 5 then Print 

1 2 3 * 5

6 7 * 9 10

11 * 13 14 15

* 17 18 19 *

21 22 23 * 25'''

n=int(input())
if n<=0:
    print("Given Value is Invalid")
else:
    a=1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a%4==0:
                print("*",end=" ")
            else:
                print(a,end=" ")
            a=a+1
        print()

'''Write a Program to Print the following Basic Pattern?

If Input is 5 then Print 

55555

54444

54333

54322

54321'''

n=int(input())
if n==0:
    print("InvaliD Input")
else:
    n=abs(n)
    for i in range(n,0,-1):
        for j in range(n,0,-1):
            if j>=i:
                print(j,end="")
            else:
                print(i,end="")

        print()

'''Write a Program to Print the following Basic Pattern?

If Input is 3 and 5 then Print 

1 2 3 4 5

6 7 8 9 10

11 12 13 14 15'''

n=int(input())
n2=int(input())
if n==0 or n2==0:
    print("Invalid Inputs")
else:
    n=abs(n)
    n2=abs(n2)
    a=1
    for i in range(1,n+1):
        for j in range(1,n2+1):
            print(a,end=" ")
            a=a+1
        print()

'''Write a Program to Print the following Basic Pattern?

If Input is 5 then Print 

1 0 0 0 0

0 2 0 0 0

0 0 3 0 0

0 0 0 4 0

0 0 0 0 5'''

n=int(input())
if n<=0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                print(j,end=" ")
            else:
                print(0,end=" ")
        print()

'''Write a Program to Print the following Basic Pattern?

If Input is 5 then Print 

1 2 3 4 5

1 2 3 4 5

1 2 3 4 5

1 2 3 4 5

1 2 3 4 5'''

n=int(input())
if n<=0:
    print("Invalid Input")
else:
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end=" ")
        print()