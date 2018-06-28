# Message double returns the string Argument doubled
def msg_double(phrase):
      double = phrase + " " + phrase
      return double

# save return value in variable
msg_2x = msg_double("let's go")
print(msg_2x)

# example of functions with return values used in functions
def msg_double2(phrase):
      double = phrase + " " + phrase
      return double

# prints the returned object
print(msg_double2("Save Now!"))

# echo the type of the returned object
print (type(msg_double2("Save Now!")))


#Task 1
def make_doctor(name):
    return name


full_name= input("Introduce el nombre: ")
print (make_doctor(full_name))


print()


#Task 2
def make_schedule(period1, period2, period3):
    schedule = ("[1st] " + period1.title() + ", [2nd] " + period2.title() + ", [3nd] " + period3)
    return schedule

student_schedule = make_schedule("mathematics", "history", "science")
print("SCHEDULE:", student_schedule)