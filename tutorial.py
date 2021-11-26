# variables
#data types
#string
name="Nikhil"
name1="Ankit"
name2="123"
inte=int(name2) #type conversion
print(name2+name2) #concatenation
print(inte+inte) #adding
#integer
a=5
b=-5
print(a+b)
#float
f=5.5
d=8.9
print(f+d)
#boolean
c=True
d=False
print(c+d) #boolean addition
print(c*d) #boolean multiplication
#list are mutable
l=[1,2,3,4,5]
print(l[2]) #indexing
l.append(6) #appending in the ending
print(l)
# l[1] = 10 #replacing
print(l)
# l.insert(1,20) #inserting
print(l)
print(l[1:3]) #slicing
print(l[1:]) #slicing
print(l[:3]) #slicing
#tuple
t=(6,7,8,9,10)
print(t[2])
print(t[1:3]) #slicing
print(t[1:]) #slicing
print(t[:3]) #slicing
#dictionary
d={'name':'Nikhil','age':'20','city':'Pune'}
print(d['name'])
r=["name","age","city"]
for i in r:
    print(i)
