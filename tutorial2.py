"""put in there
multiple lines
of comments
"""
#input
inp=input("Enter something")
"""by deafult input is always of type string"""
print(type(inp))
# keywords
"""int
float
def
if
else
elif
while
for
in
True
False
None
and aka &
or aka !!
not aka !="""
#indentation
"""def is a key word"""
a=1
b=2
if(b>a):
    print("b is greater than a")
else:
    print("a is greater than b")
#operators
"""+
-
*
= # assignment opreator
/ #quotient
// # floor division
% #remainder 

!= # not eqal to
"""
var=3
comp=3
if(var!=comp):
    print("var is not equal to comp")
elif(var==comp):
    print("var is equal to comp")
# if there is a situation of specifying three or more conditions we 
# use elif if there are only two conditions we can simply use if , else.



#logical operators
#bitwise operators
#assignment operators
"""= # a=5 etc"""
#comparison operators
"""< # less than
> # greater than
<= # less than or equal to
>= # greater tha or equal to
"""
#identity operators

#if statements
#swapping
a=5
b=6
"""for swapping manually
c=a
a=b
b=c"""
print(a,b)
a,b=b,a
print(a,b)


#definitions aka functions
#predifined functions/definitions
"""abs()
all()
any()
ascii()
bin()
bool()
bytearray()
bytes()
callable()
chr()
classmethod()
compile()
complex()
delattr()
dict()
dir()
divmod()
enumerate()
eval()
exec()
filter()
float()
format()
frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex()
id()
input()
int()
isinstance()
issubclass()
iter()
len()
list()
locals()
map()
max()
memoryview()
min()
next()
object()
oct()
open()
ord()
pow()
print()
property()
range()
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()"""
#user defined functions 
#functions without parameters and without return type
def func():
    print("hello")
    print("world")
#functions with parameters and without return type
"""a and b are parameters"""
def func(a,b):
    print(a+b)
    print(b-a)
#function overriding
func(10,20) # function call with parameters
#functions with parameters and with return type
def func1(a,b):
    return a+b
"""print(func1(12,22))"""
ret=func1(12,22)
print(ret)
#functions without parameters and with return type
def func2():
    s="hello"
    d="world"
    return s+d
print(func2())
# rew=func2()
# print(rew)
#loops
#incrementing
#decrementing
