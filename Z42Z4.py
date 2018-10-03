from Sumamodulon import sumamod,prodmod
#from gasp import *

print ("Ring of upper triangular matrices Z_4 & 2Z_4 \\ 0 & Z_4")
Z=[0,1,2,3]
Z2=[0,2]

R1=[]
for x in Z:
	for y in Z2:
		R1.append([x,y])

R2=[]
for x in Z:
	R2.append([0,x])


R=[]
for x in R1:
	for y in R2:
		R.append([x,y])

print "R=" + str(R)
print len(R)

def suma(x,y):
	m = sumamod(x[0][0],y[0][0],4)
	n = sumamod(x[0][1],y[0][1],4)
	w = [m,n]
	return [w,[0,sumamod(x[1][1],y[1][1],4)]]

def prod(x,y):
	z = prodmod(x[0][0],y[0][1],4)
	v = prodmod(x[0][1],y[1][1],4)
	s = sumamod(z,v,4)
	return [[prodmod(x[0][0],y[0][0],4),s],[0,prodmod(x[1][1],y[1][1],4)]]

def cicl(y):
	C=[]
	for x in R:
		if prod(x,y) not in C:
			C.append(prod(x,y))
	return C 

K = []
for x in R:
	if all(y in cicl(x) for y in R) == False:
		K.append(x)

K.remove([[0,0],[0,0]])

for k in K:
	for j in K:
		if j!=k and all(v in cicl(k) for v in cicl(j)) and all(u in cicl(j) for u in cicl(k)):
			K.remove(j)

for k in K:
	for j in K:
		if j!=k and all(v in cicl(k) for v in cicl(j)) and all(u in cicl(j) for u in cicl(k)):
			K.remove(j)

#print("Hay %s ideales ciclicos no triviales" %(len(K)))

## Conjunto de Ideales ciclicos

CLC=[]
for k in K:
	CLC.append(cicl(k))

## Atomos de la reticula de ideales
AT=[]
for I in CLC[:]:
	CLC.remove(I)
	if all(all(j in I for j in J)==False for J in CLC):
		AT.append(I)
		CLC.insert(0,I)
	else:
		CLC.insert(0,I)

#print("Los atomos de la reticula de ideales son:")
#for A in AT:
#	print (A)

##### Ideals sum function

def sumaide(I,J):
	if I!=J:
		#if all(v in I for v in J) or all(u in J for u in I):
		#	return("Uno esta contenido en el otro")
		#else:
		S=[]	
		for h in I:
			for j in J:
				if suma(h,j) not in S:
					S.append(suma(h,j))
		return S
	else:
		return I

##### Calculamos todos los ideales
for I in CLC:
	I.sort()

a, b= 0, 1
while a<b:
	a = len(CLC)
	for I in CLC[:]:
		for J in CLC:
			G = sumaide(I,J)
			G.sort()
			if G not in CLC:
				CLC.append(G)
	b= len(CLC)
if R not in CLC:
	print 'Hay ',len(CLC),' ideales propios'
else:
	print 'Hay en total ',len(CLC)+2,' ideales'

print "Los estratos de la reticula (primero los atomos y al final los maximos)"

if R in CLC:
	CLC.remove(R)
Sub=[]
for I in CLC:
	Sub.append(I)

while len(CLC)>0:
	AT=[]
	for I in CLC[:]:
		CLC.remove(I)
		if all(all(j in I for j in J)==False for J in CLC):
			AT.append(I)
			CLC.insert(0,I)
		else:
			CLC.insert(0,I)
	print len(AT)
	for A in AT:
		print A
		CLC.remove(A)


Bil=[]
for I in Sub:
	if all(all(prod(i,m) in I for m in R) for i in I):
		Bil.append(I)

print 'Hay ',len(Bil),' ideales bilaterales propios'



#### The funtion aRb and the prime ideals

def aRb(x,y):
	S=[]
	for z in R:
		c=prod(x,(prod(z,y)))
		S.append(c)
	return S

MM=[]
for x in R:
	for y in R:
		MM.append([x,y])

MZ=[]
for x in MM:
	if x[0] == [[0,0],[0,0]] or x[1] == [[0,0],[0,0]]:
		continue
	else:
		MZ.append(x)

#print MZ
####print "The prime ideals are:"

for I in Bil:
	L=[]
	for x in MZ:
		if all(y in I for y in aRb(x[0],x[1]))==True:
			L.append(x)
	if L==[]:
		print "No fue primo"
	elif all((z[0] in I or z[1] in I) for z in L)==True:
		print I 
	else:
		print "No fue primo jaja"



#print 'Los estratos de la reticula de ideales bilaterales son:'

#while len(Bil)>0:
#	AT=[]
#	for I in Bil[:]:
#		Bil.remove(I)
#		if all(all(j in I for j in J)==False for J in Bil):
#			AT.append(I)
#			Bil.insert(0,I)
#		else:
#			Bil.insert(0,I)
#	print len(AT)
#	for A in AT:
#		print A
#		Bil.remove(A)
#
######## Zero-divisors and Regular elements

def zero(x):
	Z=[]
	for y in R:
		if prod(x,y)==[[0,0],[0,0]]:
			Z.append(y)
	return Z

G=[]
for x in R:
	if x != [[0,0],[0,0]]:
		G = G+zero(x)

#print G

Reg=[]
for x in R:
	if (x in G)==False:
		Reg.append(x)

print "These are the regular elements of the ring"
print len(Reg)
print Reg

ZD=[] 
for x in R:
	if (x in Reg)==False:
		ZD.append(x)

print "These are the zero divisors of the ring"
print len(ZD)
print ZD

