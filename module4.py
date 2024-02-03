def user_input():
	"""Input prompt"""

	# Printing statement to signal the user that we are waiting for input.
	user_input = input("Please type in your name\n")

	# Printing a message based on the input.
	print(f"Welcome, {user_input}!")

def main():

    user_input()

    # Ask user for input N
    N = int(input("Enter the number of elements (N): "))

    # Read N numbers from the user
    numbers = []
    for i in range(N):
        num = int(input("Enter number {}: ".format(i + 1)))
        numbers.append(num)

    # Ask user for input X
    X = int(input("Enter the number to search for (X): "))

    # Search for X in the list of numbers
    index = -1
    for i in range(N):
        if numbers[i] == X:
            index = i + 1
            break

    # Output the result
    if index == -1:
        print("-1")
    else:
        print("The number {} is found at index {}".format(X, index))


if __name__ == "__main__":
    main()
