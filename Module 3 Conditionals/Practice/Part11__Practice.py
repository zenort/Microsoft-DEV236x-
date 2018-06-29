#Practice
# [ ] input a variable: age as digit and cast to int

age=int(input("Cual es tu edad? "))
if age >= 12:
    print("On age in 10 years")
else:
    print("It is good to be " +str(age))


# [ ] input a number
numero=input("Introduce un numero: ")
if numero.isdigit()==True:

    print("casting int realizado y es:", int(numero))
    if int(numero)>100:
        print("greater than 100 is", int(numero)>100)
    else:
        pass
else:
    print("only int is accepted")
