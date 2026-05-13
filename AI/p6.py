# Forward Chaining using ABCD

database = ["A", "B", "C", "D"]

def display():

    print("\n1. A")
    print("2. B")
    print("3. C")
    print("4. D")

    print("\nSelect One :", end=' ')


def main():

    print("*----- Forward Chaining -----*")

    display()

    x = int(input())

    print()

    # Rules
    if x == 1:
        print("A -> B")

    elif x == 2:
        print("B -> C")

    elif x == 3:
        print("C -> D")

    elif x == 4:
        print("Goal Reached : D")

    else:
        print("Invalid Option")

    # Display selected value
    if x >= 1 and x <= 4:

        print("\nSelected :", database[x - 1])


if __name__ == "__main__":
    main()