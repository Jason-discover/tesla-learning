"""for i in range(5):
    for j in range(5):
        print("1",end="")
    print()"""

"""for i in range(5):
    for j in range(1,6):
        print(j,end="")
    print()"""

"""for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()"""

"""for i in range(6,1,-1):
     for j in range(1,i):
         print(j,end="")
     print()"""

for i in range(6,1,-1):
    for j in range(i-1):
        print("*",end="")
    print()