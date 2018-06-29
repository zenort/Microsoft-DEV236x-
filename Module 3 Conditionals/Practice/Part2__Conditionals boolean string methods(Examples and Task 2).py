# review code and run cell
favorite_book = input("Enter the title of a favorite book: ")

if favorite_book.istitle():
    print(favorite_book, "- nice capitalization in that title!")
else:
    print(favorite_book, "- consider capitalization throughout for book titles.")

# review code and run cell
a_number = input("enter a positive integer number: ")

if a_number.isdigit():
    print(a_number, "is a positive integer")
else:
    print(a_number, "is not a positive integer")


# another if
if a_number.isalpha():
    print(a_number, "is more like a word")
else:
    pass

# review code and run cell
vehicle_type = input('"enter a type of vehicle that starts with "P": ')

if vehicle_type.upper().startswith("P"):
    print(vehicle_type, 'starts with "P"')
else:
    print(vehicle_type, 'does not start with "P"')


print()

#Task 2 Multipart
test_string_1 = "welcome"
test_string_2 = "I have $3"
# [ ] use if, else to test for islower() for the 2 strings
if test_string_1.islower():
    print("la cadena de caracteres esta en minuscula")
else:
    print("no esta en minuscula")

if test_string_2.islower():
    print("la cadena de caracteres esta en minuscula")
else:
    print("no esta en minuscula")


#Task 2 continue
print()
test_string_1 = "welcome"
test_string_2 = "I have $3"
test_string_3 = "With a function it's efficient to repeat code"
# [ ] create a function w_start_test() use if & else to test with startswith('w')
# [ ] Test the 3 string variables provided by calling w_start_test()

def w_start_test(test):
    if test.startswith("W"):
         print(test, 'starts with "W"')
    else:
         print(test, 'does not start with "W"')

w_start_test(test_string_1)
w_start_test(test_string_2)
w_start_test(test_string_3)
