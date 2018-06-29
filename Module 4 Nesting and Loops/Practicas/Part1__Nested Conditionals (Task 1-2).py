#Task 1 Say "Hello"
pregunta=input("Say Hello? ")
if pregunta =="Hello":
    pregunta2=input("Say Hello: ")
    if pregunta2=="Hello":
        print("Hello")
    else:
        print("Hi")
else:
    print("(frendly nod)")


print()
print()


#Task 2 Guess bird
bird_guess=input("Adivina (1 intento) el pajaro: ")
bird_names="Paloma, Halcon, Colibri"
if bird_guess in bird_names:
    print("Yes 1 try!")
else:
    bird_guess=input("Adivida (2 intento) el pajaro: ")
    if bird_guess in bird_names:
        print("Yes 2 try!")
    else:
        bird_guess = input("Adivida (3 intento) el pajaro: ")
        if bird_guess in bird_names:
            print("Yes 3 try!")
        else:
            print("Sorry, out of tries")
