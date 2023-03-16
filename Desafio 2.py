import math

numero = int(input("Digite um número para saber se faz parte da sequencia Fibonacci: "))
calc1 = 5*(numero**2) - 4
calc2 = 5*(numero**2) + 4

if (int(math.sqrt(calc1))*int(math.sqrt(calc1))) == calc1 or (int(math.sqrt(calc2))*int(math.sqrt(calc2)) == calc2):

    print("O número", numero, "faz parte da sequencia Fibonacci!")
       

else:
    
    print("O número", numero, "não faz parte da sequencia Fibonacci!")
   