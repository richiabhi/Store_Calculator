s = 0
print("Welcome to Store Calculator Enter the prices to add or 'q' to exit")
while (True):
    entry = input("Enter the item price : ")
    if (entry != 'q'):
        s = s + int(entry)
        print(f"Order Total is Rs.{s}")

    else:
        print(f"Your bill total is Rs.{s}, Thanks for visiting us")
        break
