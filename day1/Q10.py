"""
Create a CLI calculator that performs basic
arithmetic operations based on user input with input validation.
"""


print("CLI calculator")

print("\n1.Add 2.Sub 3.Mul 4.Div\n")
choice = int(input("choose a option:"))

if choice == 1:
    n1 = float(input("Num 1:"))
    n2 = float(input("Num 2:"))
    print(n1+n2)
elif choice == 2:
    n1 = float(input("Num 1:"))
    n2 = float(input("Num 2:"))
    print(n1-n2)
elif choice == 3:
    n1 = float(input("Num 1:"))
    n2 = float(input("Num 2:"))
    print(n1*n2)
elif choice == 4:
    n1 = float(input("Num 1:"))
    n2 = float(input("Num 2:"))
    if n2 == 0:
        print("undefined")
    else:
        print(n1/n2)
else: 
    print("Invalid choice")