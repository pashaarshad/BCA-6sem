# Forward Chaining Program

database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]

knowbase = ["Frog", "Canary", "Green", "Yellow"]


def display():

    print("\nX is")
    print("1. Croaks")
    print("2. Eat Flies")
    print("3. Shrimps")
    print("4. Sings")

    print("\nSelect One :", end=' ')


def main():

    print("*----- Forward Chaining -----*")

    display()

    x = int(input())

    print()

    # Rules
    if x == 1 or x == 2:
        print("Chance Of Frog")

    elif x == 3 or x == 4:
        print("Chance Of Canary")

    else:
        print("Invalid Option")

    # Knowledge Base Checking
    if x >= 1 and x <= 4:

        print("\nX is", database[x - 1])

        print("\nColor Is")
        print("1. Green")
        print("2. Yellow")

        print("\nSelect Option :", end=' ')

        k = int(input())

        # Frog + Green
        if k == 1 and (x == 1 or x == 2):

            print("\nYes it is", knowbase[0])
            print("And Color is", knowbase[2])

        # Canary + Yellow
        elif k == 2 and (x == 3 or x == 4):

            print("\nYes it is", knowbase[1])
            print("And Color is", knowbase[3])

        else:
            print("\nInvalid Knowledge Database")


if __name__ == "__main__":
    main()