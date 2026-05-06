# Check if a given string is a palindrome (case-insensitive).

s = input("Enter a string:")





if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")