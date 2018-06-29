#Example
# review and run GREET COUNT
greet_count = 5

# loop while count is greater than 0
while greet_count > 0:
    print(greet_count, "!")
    greet_count -= 1
print("\nIGNITION!")


print("\n")


#Task 1 Program: Animal Names
animal_count=0
nombre_temporal=""
nombre_final=""

while animal_count <4:
    animal_names=input("Introduce nombre de animal: ")
    if animal_names=="exit":
        break
    elif animal_names=="":
        animal_count += 1
        if animal_count ==4:
            print("No animals!!!")
        else:
            pass
    else:
        nombre_final=nombre_temporal+animal_names+", "
        nombre_temporal=nombre_final
        animal_count +=1

print("La lista de animales al completo: " +nombre_final)
