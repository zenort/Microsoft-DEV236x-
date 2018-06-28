def fish_store(fish_name, fish_price):
    mensaje = "Fish Type: " +fish_name + " costs $" +fish_price
    return mensaje


enter_name= input('enter fish name: ')
enter_price= input('enter the fish price (no symbols): ')

print (fish_store(enter_name, enter_price))
