# INTEGER DATATYPE ASSIGNMENT
# ===========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the sum of first 5 even numbers
print("SOLVED EXAMPLE:")
print("Calculate the sum of first 5 even numbers")
first_5_even = [2, 4, 6, 8, 10]
sum_even = sum(first_5_even)
print(f"First 5 even numbers: {first_5_even}")
print(f"Sum: {sum_even}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the product of first 10 natural numbers
print("Question 1: Calculate the product of first 10 natural numbers")
import math
x=[0,1,2,3,4,5,6,7,8,9]
y = math.prod(x)
print(y)


# Question 2: Find the remainder when 156 is divided by 7
print("\nQuestion 2: Find the remainder when 156 is divided by 7")
import math
x=156
y=7
A=x/y
print(A)

# Question 3: Calculate the square of 25
print("\nQuestion 3: Calculate the square of 25")
x=25
y=x**2
print(y)

# Question 4: Find the cube root of 125
print("\nQuestion 4: Find the cube root of 125")
x=125
y=x**3
print(y)

# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")
x=[1,2,3,4,5]
y=sum(x)
print(y)

# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")
x=97
if x%2==0:
    print("97 is  not a even number")
else:
    print("97 is a prime num")
    


# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")
import math
x=8
x=math.factorial(8)
print(x)

# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")
x=[15,23,31,42,56]
y=sum(x)/(len(x))
print(y)
# Question 9: Find the greatest common divisor (GCD) of 48 and 36
print("\nQuestion 9: Find the greatest common divisor (GCD) of 48 and 36")
import math
x=48
y=36
z=math.gcd(x,y)
print(z)

# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")
#for int i in range (0,40):
 #   if (i%2==1):
  #      print(i, end=' ')
   #     print=sum(i)
x=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]
y=sum(x)
print(y)

    
    

