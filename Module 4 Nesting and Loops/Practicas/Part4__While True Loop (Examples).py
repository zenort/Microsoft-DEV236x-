#Example
#while True loops forever unless a break statement is used

# Review and run code
# this example never loops because the break has no conditions
while True:
    print('write forever, unless there is a "break"')
    break #sin este "break" el  bucle seguiria ifinitamente


# [ ] review the NUMBER GUESS code then run - Q. what cause the break statement to run?
number_guess = "0"
secret_number = "5"

while True:
    number_guess = input("guess the number 1 to 5: ")
    if number_guess == secret_number:
        print("Yes", number_guess,"is correct!\n")
        break
    else:
        print(number_guess,"is incorrect\n")


# [ ] review WHAT TO WEAR code then run testing different inputs
while True:
    weather = input("Enter weather (sunny, rainy, snowy, or quit): ")
    print()

    if weather.lower() == "sunny":
        print("Wear a t-shirt and sunscreen")
        break
    elif weather.lower() == "rainy":
        print("Bring an umbrella and boots")
        break
    elif weather.lower() == "snowy":
        print("Wear a warm coat and hat")
        break
    elif weather.lower().startswith("q"):
        print('"quit" detected, exiting')
        break
    else:
        print("Sorry, not sure what to suggest for", weather +"\n")
