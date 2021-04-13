# 0. Print Message on Display.
    # syntax: print("message") 
print("Hello, World!")

# 1. To know the type of any value 

    # syntax: type(value) 
type("Hello, World!")

type(123)

# 2. Scope of variable

a=10

b=a+1

print(b)

# 3. Addition of two numbers

a=int(input("Enter your first number : "))
b=int(input("Enter your second numbers : "))
sum=a+b
print("The sum of",a,"and",b,"is",sum)

# 4. Swapping of two variables.

    # usually we swap with the temp variable as 
	
	A=30
	B=40
	Temp=A
	A=B
	B=Temp
	print(A)
	print(B)
	
	# In Python, concept of multiple assignment, it can simplify the task of swapping two numbers.
	
	A=20
	B=30
	A , B = B , A
	print(A)
	print(B)
	
# 5. Calculate area of rectangle using input()

    # We can use float() instead of int()
	
print("Enter length:",end='')
length=int(input())
print("Enter breadth:",end='')
breadth=int(input())
area=length*breadth
print("Area of Rectangle is:",area)

# 6. Python Inbuilt Functions 

    # absolute(abs) value of x
x=4
abs(x)

a=-4
abs(a)

    # print largest value among number 
max(10,50,80,999,70,90,99)	
    # print minimum value among number 
min(10,50,80,999,70,90,99)
    # print X^Y. syntax: pow(X,Y)
pow(2,3) 
    # prints an integer nearest to the value of x. syntax: round(x)
round(10.34)
round(10.89)

# 7. Inbuilt Mathematical Functions in Python 

import math as m
m.ceil(10.23)              # ceil(x) -> round x to nearest integer and returns that integer      
m.floor(18.9)              # floor(x) -> returns the largest value not greater than x    
m.exp(1)                   # exp(x) -> returns the exponential value for e^x 
m.log(2.7184457)           # log(x) -> returns the natural logarithmic of x (to base e)   
m.log(8,2)                 # log(x,base) -> returns the logarithmic of x to the given base 
m.sqrt(9)                  # sqrt(x) -> returns the square root of x 
m.sin(3.14159/2)           # sin(x) -> return the sin of x, where x is in radians 
m.asin(1)                  # asin(x) -> return the angle in radians for the inverse of sine 
m.cos(0)                   # cos(x) -> return the sin of x, where x is in radians 
m.acos(1)                  # acos(x) -> return the angle in radians for the inverse of cosine
m.tan(3.14/4)              # tan(x) -> return the tangent of x, where x is in radians 
m.degrees(1.57)            # degrees(x) -> convert angle x from radians to degree 
m.radians(89.99999)        # radians(x) -> convert angle x from degrees to radians  

# 8. Print ASCII values of characters ( syntax: ord('char')  ) 

ord('A')
ord('Z')
ord('a')
ord('z')

# 9. Print the character corresponding to its ASCII code. ( syntax: chr('char')  ) 

chr(90)
chr(65)
chr(97)
chr(122)

# 10. Calculate the square and cube of a number. 

num=input("Enter number:")
print("Number:",num)
sq=num*num
cube=num*num*num
print("Sqaure of number ",num," is ",sq) 
print("Cube of number ",num," is ",cube)

# 11. Calculate Simple Interest 

P=float(input("Enter the value of Principal : "))
R=float(input("Enter the Rate : "))
T=int(input("Enter the Time : "))
SI=(P*R*T)/100
print("The Simple Interest is : ",SI)

# 12. Calculate temperature in Celsius and convert it into Fahrenheit 

celsius=eval(input("Enter degrees in Celsius: "))
print("Celsius:",celsius)
Fahrenheit=(9/5)*celsius+32
print("Fahrenheit : ",Fahrenheit )
