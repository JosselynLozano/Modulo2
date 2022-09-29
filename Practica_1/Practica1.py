import sys

print ("Iniciado")
x = int(sys.argv[1])
#y = x + 1
lista = []

def lista1(y):
    for i in range(1,y):
        print(i, end=", ")
        lista.append(i)
    return lista

def numeros_primos(y):
    cont = 0
    for i in range(2,y):
        primos = True
        for j in range(2,i):
            if i == j:
               break
            elif i%j == 0:
               primos = False
            else:
               continue
        if primos == True:
            print(i, end=", ")
            cont += 1   
    return lista
    
print ("Lista creada: ")
lista1(x + 1)
print ("\n")
print("Números primos:")
numeros_primos(x + 1)
print ("\n")
print("Fin\n")