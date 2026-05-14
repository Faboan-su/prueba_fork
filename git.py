a=2
b=1
c=[1,2,3,4,5]
resultado=a+b
print(resultado)
for i in c:
    print(i)
regla="tres simples"
print(regla)
#se puede hacer algo aca pero no se que

#hola soy nuevo y trabajo aqui
for i in range(1,5):
    print("*"*i)
    for j in range(1,5):
        print("*"*j)
        
#par o impar
x=int(input("introduce numero:"))
if x==0:
    print("Numero invalido")
elif(x%2==0):
    print("par")
else:
    print("impar")
#ccuenta del 10 al 1
i=10
while i>0:
    print(i)
    i-=1
    