# Backward Chaining using ABCD

database = ["A", "B", "C", "D"]

def main():

    print("*----- Backward Chaining -----*")

    goal = input("\nEnter Goal : ")

    print()

    # Backward Rules
    if goal == "D":

        print("D <- C")
        print("C <- B")
        print("B <- A")

        print("\nGoal Achieved")

    elif goal == "C":

        print("C <- B")
        print("B <- A")

        print("\nGoal Achieved")

    elif goal == "B":

        print("B <- A")

        print("\nGoal Achieved")

    elif goal == "A":

        print("A is the Initial Fact")

    else:

        print("Invalid Goal")


if __name__ == "__main__":
    main()