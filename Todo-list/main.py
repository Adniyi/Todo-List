print("Welcome to My Todo list Project")
def todo():
    list = []
    while True:
        a = input("Would you like to make an Entry (y) or (n): ")

        if a.lower() == "y":
            e = input("Make an Entry: ")
            list.append(e)
            print(list)

        elif a.lower() == "n":
            b = input("Would you like to Delete an Entry (y) or (no): ")

            if b.lower() =="y":
                f = input("Enter the Entry: ")
                list.remove(f)
                print(list)
            else:
                print("No Entry Found")
        else:
            break



Todo = todo()
print("Hope you enjoyed my little Project")

