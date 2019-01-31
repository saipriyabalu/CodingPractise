# 1. Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

def check(st):
	l=[]
	for i in st:
		if i not in l:
			l.append(i)
			flag=1
		else:
			flag=0
	if(flag==1):
		return "unique"
	else:
		return "not unique"



print(check(raw_input()))
