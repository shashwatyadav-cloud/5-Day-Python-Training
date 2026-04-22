"""
Environment Configuration Script
Build a Python script that automates the developer environment setup process. This simulates real-world scenarios where developers need to configure their local environment.

Requirements:

Check if Python is installed and print version
Validate Python version (must be 3.8 or higher)
Create a project directory structure (src/, tests/, docs/, logs/)
Generate a requirements.txt file with basic packages
Create a .gitignore file with common Python patterns
Print a summary report with colored output (use ANSI escape codes)
Handle errors gracefully with try-except blocks.

"""



import sys
from pathlib import Path

try:
    print("Python version:", sys.version)

    # Check for version
    print("Python version:", sys.version_info.major,sys.version_info.minor,sys.version_info.micro)

    if sys.version_info >= (3, 8):
        print("Python version is valid")
    else:
        print("Older version")
        sys.exit()



    # Create a project directory structure (src/, tests/, docs/, logs/)

    Path("project/src").mkdir(parents=True, exist_ok=True)
    Path("project/tests").mkdir(parents=True, exist_ok=True)
    Path("project/docs").mkdir(parents=True, exist_ok=True)
    Path("project/logs").mkdir(parents=True, exist_ok=True)

    with open("requirements.txt", "w") as f:
        f.write("numpy\npandas\n")




    with open(".gitignore", "w") as f:
        f.write(".env")


    GREEN = "\033[92m"
    RESET = "\033[0m"
    print(GREEN + "✔ Python version checked")
    print(GREEN + "✔ Version validation done")
    print(GREEN + "✔ Project folders created")
    print(GREEN + "✔ requirements.txt created")
    print(GREEN + "✔ .gitignore created")

except Exception as e:
    print("Error:",e)



