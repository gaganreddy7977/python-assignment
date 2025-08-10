# TUPLE DATATYPE ASSIGNMENT
# ========================

# SOLVED EXAMPLE
# --------------
# Question: Find the sum and product of all elements in a tuple
print("SOLVED EXAMPLE:")
print("Find the sum and product of all elements in a tuple")
numbers = (2, 4, 6, 8, 10)
sum_tuple = sum(numbers)
product = 1
for num in numbers:
    product *= num
print(f"Tuple: {numbers}")
print(f"Sum: {sum_tuple}")
print(f"Product: {product}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a tuple of first 10 natural numbers
print("Question 1: Create a tuple of first 10 natural numbers")
x=tuple(range(10))
print(x)

# Question 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("\nQuestion 2: Find the length of tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)")
x=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
y=len(x)
print(y)

# Question 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')
print("\nQuestion 3: Access the 3rd element from tuple ('a', 'b', 'c', 'd', 'e')")
x=('a', 'b', 'c', 'd', 'e')
y=x[3]
print(y)

# Question 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)
print("\nQuestion 4: Find the maximum value in tuple (23, 45, 12, 67, 34, 89, 56)")
x=(23, 45, 12, 67, 34, 89, 56)
y=max(x)
print(y)

# Question 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)
print("\nQuestion 5: Count how many times 5 appears in (1, 5, 2, 5, 3, 5, 4, 5, 6)")
x=(1, 5, 2, 5, 3, 5, 4, 5, 6)
y=5
count=0
for i in x:
    if i==y:
       count +=1
print(count)

# Question 6: Create a tuple of mixed data types (integer, float, string, boolean)
print("\nQuestion 6: Create a tuple of mixed data types (integer, float, string, boolean)")
x=(1,2.2,"hi",True)
print(x)


# Question 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')
print("\nQuestion 7: Find the index of element 'python' in ('java', 'python', 'c++', 'javascript')")
x=('java', 'python', 'c++', 'javascript')
y=x.index('python')
print(y)

# Question 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)
print("\nQuestion 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)")
x=(10, 20, 30, 40, 50)
if i in x:
    i==25
print(f'true')

# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")
x=tuple(range(11))
for i in x:
    if i%2==0 :
        
     print(i)

# Question 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)
print("\nQuestion 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)")
x=(15, 23, 31, 42, 56, 78)
y=sum(x)/len(x)
print(y)