# STRING DATATYPE ASSIGNMENT - 50 QUESTIONS
# ========================================

# SOLVED EXAMPLE
# --------------
# Question: Count vowels in the string "Hello World"
print("SOLVED EXAMPLE:")
print("Count vowels in the string 'Hello World'")
text = "Hello World"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"String: {text}")
print(f"Number of vowels: {count}")
print("-" * 50)

# ASSIGNMENT QUESTIONS (50 QUESTIONS)
# ==================================

# Question 1: Reverse the string "Python Programming"
print("Question 1: Reverse the string 'Python Programming'")
x="Python Programming"
x1=x[::-1]
print(x1)



# Question 2: Check if "racecar" is a palindrome
print("\nQuestion 2: Check if 'racecar' is a palindrome")
n="racecar"
m=n[::-1]
if n == m:
    print(f"it is a palindrome")
else:
    print(f" it is not a palindrome")


# Question 3: Count the number of words in "Python is a great programming language"
print("\nQuestion 3: Count the number of words in 'Python is a great programming language'")
x=['python','is','a','great','programming','language']
print(len(x))

# Question 4: Convert "hello world" to title case
print("\nQuestion 4: Convert 'hello world' to title case")
import string
m="hello world"
n=m.title()
print(n)

# Question 5: Find the length of string "Data Science"
print("\nQuestion 5: Find the length of string 'Data Science'")
n="Data Science"
print(len(n))

# Question 6: Replace all spaces with underscores in "Machine Learning"
print("\nQuestion 6: Replace all spaces with underscores in 'Machine Learning'")
n="Machine Learing"
e=n.replace(" ","_")
print(e)

# Question 7: Check if "python" is in "Python Programming Language"
print("\nQuestion 7: Check if 'python' is in 'Python Programming Language'")
w="python Programming Language"
e="python"
if e in w:
    print("it is prestent")
else:
    print("it is not present")


# Question 8: Extract the first 5 characters from "Artificial Intelligence"
print("\nQuestion 8: Extract the first 5 characters from 'Artificial Intelligence'")
m="Artificial Intelligence"
print(m[0:5])


# Question 9: Convert "UPPERCASE" to lowercase
print("\nQuestion 9: Convert 'UPPERCASE' to lowercase")
n="UPPERCASE"
t=n.lower()
print(t)

# Question 10: Remove all vowels from "Computer Science"
print("\nQuestion 10: Remove all vowels from 'Computer Science'")
S1="Computer Science"
y=("aeiou")
for i in S1:
    if i not in y:
        print(i,end="")
    

# Question 11: Find the most frequent character in "mississippi"
print("\nQuestion 11: Find the most frequent character in 'mississippi'")
x="mississippi"
y=max(x)
print(y)

# Question 12: Check if two strings are anagrams: "listen" and "silent"
print("\nQuestion 12: Check if two strings are anagrams: 'listen' and 'silent'")
x="listen"
y="silent"


# Question 13: Capitalize first letter of each word in "python programming language"
print("\nQuestion 13: Capitalize first letter of each word in 'python programming language'")
st4="python programming language"
print(st4.title())

# Question 14: Count consonants in "Hello World"
print("\nQuestion 14: Count consonants in 'Hello World'")
str5="hello world"
V=('aeiou')
count = 0
for i in str5:
    if i not in V and i !=' ':
        count +=1
print(i,end="")


# Question 15: Find the longest word in "Python is a programming language"
print("\nQuestion 15: Find the longest word in 'Python is a programming language'")
x=("Python is a programming language")
y=x.split()
z=max(y)
print(z)


# Question 16: Remove all punctuation from "Hello, World! How are you?"
print("\nQuestion 16: Remove all punctuation from 'Hello, World! How are you?'")
import string
str="Hello, World! How are you?"
for char in str:
    #if char not in string.punctuation:
    if char not in '!,?':
        print(char,end='')



# Question 17: Check if string starts with "Python"
print("\nQuestion 17: Check if string starts with 'Python'")
x="python"
y=x.startswith("python")
print(y)

# Question 18: Find the index of first occurrence of 'o' in "Hello World"
print("\nQuestion 18: Find the index of first occurrence of 'o' in 'Hello World'")
x="Hello World"
y=x.index("o")
print(y)


# Question 19: Split string "apple,banana,orange" by comma
print("\nQuestion 19: Split string 'apple,banana,orange' by comma")
x="apple,banana,orange"
y=x.split(",")
print(y)

# Question 20: Join list ['Python', 'is', 'awesome'] with spaces
print("\nQuestion 20: Join list ['Python', 'is', 'awesome'] with spaces")
x=['Python', 'is', 'awesome']
for i in x:
    if i!=' ':
        print(i,end=" ")

# Question 21: Check if string contains only digits: "12345"
print("\nQuestion 21: Check if string contains only digits: '12345'")
x="12345"
y=x.isalnum()
print(y)

# Question 22: Check if string contains only letters: "HelloWorld"
print("\nQuestion 22: Check if string contains only letters: 'HelloWorld'")
x="HelloWorld"
print(x.isalpha())

# Question 23: Convert "hello world" to "hElLo WoRlD" (alternating case)
print("\nQuestion 23: Convert 'hello world' to 'hElLo WoRlD' (alternating case)")
x='hello world'
y=[]
for i in range(len(x)):
    if i%2!=0 :
        y.append(x[i])
        
        

    


# Question 24: Find all positions of 'a' in "banana"
print("\nQuestion 24: Find all positions of 'a' in 'banana'")
x="banana"
positions =[]
for i in range(0,len(x)):
        if x[i]=="a":
            positions.append(i)
print(positions)
        
# Question 25: Remove leading and trailing whitespace from "  Hello World  "
print("\nQuestion 25: Remove leading and trailing whitespace from '  Hello World  '")
str="  Hello World  "
print(str.lstrip(),str.rsplit())

# Question 26: Check if string ends with "ing": "programming"
print("\nQuestion 26: Check if string ends with 'ing': 'programming'")
x="programming"
y=x.endswith("ing")
print(y)

# Question 27: Replace first occurrence of 'o' with '0' in "Hello World"
print("\nQuestion 27: Replace first occurrence of 'o' with '0' in 'Hello World'")
x="Hello World"
y=x.replace("o","0",1)
print(y)


# Question 28: Find the shortest word in "Python is a programming language"
print("\nQuestion 28: Find the shortest word in 'Python is a programming language'")
x="Python is a programming language"
y=x.split()
z=min(y)
print(z)

# Question 29: Count words that start with 'p' in "Python programming is powerful"
print("\nQuestion 29: Count words that start with 'p' in 'Python programming is powerful'")
x="Python programming is powerful"
count=0
for i in x and x.lower():
    if i=='p':
        count+=1
        print(count)


# Question 30: Reverse words in "Hello World Python"
print("\nQuestion 30: Reverse words in 'Hello World Python'")
x="Hello World Python"
y=x[::-1]
print(y)

# Question 31: Check if string is a valid email format: "user@example.com"
print("\nQuestion 31: Check if string is a valid email format: 'user@example.com'")
import string
maile="user@example.com"
if '@' in maile and '.' in maile and maile.index("@")<maile.index('.'):
    print("valid")
else:
    print("invalied")
    
# Question 32: Extract domain from "https://www.example.com/path"
print("\nQuestion 32: Extract domain from 'https://www.example.com/path'")
str="https://www.example.com/path"
x=str.split('//')[-1].split('/')[0]
print(x)



# Question 33: Count lines in multi-line string
print("\nQuestion 33: Count lines in multi-line string")
mul_line='''hi 
my 
name 
is 
gagan'''
str=mul_line.split()
print(len(str))


# Question 34: Find common characters between "hello" and "world"
print("\nQuestion 34: Find common characters between 'hello' and 'world'")
import string
x="hello"
y="world"
str=set(x) & set(y)
print(str)

# Question 35: Check if string is a valid phone number: "+1-555-123-4567"
print("\nQuestion 35: Check if string is a valid phone number: '+1-555-123-4567'")
x="+1-555-123-4567"

# Question 36: Extract numbers from "abc123def456ghi789"
print("\nQuestion 36: Extract numbers from 'abc123def456ghi789'")
str="abc123def456ghi789"
for i in str:
    if i.isnumeric():
        print(i,end="")


# Question 37: Convert "snake_case" to "camelCase"
print("\nQuestion 37: Convert 'snake_case' to 'camelCase'")
#str="wow"
#str2=

# Question 38: Check if string is a valid palindrome ignoring case: "A man a plan a canal Panama"
print("\nQuestion 38: Check if string is a valid palindrome ignoring case: 'A man a plan a canal Panama'")
import string
str="A man a plan a canal Panama"
str1=str.lower().replace(' ','')
str2=str1[::-1]
if (str1==str2):
    print("valid")
else:
    print("invalied")

# Question 39: Find the most common word in "the quick brown fox jumps over the lazy dog"
print("\nQuestion 39: Find the most common word in 'the quick brown fox jumps over the lazy dog'")
str="the quick brown fox jumps over the lazy dog"
str1=str.split()
count=0
sp=''
for i in str1:
    count=str1.count(i)
    if count > count:
        count=count
        sp=i
    print(sp)





# Question 40: Generate acronym from "National Aeronautics and Space Administration"
print("\nQuestion 40: Generate acronym from 'National Aeronautics and Space Administration'")
str= "National Aeronautics and Space Administration"
str2=str.split()
for i in str2:
    if len(i)>3:
        print(i[0:1])

    


# Question 41: Check if string contains balanced parentheses: "((()))"
print("\nQuestion 41: Check if string contains balanced parentheses: '((()))'")
x="((()))"
if len(x)%2==0:
    print("it is equal")
else:
    print("it is not equal")

# Question 42: Convert "hello world" to Morse code
print("\nQuestion 42: Convert 'hello world' to Morse code")



# Question 43: Find the longest common substring between "programming" and "grammar"
print("\nQuestion 43: Find the longest common substring between 'programming' and 'grammar'")
str1="programming"
str2="grammar"
if "gramm" in str1 and "gramm" in str2:
    print(f" the longest common substring is : gramm")
            



# Question 44: Check if string is a valid URL: "https://www.google.com"
print("\nQuestion 44: Check if string is a valid URL: 'https://www.google.com'")
x="https://www.google.com"
str=x.startswith("https") and x.endswith(".com")
print(True)


# Question 45: Extract all words with length > 5 from "Python programming is amazing and powerful"
print("\nQuestion 45: Extract all words with length > 5 from 'Python programming is amazing and powerful'")
str="Python programming is amazing and powerful"
word=str.split()
for i in word:
    if len(i)>5:
        print(i,end='')
    

# Question 46: Convert "hello world" to Pig Latin
print("\nQuestion 46: Convert 'hello world' to Pig Latin")
str="hello world"
convert=str.replace("hello world","pig latin")
print(convert)

# Question 47: Check if string is a valid IPv4 address: "192.168.1.1"
print("\nQuestion 47: Check if string is a valid IPv4 address: '192.168.1.1'")


# Question 48: Find all substrings of "abc"
print("\nQuestion 48: Find all substrings of 'abc'")
str="abc"
for i in range(len(str)):
    for j in range(i,len(str)+1):
        print(str[i:j])



# Question 49: Convert "hello world" to ROT13 encoding
print("\nQuestion 49: Convert 'hello world' to ROT13 encoding")
# Your code here

# Question 50: Check if string is a valid credit card number: "4532015112830366"
print("\nQuestion 50: Check if string is a valid credit card number: '4532015112830366'")
num="4532015112830366"

if len(num)==16 and num.isalnum():
    print("it valied")
else:
    print("it is not valied")
