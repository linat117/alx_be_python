number = int(input("Enter a number to see its multiplication table: "))
product = 0
for numbers in range(1, 11):
    product = numbers * number
    print(f"{number} * {numbers} = {product}")

