#Task 2
# [ ] Create the Shirt Count program, run tests
#enter a sizes (S, M, L)

size_s=0
size_m=0
size_l=0

s_cost= 2
m_cost= 4
l_cost= 6

while True:
    size=input("Introduce el tamaño (S,M,L) or \"exit\" (to finish):")
    if size.lower()=="s":
        size_s +=1
        s_cost = s_cost+2
    elif size.lower()=="m":
        size_m +=1
        m_cost=m_cost+4
    elif size.lower()== "l":
        size_l=size_l+1
        l_cost=l_cost+6
    elif size.lower().startswith("e"):
        total_cost=s_cost+m_cost+l_cost
        print()
        break
    else:
        pass

print("S:", size_s, "M:", size_m, "L:", size_l)
print("Cost of S:", s_cost, "M:", m_cost, "L:", l_cost)
print("Precio total:", total_cost)
