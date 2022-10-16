"""A document to test functions that I can recycle in other files."""


def type_check(choice_list: list) -> int:
    """A function to ensure that the user inputs an integer within correct bounds."""
    number_of_options: int = 0
    for i in choice_list:
        print(i)
        number_of_options += 1
    selection: str = input("Select the number of your choice, or type 'quit' to exit the program: ")
    if selection == "quit":
        exit()
    try:
        selection = int(selection)
        if selection > 0 and selection <= number_of_options:
            return selection
        else:
            print("Choose a valid choice!")
            return type_check(choice_list)
    except ValueError:
        print("Please enter an integer!")
        return type_check(choice_list)


def odd_and_even(a: list[int]) -> list[int]:
    """Returns a list of odd numbers from even indices of a list."""
    result: list[int] = list()
    for i in range(0, len(a), 2):
        if a[i] % 2 == 1:
            result.append(a[i])
    return result


# print(odd_and_even([2, 9, 4, 17, 9, 10, 15, 13, 14, 21]))
# print(odd_and_even([1, 1, 1, 0, 1]))

# choice = type_check(["1. Option 1", "2. Option 2", "3. Option 3", "4. Option 4"])
# print(choice)

# Useful commands:
# python -m mypy exercises/<FILE_NAME.py>