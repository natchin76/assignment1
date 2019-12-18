#function that adds arbitrary nos
def add(*args):
	s=0
	for i in args:
		s+=i
	return(s)
a=add(1,2,3,4)
print(a)			
	
