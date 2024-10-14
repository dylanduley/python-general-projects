def main():
    name = input('Type your full name and press ENTER: ')
    name_list = name.split()

    print(name_list)  # Print the list to check the split result

    # Handle cases where there are fewer than three names
    try:
        first = name_list[0][0].upper()
        middle = name_list[1][0].upper() if len(name_list) > 1 else ""
        last = name_list[2][0].upper() if len(name_list) > 2 else ""
    except IndexError:
        print("Please enter your full name (first, middle, last).")
        return

    # Construct and print the initials
    initials = f"{first}. {middle}. {last}".strip()
    print(initials)

main()
