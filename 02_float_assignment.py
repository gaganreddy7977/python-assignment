# FLOAT DATATYPE ASSIGNMENT
# =========================

# SOLVED EXAMPLE
# --------------
# Question: Calculate the area of a circle with radius 5.5
print("SOLVED EXAMPLE:")
print("Calculate the area of a circle with radius 5.5")
import math
radius = 5.5
area = math.pi * radius ** 2
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577
print("Question 1: Calculate the average of 3.14, 2.718, 1.618, 0.577")
x=(3.14, 2.718, 1.618, 0.577)
y=(sum(x)/len(x))
print(y)

# Question 2: Convert 98.6 Fahrenheit to Celsius (F = C * 9/5 + 32)
print("\nQuestion 2: Convert 98.6 Fahrenheit to Celsius")
x=(98.6)
c=((x/(5/9))+32)
print(f"celsius :{c}")


# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")
p=1000
r=5.5
n=1
t=3
A=p*(1+(r/1)**(n*t))
print(A)

# Question 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2
print("\nQuestion 4: Find the hypotenuse of a right triangle with sides 3.5 and 4.2")
import math
x=(3.5)**2
y=(4.2)**2
A=math.sqrt(x+y)
print(f"the hypotenuse of a right triangle with sides 3.5 and 4.2 :{A}")


# Question 5: Calculate the volume of a sphere with radius 7.8
print("\nQuestion 5: Calculate the volume of a sphere with radius 7.8")
import math
r=7.8
A=math.pi*(4/3)*r**3
print(f"the volume of a sphere with radius 7.8 :{A}")

# Question 6: Round 3.14159 to 3 decimal places
print("\nQuestion 6: Round 3.14159 to 3 decimal places")
print(round(3.14159,3))

# Question 7: Calculate the percentage: 45 out of 67
print("\nQuestion 7: Calculate the percentage: 45 out of 67")
import math
x=45
y=67
a=(x/y)*100
print(f"the percentage: 45 out of 67 :{a}")

# Question 8: Find the square root of 23.456
print("\nQuestion 8: Find the square root of 23.456")
import math
x=23.456
y=math.sqrt(x)
print(f"the square root of 23.456 is :{y}")

# Question 9: Calculate the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years
print("\nQuestion 9: Calculate simple interest: Principal=2500, Rate=6.5%, Time=2.5 years")
x=2500*(1+(6.5*2.5))
print(f"the simple interest: Principal=2500, Rate=6.5%, Time=2.5 years : {x}" )

# Question 10: Convert 45.7 degrees to radians
print("\nQuestion 10: Convert 45.7 degrees to radians")
import math
x=45.7
w=((math.pi/180)*x)
print(f"the 45.7 degress to radians is :{w} ")