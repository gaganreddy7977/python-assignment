# DICTIONARY DATATYPE ASSIGNMENT - 50 QUESTIONS
# ============================================

# SOLVED EXAMPLE
# --------------
# Question: Find the key with maximum value in a dictionary
print("SOLVED EXAMPLE:")
print("Find the key with maximum value in a dictionary")
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 95, 'Eve': 88}
max_key = max(scores, key=scores.get)
max_value = scores[max_key]
print(f"Dictionary: {scores}")
print(f"Key with maximum value: {max_key}")
print(f"Maximum value: {max_value}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Create a dictionary of student names and their ages
print("Question 1: Create a dictionary of student names and their ages")
x={'name':'gagan','ages':'23'}
print(x)

# Question 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}
print("\nQuestion 2: Add a new key-value pair to dictionary {'a': 1, 'b': 2, 'c': 3}")
x={'a': 1, 'b': 2, 'c': 3}
x.update({'d':4})
print(x)

# Question 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}
print("\nQuestion 3: Get all keys from dictionary {'name': 'John', 'age': 25, 'city': 'New York'}")
y={'name': 'John', 'age': 25, 'city': 'New York'}
x=y.keys()
if 'age' in x:
    print(True)
else:
    print(False)

# Question 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}
print("\nQuestion 4: Get all values from dictionary {'python': 3, 'java': 2, 'c++': 1}")
y={'python': 3, 'java': 2, 'c++': 1}
x=y.values()
print(x)

# Question 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}
print("\nQuestion 5: Check if key 'age' exists in {'name': 'Alice', 'age': 30, 'city': 'London'}")
str={'name': 'Alice', 'age': 30, 'city': 'London'}
x=str.keys()
if 'age' in x:
    print(True)
else:
    print(False)


# Question 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}
print("\nQuestion 6: Remove key 'temp' from {'a': 1, 'b': 2, 'temp': 3, 'c': 4}")
x={'a': 1, 'b': 2, 'temp': 3, 'c': 4}
str=x.pop('temp')
print(str)


# Question 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}
print("\nQuestion 7: Find the sum of all values in {'math': 85, 'science': 92, 'english': 78}")
x= {'math': 85, 'science': 92, 'english': 78}
y=sum(x.values())
print(y)

# Question 8: Create a dictionary with squares of numbers 1 to 5
print("\nQuestion 8: Create a dictionary with squares of numbers 1 to 5")
squares = {x: x**2 for x in range(1, 6)}
print(squares)


# Question 9: Count frequency of each character in string "hello"
print("\nQuestion 9: Count frequency of each character in string 'hello'")
str='hello'
y={} 
for i in str:
    if i in y:
        y[i]+=1
    else:
        y[i]=1
print(y)



# Question 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}
print("\nQuestion 10: Merge two dictionaries {'a': 1, 'b': 2} and {'c': 3, 'd': 4}")
e=dict({'a': 1, 'b': 2})
y=dict({'c': 3, 'd': 4})
print(e|y, end=' ')



# Question 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 11: Create a nested dictionary: {'person': {'name': 'Alice', 'age': 25}}")
dict={'person': {'name': 'Alice', 'age': 25}}
print(dict)

# Question 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}
print("\nQuestion 12: Access nested value 'name' from {'person': {'name': 'Alice', 'age': 25}}")
D={'person': {'name': 'Alice', 'age': 25}}
A=dict["person"]["name"]
print(A)

# Question 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
print("\nQuestion 13: Create a dictionary with list values: {'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}")
I={'fruits': ['apple', 'banana'], 'colors': ['red', 'blue']}
L=I.values()
print(L)

# Question 14: Add 'orange' to the 'fruits' list in nested dictionary
print("\nQuestion 14: Add 'orange' to the 'fruits' list in nested dictionary")
I['fruits'].append('orange')
print(I)


# Question 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}
print("\nQuestion 15: Create a dictionary with tuple values: {'coordinates': (10, 20), 'rgb': (255, 0, 0)}")
Z={'coordinates': (10, 20), 'rgb': (255, 0, 0)}

# Question 16: Extract first coordinate from nested tuple
print("\nQuestion 16: Extract first coordinate from nested tuple")
A=Z['coordinates']
print(A)

# Question 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
print("\nQuestion 17: Create a dictionary with set values: {'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}")
A={'vowels': {'a', 'e', 'i'}, 'consonants': {'b', 'c', 'd'}}
W=A.values()
print(W)

# Question 18: Add 'o' to vowels set in nested dictionary
print("\nQuestion 18: Add 'o' to vowels set in nested dictionary")
A['vowels'].update({'o'})
print(A)

# Question 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}
print("\nQuestion 19: Create a 3-level nested dictionary: {'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}")
x={'company': {'department': {'employee': {'name': 'John', 'id': 123}}}}

# Question 20: Access employee name from 3-level nested dictionary
print("\nQuestion 20: Access employee name from 3-level nested dictionary")
t=x['company']['department']['employee'].values()
print(t)

# Question 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}
print("\nQuestion 21: Create a dictionary with mixed data types: {'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}")
data_types={'int': 42, 'float': 3.14, 'str': 'hello', 'bool': True}

# Question 22: Check data type of each value in mixed dictionary
print("\nQuestion 22: Check data type of each value in mixed dictionary")
l=data_types.values()
print(l)

# Question 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}
print("\nQuestion 23: Create a dictionary with function values: {'len': len, 'str': str, 'int': int}")
fun= {'len': len, 'str': str, 'int': int}
print(fun)

# Question 24: Apply each function to "123" using dictionary
print("\nQuestion 24: Apply each function to '123' using dictionary")
fun= {'len': len, 'str': str, 'int': int}
fun.update({'len':123,'str':123 ,'int':123})
print(fun)


# Z={'a': None, 'b': None, 'c': None}
# Z.update({'a':0,'b':0,'c':0})
# print(Z)

# Question 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}
print("\nQuestion 25: Create a dictionary with lambda functions: {'double': lambda x: x*2, 'square': lambda x: x**2}")
Q={'double': lambda x: x*2, 'square': lambda x: x**2}
print(Q)

# Question 26: Apply each lambda function to 5
print("\nQuestion 26: Apply each lambda function to 5")
Q={'double': lambda x: x*2, 'square': lambda x: x**2 ,}
if x==5:
    print(dict(Q))



# Question 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}
print("\nQuestion 27: Create a dictionary with class values: {'list': list, 'dict': dict, 'set': set}")
X={'list': list, 'dict': dict, 'set': set}
print(X)


# Question 28: Create instances using class dictionary
print("\nQuestion 28: Create instances using class dictionary")

# Question 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}
print("\nQuestion 29: Create a dictionary with None values: {'a': None, 'b': None, 'c': None}")
Z={'a': None, 'b': None, 'c': None}
Z.update({'a':0,'b':0,'c':0})
print(Z)

# Question 30: Replace all None values with 0
print("\nQuestion 30: Replace all None values with 0")
Z={'a': None, 'b': None, 'c': None}
Z.update({'a':0,'b':0,'c':0})
print(Z)

# Question 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}
print("\nQuestion 31: Create a dictionary with boolean values: {'is_active': True, 'is_admin': False}")
t={'is_active': True, 'is_admin': False}

# Question 32: Count True values in boolean dictionary
print("\nQuestion 32: Count True values in boolean dictionary")
q=t.values()
count=0
for i in q:
    if i==True:
        count+=1
print(count)


# Question 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}
print("\nQuestion 33: Create a dictionary with complex numbers: {'z1': 3+4j, 'z2': 1+2j}")
z={'z1': 3+4j, 'z2': 1+2j}
print(z)


# Question 34: Find magnitude of each complex number
print("\nQuestion 34: Find magnitude of each complex number")
q=z.values()
t=[]
for i in q:
    z=abs(i)
    t.append(z)
print(t)


# Question 35: Create a 4-level nested dictionary
print("\nQuestion 35: Create a 4-level nested dictionary")
q={'school':{'princely':{'den':{'teacher':'student'}}}}

# Question 36: Access deepest value in 4-level nested dictionary
print("\nQuestion 36: Access deepest value in 4-level nested dictionary")
e=q['school']['princely']['den']['teacher']
print(e)

# Question 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}
print("\nQuestion 37: Create a dictionary with range values: {'r1': range(3), 'r2': range(5)}")
q={'r1': range(3), 'r2': range(5)}
print(q)

# Question 38: Convert each range to list
print("\nQuestion 38: Convert each range to list")
a=list(range(3))
b=list(range(5))
t={'r1':a,'r2':b}
print(t)



# Question 39: Create a dictionary with generator values
print("\nQuestion 39: Create a dictionary with generator values")
d = {'a': 1, 'b': 2, 'c': 3}
v = (i for i in d.values())
for i in v:
    print(i)

# Question 40: Convert each generator to list
print("\nQuestion 40: Convert each generator to list")
d = {'a': 1, 'b': 2, 'c': 3}                    ##
v = (i for i in d.values())
t=[]
for i in v:
    t.append(i)
print(t)

# Question 41: Create a dictionary with iterator values
print("\nQuestion 41: Create a dictionary with iterator values")
r = iter(range(1, 6))                                       
y = {i: next(r) for i in range(5)}
print(y)

# Question 42: Extract all elements from each iterator
print("\nQuestion 42: Extract all elements from each iterator")
elements=y.items()
print(elements)



# Question 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}
print("\nQuestion 43: Create a dictionary with nested lists: {'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}")
lists={'matrix': [[1, 2], [3, 4]], 'vector': [5, 6, 7]}


# Question 44: Find sum of each nested list
print("\nQuestion 44: Find sum of each nested list")
a=lists['matrix']
A=[]
for i in a:
        z=sum(i)
        A.append(z)
print(A)

b=sum(lists['vector'])
print([b])
nested_list={'matrix':A,'vector':[b]}
print(nested_list)




# Question 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}
print("\nQuestion 45: Create a dictionary with nested dictionaries: {'config': {'db': {'host': 'localhost', 'port': 5432}}}")
M={'config': {'db': {'host': 'localhost', 'port': 5432}}}
print(M)

# Question 46: Access database port from nested configuration
print("\nQuestion 46: Access database port from nested configuration")
A=M['config']['db']['port']
print(A)


# Question 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print("\nQuestion 47: Create a dictionary with nested tuples: {'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}")
Q={'points': ((1, 2), (3, 4)), 'rgb': ((255, 0, 0), (0, 255, 0))}
print(Q)

# Question 48: Extract first point coordinates
print("\nQuestion 48: Extract first point coordinates")
E=Q['points']
W=E[0]
print(W)


# Question 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}
print("\nQuestion 49: Create a dictionary with nested sets: {'groups': {{1, 2, 3}, {4, 5, 6}}, 'categories': {{'a', 'b'}, {'c', 'd'}}}")
A={'groups': {frozenset({1, 2, 3}), frozenset({4, 5, 6})}, 'categories': {frozenset({'a', 'b'}), frozenset({'c', 'd'})}}
print(A)
# Question 50: Find union of all nested sets
print("\nQuestion 50: Find union of all nested sets")
B=A['groups']
C=A['categories']
union_group=set().union(*B)
print(union_group)
union_categories=set().union(*C)
print(union_categories)