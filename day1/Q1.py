"""Write a program to swap two 
   variables without using a third variable."""

try:
    print("before swap")
    x = int(input("first number:"))
    y = int(input("second number:"))
    
   

    x = x^y 
    y = x^y 
    x = x^y

    print("after swap")

    print(f"first number is {x}")
    print(f"second number is {y}")
except:
  print("An exception occurred")