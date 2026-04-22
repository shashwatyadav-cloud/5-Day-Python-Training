# Convert temperature from Celsius to Fahrenheit and vice versa


print("option 1: celsius to Fahrenheit")
print("option 2: Fahrenheit to celsius")
option = int(input("choose a option:"))


if option == 1:
    temp = int(input("give a temprature to convert from celsius to Fahrenheit:"))
    new_temp = ((temp*9)/5)+32
    print(f'temprature in Fahrenheit is {new_temp}')
elif option == 2:
    temp = int(input("give a temprature to convert from Fahrenheit to celsius:"))
    new_temp = ((temp-32)*5)/9
    print(f'temprature in celsius is {new_temp}')
else:
    print("invalid option")



