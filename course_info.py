def main():
    # Load the dictionaries
    number_caps = num_dictionary()
    instructor_caps = ins_dictionary()
    time_caps = time_dictionary()

    # Get course room number
    course_number = input('Enter course number: ')
    if course_number in number_caps:
        print('Room:', number_caps[course_number])
    else:
        print('Incorrect Course Number')

    # Get course instructor
    course_number = input('Enter course number for instructor: ')
    if course_number in instructor_caps:
        print('Instructor:', instructor_caps[course_number])
    else:
        print('Incorrect Course Number')

    # Get course meeting time
    course_number = input('Enter course number for meeting time: ')
    if course_number in time_caps:
        print('Meeting Time:', time_caps[course_number])
    else:
        print('Incorrect Course Number')

def num_dictionary():
    return {"CS101": "3004", "CS102": "4501", "CS103": "6755",
            "NT110": "1244", "CM241": "1411"}

def ins_dictionary():
    return {"CS101": "Haynes", "CS102": "Alvarado", "CS103": "Rich",
            "NT110": "Burke", "CM241": "Lee"}

def time_dictionary():
    return {"CS101": "8:00am", "CS102": "9:00am", "CS103": "10:00am",
            "NT110": "11:00am", "CM241": "1:00pm"}

main()
