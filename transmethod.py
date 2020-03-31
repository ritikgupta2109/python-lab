#python 3.7.1

a = 'abcdef'
b = '123456'
trans = 'rk'.maketrans(a,b)

k='this is python class at 10:40 AM'
out=k.translate(trans)
print(out)