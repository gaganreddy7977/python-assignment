# SET DATATYPE ASSIGNMENT
# ======================

# SOLVED EXAMPLE
# --------------
# Question: Find the union of two sets
print("SOLVED EXAMPLE:")
print("Find the union of two sets")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union_set = set1.union(set2)
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {union_set}")
print("-" * 50)

# ASSIGNMENT QUESTIONS
# ===================

# Question 1: Create a set of first 10 natural numbers
print("Question 1: Create a set of first 10 natural numbers")
x=set(range(0,10))
print(x)


# Question 2: Add element 11 to set {1, 2, 3, 4, 5}
print("\nQuestion 2: Add element 11 to set {1, 2, 3, 4, 5}")
x={1, 2, 3, 4, 5}
x.add(11)
print(x)

# Question 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}
print("\nQuestion 3: Remove element 3 from set {1, 2, 3, 4, 5, 6}")
x={1, 2, 3, 4, 5, 6}
x.remove(3)
print(x)

# Question 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 4: Find the intersection of {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
x={1, 2, 3, 4, 5}
y={4, 5, 6, 7, 8}
n=x.intersection(y)
print(n)

# Question 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}
print("\nQuestion 5: Find the difference between {1, 2, 3, 4, 5} and {4, 5, 6, 7, 8}")
x={1, 2, 3, 4, 5}
y={4, 5, 6, 7, 8}
n=x.difference(y)
print(n)

# Question 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}
print("\nQuestion 6: Check if 5 is in set {1, 2, 3, 4, 6, 7, 8}")
x={1, 2, 3, 4, 6, 7, 8}
y={5}
if x in y:
        print(True)
else:
        print(False)



# Question 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}
print("\nQuestion 7: Find the length of set {'a', 'b', 'c', 'd', 'e'}")
x={'a', 'b', 'c', 'd', 'e'}
y=len(x)
print(y)


# Question 8: Create a set of vowels from string "hello world"
print("\nQuestion 8: Create a set of vowels from string 'hello world'")
x=("aeiou")
y=("hello world")

for i in x:
    if i in y:
        print(i)


# Question 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set
print("\nQuestion 9: Remove duplicates from list [1, 2, 2, 3, 4, 4, 5, 6, 6, 7] using set")
x={1, 2, 2, 3, 4, 4, 5, 6, 6, 7}
y=set(x)
print(y)


# Question 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}
print("\nQuestion 10: Check if {1, 2, 3} is a subset of {1, 2, 3, 4, 5, 6}")
x={1, 2, 3}
y={1, 2, 3, 4, 5, 6}
c=x.issubset(y)
print(c)