s="mumbai"
a=[]
#using for loop
for i in s:
	a.append(ord(i))
print("for loop:",a)
#list comprehension
a=[ord(i) for i in s]
print("list comprehension",a)
#map
x=map(lambda i:ord(i),s)
print("map:",list(x))
	
