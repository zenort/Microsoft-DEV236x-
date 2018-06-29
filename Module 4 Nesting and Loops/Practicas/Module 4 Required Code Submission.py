#Module 4 Final

def str_analysis(something):
    if something.isdigit():
        if int(something) >99:
            print(something, "is pretty big number!")
        else:
            print(something, "is a smaller number than expected")
    elif something.isalpha():
        print("\""+something+"\" is all alphabetical characters!")
    else:
        print("\""+something+"\" is a sorprise! It's neither all alpha nor all digit charcters!")


test=input("enter word or integer: ")

while test=="":
      test=input("enter word or integer: ")

str_analysis(test)