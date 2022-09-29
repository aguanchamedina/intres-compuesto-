print("---------------------------------")
print("--------INTERES COMPUESTO-------")
print("---------------------------------")

#INPUT
C = int(input("Digite el valor de C: "))

#PROCESS
B = 2 * C 
N = 0 
while C < B: 
    C = 1.05 *C 
    N = N + 1 
    

     
    
#OUTPUT

print("El interes compuesto es de: " + str(N)) 
