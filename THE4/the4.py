def is_valid(T,D,S):
	i=0
	Tlist=inorder(T).split(" ")
	Tlist=Tlist[:-1]
	Tlist=lower1(Tlist)
	D=lower2(D,0)
	gram=control(Tlist,D,[])
	D=lower3(D,gram)
	mar=S.lower()
	mar=mar.split(" ")
	while i<(len(mar)):
		if len(gram)!=len(mar):
			return False
		elif mar[i] in D[gram[i]]:
			i=i+1
		else:
			return False
	return True

def lower1(Tlist):
	z=0
	while z<(len(Tlist)):
		Tlist[z]=Tlist[z].lower()
		z=z+1
	return Tlist

def lower2(D,z):
	if z==len(D):
		return D
	else:
		a=D.keys()[z].lower()
		D[a]=D.pop(D.keys()[z])
		del a
		return lower2(D,z+1)

def lower3(D,gram):
	u=0
	while u<(len(gram)):
		j=0
		while j<len(D[gram[u]]):
			D[gram[u]][j]=D[gram[u]][j].lower()
			j=j+1
		u=u+1
	return D

def control(Tlist,D,Tll):
	if Tlist==[]:
		return Tll
	elif Tlist[0] in D:
		Tll.append(Tlist[0])
		return control(Tlist[1:],D,Tll)
	elif Tlist[0] not in D:
		return control(Tlist[1:],D,Tll)
		
def inorder(tree):
	if tree==[]:
		return ""
	elif len(tree)==1:
		return str(tree[0])+ " "
	elif len(tree)==2:
		return inorder(tree[1]) + str(tree[0])+ " "
	else:
		return helpyaa(tree)

def helpyaa(tree):
	x=inorder(tree[1]) + str(tree[0])+ " "
	n=2
	while n<len(tree):
		x = x+inorder(tree[n])
		n = n+1
	return x
