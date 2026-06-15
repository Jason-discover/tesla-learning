# for i in range(5):
#     print(i)

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

i = 1
j = 1
while i <=5:
    while j<=5:
        print(str(j)*i, end="")
        j += 1
        break
    print()
    i += 1