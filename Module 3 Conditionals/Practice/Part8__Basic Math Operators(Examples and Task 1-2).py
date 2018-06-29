#Example
# [ ] review and run example
print("3 + 5 =",3 + 5)
print("3 + 5 - 9 =", 3 + 5 - 9)
print("48/9 =", 48/9)
print("5*5 =", 5*5)
print("(14 - 8)*(19/4) =", (14 - 8)*(19/4))
# [ ] review and run example - 'million_maker'
def million_maker():
    make_big = input("enter a non-decimal number you wish were bigger: ")
    return int(make_big)*1000000

print("Now you have", million_maker())

print()

#Task 1
# [ ] print the result of subtracting 15 from 43
print("15-43 =", 15-43)

# [ ] print the result of multiplying 15 and 43
print("15*43=", 15*43)

# [ ] print the result of dividing 156 by 12
print("156/12=", 156/12)

# [ ] print the result of dividing 21 by 0.5
print("21/0.5=", 21/0.5)

# [ ] print the result of adding 111 plus 84 and then subtracting 45
print("111+84-45 =", 111+84-45)

# [ ] print the result of adding 21 and 4 and then multiplying that sum by 4
print("(21+4)*4=", (21+4)*4)

print()


#Task 2
## [ ] create and test multiply() function

def multiply(num1, num2):
    result=num1*num2
    return str(result)

numero1=int(input("Introduce el primer numero a multiplicar: "))
numero2=int(input("Introduce el segundo numero a multiplicar: "))
print("El resultado de la multiplicacion: " +multiply(numero1, numero2))
