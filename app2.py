from my_funcs import introduction


print("The Wild")
name = input("What's your name: ")
print(f"{name} welcome to The Wild")
print("""
Menu:
1. Intro to Wildlife Conservation
2. Importance of Wildlife Conservation
3. Trivia Game
4. Exit

Select any option
""")

entry = ""

while True:
    entry = input("> ")
    if entry == "1":
        introduction()
    elif entry == "2":
        pass
    elif entry == "3":
        pass
    elif entry == "4":
        break
    else:
        print("""Please choose a valid option.
        Valid options are 1, 2, 3, 4""")
