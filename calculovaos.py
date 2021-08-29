x=eval(input("Medida do material do quadro?"))
w=eval(input("Medida do material a ser colocado no meio?"))
y=eval(input("Medida interna do quadro?"))
c=eval(input("Medida aproximada do vão?"))
v= c+w
b= (y+w)//v
print("Vão mais material: ", y+w)
if (b//1 == b):
	u=b
else:
	u=b+1
print("Quantidade de vãos: ",u)
z= (y+w)/u
print("Medida do vão: ",z)
a= w+y

while x < a:
	x = x+z
	print(x)