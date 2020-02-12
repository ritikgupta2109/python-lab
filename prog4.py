l1 = [1,3,3,5,57,8,46,5,77,57,]
l2 = [1,2,345,477,5,6,78,979,3,5]
l = [l1.append(i) for i in l2 if i not in l1]
print(l1)
