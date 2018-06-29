numero=float(input("Enter cheese order weight (numeric value): "))
if numero >=100:
    print(numero, "is more than currently available stock")
elif numero <=0.25:
    print(numero, "is below minimum order amount")
else:
    costs=numero*8
    print(numero, "costs $"+str(costs))


