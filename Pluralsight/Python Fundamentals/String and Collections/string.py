# string with escape sequence
print('C:\deepa\newbook')
print()
# use of r operator
print(r'C:\deepa\newbook')
print()

# Multilines string
a = """This is a 
multiline 
string"""
print(a)
print()

# tabbed string
a = "This is string 	contains	tab	character"	 
print(a)
print()

# Encoding and Decoding
a = "intérêt"
b = a.encode("utf-8")
c = b.decode("utf-8")

print("String a is :{0} is of type :{1}".format(a,type(a)))
print("String b is :{0} is of type :{1}".format(b,type(b)))
print("String c is :{0} is of type :{1}".format(c,type(c)))

if a == c:
    print("strings a and c are equal")

