def main():
    # Get the width and length of Rectangle 1
    width1 = int(input('Enter the width of Rectangle 1: '))
    length1 = int(input('Enter the length of Rectangle 1: '))

    # Get the width and length of Rectangle 2
    width2 = int(input('Enter the width of Rectangle 2: '))
    length2 = int(input('Enter the length of Rectangle 2: '))

    # Get Area of both Rectangles
    area1 = width1 * length1
    area2 = width2 * length2

    # Find out which is greater
    if area1 > area2:
        print('Rectangle 1 has the greater area.')
    elif area2 > area1:
        print('Rectangle 2 has the greater area.')
    else:
        print('Both rectangles are equal in area.')

if __name__ == "__main__":
    main()
