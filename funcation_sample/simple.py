
# Write a function sum_all(*args) that returns the sum of all numbers passed.

def sum_all(*args):
    return sum(args)
x=sum_all(1,2,3,4,5,6,7,8,9)
print(f"funcation of sum all no:{x}")


# Write a function concat_strings(*args) that joins all string arguments into one string.

def concat_strings(*args):
    str = ''
    for i in args:
        str = str + i
    return (str)
y=concat_strings('gagan','reddy')
print(f"funcation concat strings :{y}")


def concat_strings(*args):
    str=''
    return str.join(args)
str2=concat_strings('cat','dog')
print(f"funcation concat strings using join: {str2}")

# Write a function max_number(*args) that returns the maximum value passed.

def max_number(*args):
    return max(args)
a=max_number(1,2,3,4,5,6,7,8,44,66,32,112)
print(f"funcation max no:{a}")

#Write a function unpack_args(*args)that takes nested lists/tuples and flattens them.





# What happens if you pass a list directly vs.using unpacking (*list) when calling a function with *args? Show with an example.
 
def data2(*args):
    return args
q=data2([1,2,3,4])
print(f"list directly args:{q}")

def data1(args):
    return args
d=data1([1,2,3,4])
print(f"calling a funcation *args:{d} ")


# Write a function reverse_args(*args)that prints arguments in reverse order.

def reverse_args(*args):
    return(args[::-1])
l=reverse_args(1,2,3,4,5,6)
print(f"unction reverse args:{l}")
