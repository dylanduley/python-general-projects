NUM_STATES = 5


def main():
    state_caps = state_cap_dictionary()

    correct = 0
    incorrect = 0

    for _ in range(NUM_STATES):
        state, capital = state_caps.popitem()

        print(f'What is the capital of {state}? ', end='')
        response = input()

        if response.lower() == capital.lower():
            correct += 1
        else:
            incorrect += 1

        print('Number of Correct answers:', correct)
        print('Number of Incorrect answers:', incorrect)


def state_cap_dictionary():
    return {
        "Washington": "Olympia", "Oregon": "Salem",
        "California": "Sacramento", "Ohio": "Columbus",
        "Nebraska": "Lincoln", "Colorado": "Denver",
        "Michigan": "Lansing", "Massachusetts": "Boston",
        "Florida": "Tallahassee", "Texas": "Austin",
        "Oklahoma": "Oklahoma City", "Hawaii": "Honolulu",
        "Alaska": "Juneau", "Utah": "Salt Lake City",
        "New Mexico": "Santa Fe", "North Dakota": "Bismarck",
        "South Dakota": "Pierre", "West Virginia": "Charleston",
        "Virginia": "Richmond", "New Jersey": "Trenton",
        "Minnesota": "Saint Paul", "Illinois": "Springfield",
        "Indiana": "Indianapolis", "Kentucky": "Frankfort",
        "Tennessee": "Nashville", "Georgia": "Atlanta",
        "Alabama": "Montgomery", "Mississippi": "Jackson",
        "North Carolina": "Raleigh", "South Carolina": "Columbia",
        "Maine": "Augusta", "Vermont": "Montpelier",
        "New Hampshire": "Concord", "Connecticut": "Hartford",
        "Rhode Island": "Providence", "Wyoming": "Cheyenne",
        "Montana": "Helena", "Kansas": "Topeka",
        "Iowa": "Des Moines", "Pennsylvania": "Harrisburg",
        "Maryland": "Annapolis", "Missouri": "Jefferson City",
        "Arizona": "Phoenix", "Nevada": "Carson City",
        "New York": "Albany", "Wisconsin": "Madison",
        "Delaware": "Dover", "Idaho": "Boise",
        "Arkansas": "Little Rock", "Louisiana": "Baton Rouge"
    }


main()
