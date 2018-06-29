total = 0
items = ""

while True:
    respuestaAT = input("Choose Report Type (\"A\" or \"T\"): ")
    if respuestaAT=="A":
        break
    elif respuestaAT=="T":
        break
    else:
        print(respuestaAT, "is invalid input")

print("Input an integer to add to the total or \"Q\" to quit")
while True:
    item=input("Enter an integer or \"Q\": ")
    if item.isdigit():
        if respuestaAT=="A":
            items = items + item + "\n"
            total = total + int(item)
        elif respuestaAT=="T":
            items = items + item + "\n"
            total = total + int(item)
    elif item.startswith("Q"):
        if respuestaAT=="A":
            print("\nItems")
            print(items)
            print("Total")
            print(total)
        elif respuestaAT=="T":
            print("\nTotal")
            print(total)
        break
    elif item=="":
        pass
    else:
        print(item, "is invalid input")



