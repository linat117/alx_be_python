user_input = int(input("Enter the size of the pattern:"))
row=1
while row <= user_input:
    for asterix in range(user_input):
        print("*", end="")
    print()
    row = row +1
