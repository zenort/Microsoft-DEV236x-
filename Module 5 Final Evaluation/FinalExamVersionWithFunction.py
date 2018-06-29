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


def adding_report(report):
    if report== "A":
        print("\nItems")
        print(items)
        print("Total")
        print(total)
    elif report == "T":
        print("\nTotal")
        print(total)

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
            adding_report(respuestaAT)
        elif respuestaAT=="T":
            adding_report(respuestaAT)
        break
    elif item=="":
        pass
    else:
        print(item, "is invalid input")



