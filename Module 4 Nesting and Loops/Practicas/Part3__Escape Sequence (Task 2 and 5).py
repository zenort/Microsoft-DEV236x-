print("It's" + "Python Time!")
print("It's\nPython Time!")
print("It's" + "\nPython Time!")
print("It\'s\nPython Time!")
#Task 2
#  [ ] create and test pre_word()
def pre_word(word):
    if word.isalpha()==word.startswith("pre"):
        return True
    else:
        return False

palabra=input("enter a word that starts with \"pre\": ")
if pre_word(palabra)==False:
    print("not a \"pre\" word")
else:
    print("is a valid \"pre\" word")



print("\n")
#Task 5
#Fix the Errors
# [ ] review, run, fix
print("Hello" + "\n" + "World!")


