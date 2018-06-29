#Task 3
# [ ] create improved multiply() function and test with /, no argument, and an invalid operator ($)
def multiply(num1, multdiv, num2):

    if multdiv=="*":
        result=num1*num2
    elif multdiv=="/":
        result=num1/num2
    else:
        result=print("Invalid Operator")

    return str(result)


numero1=int(input("Introduce el primer numero a multiplicar: "))
multdiv=input("Multiplicar o Dividir (* o /): ")
numero2=int(input("Introduce el segundo numero a multiplicar: "))
print("El resultado de la multiplicacion: " +multiply(numero1, multdiv, numero2))


