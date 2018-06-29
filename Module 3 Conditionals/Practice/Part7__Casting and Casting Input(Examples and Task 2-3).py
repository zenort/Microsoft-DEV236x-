#Example

weight1 = '60' # a string
weight2 = 170 # an integer
# add 2 integers
total_weight = int(weight1) + weight2
print(total_weight)

print()


#Task 2
#casting with int() & str()
str_num_1 = "11"
str_num_2 = "15"
int_num_3 = 10
# [ ] Add the 3 numbers as integers and print the result
result=int(str_num_1)+int(str_num_2)+int_num_3
print(result)

print()
#Task 2 Continue...
# [ ] code and test: adding using int casting
str_integer = "2"
int_number = 10
number_total = int(str_integer) + int_number
print(number_total)


print()
#Example: Concept: Casting Numeric Input

# [ ] review and run code
student_age = input('enter student age (integer): ')
age_next_year = int(student_age) + 1
print('Next year student will be',age_next_year)
# [ ] review and run code

# cast to int at input
student_age = int(input('enter student age (integer): '))

age_in_decade = student_age + 10

print('In a decade the student will be', age_in_decade)


print()
#Task 3
#Program: adding calculator
num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))
result=num1+num2
print("El resultado es: " +str(result))

