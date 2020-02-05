ls=[]
for i in range(100):
	a=input()
	if a=='':
		print(ls)
		break
	else:
		print(ls.append(a))
ls.sort()
print(ls[-1])
