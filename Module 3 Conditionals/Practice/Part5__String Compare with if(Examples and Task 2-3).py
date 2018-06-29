#Examples: Concept: String Comparison with if

# [ ] review and run code
msg = "Save the notebook"

if msg.lower() == "save the notebook":
    print("message as expected")
else:
    print("message not as expected")
# [ ] review and run code
msg = "Save the notebook"
prediction = "save the notebook"

if msg.lower() == prediction.lower():
    print("message as expected")
else:
    print("message not as expected")

print()

#Task 2: Conditionals: comparison operators with if
# [ ] get input for a variable, answer, and ask user 'What is 8 + 13? : '
# [ ] print messages for correct answer "21" or incorrect answer using if/else
# note: input returns a "string"
answer=input("What is 8 + 13: ")
if answer =="21":
    print("Verdadero")
else:
    print("Falso")


print()
#Task3 Program: True False Quiz Function
#Call the tf_quiz function with 2 arguments
#T/F question string
#answer key string like "T"
#Return a string: "correct" or incorrect"

def tf_quiz(question, correct_ans):
    respuesta=input(question + "(T/F): ")
    if correct_ans ==respuesta:
        return "correcto"
    else:
        return "incorrecto"

quiz_eval=tf_quiz("El dragon tiene dos cabezas ", "F")
print("tu espuesta es", quiz_eval)