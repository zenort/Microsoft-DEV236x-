def hat_available(color):
    hat_colors = 'black, red, blue, green, white, grey, brown, pink'
    return (color.lower() in hat_colors)


have_hat = hat_available('green')

print('hat available is', have_hat)

print()


#funcion prueba Pajaro_disponibilidad
def parajaro_disponible(pajaro):
    bird_types = 'crow robin parrot eagle sandpiper hawk pigeon'
    return (pajaro.lower() in bird_types)

pajaro = input('Introduce raza de pajaro en ingles: ')

print("El pajaro esta: ", parajaro_disponible(pajaro))

print()

#TASK3 Fix The Error
# define function how_many
def how_many():
    requested = input("enter how many you want: ")
    return requested

# get the number_needed
number_needed = how_many()
print(number_needed, "will be ordered")
