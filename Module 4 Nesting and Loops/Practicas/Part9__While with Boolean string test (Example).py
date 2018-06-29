#Example
# review and run example that loops until a valid first name format is entered
student_fname = ""
while student_fname.isalpha() == False:
    student_fname = input("enter student\'s first (Letters only, No spaces): ")
print("\n" + student_fname.title(),"has been entered as first name")