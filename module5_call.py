from module5_mod import FindNumber


def main():
    tracker = FindNumber()

    N = int(input("Enter the number of elements: "))
    for i in range(N):
        num = int(input("Enter number {}: ".format(i + 1)))
        tracker.insert_number(num)

    X = int(input("Enter the number to search for: "))


    result = tracker.search_number(X)

    if result == -1:
        print("-1")
    else:
        print("Index of {}: {}".format(X, result))


if __name__ == "__main__":
    main()