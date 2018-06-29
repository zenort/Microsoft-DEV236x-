#Task 2
long_num=""
int_num=input("Introduce el primer numero: ")

while int_num.isdigit() ==True:
    long_num=long_num+int_num
    int_num = input("Introduce otro numero: ")

print("Long num:" +long_num)



print("\n")
#Task 3
# [ ] review the code, run, fix the Logic error

count = 1

# loop 5 times
while count < 6:
    print(count, "x", count, "=", count*count)
    count +=1



