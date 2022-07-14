from functions import introduction, importance, involve


print("The Wild")
print("----------------------------------------")
name = input("What's your name: ")
print(f"{name} welcome to The Wild")
print("""
Menu:
1. Intro to Wildlife Conservation
2. Importance of Wildlife Conservation
3. How to get involved in wildlife conservation
4. Triva Quiz
5. Exit

Select any option
""")
print("-----------------------------------------")

entry = ""

while True:
    entry = input("> ")
    if entry == "1":
        introduction()
    elif entry == "2":
        importance()
    elif entry == "3":
        involve()
    elif entry == "4":
        pass
    elif entry == "5":
        break
    else:
        print("""Please choose a valid option.
        Valid options are 1, 2, 3, 4, 5""")
