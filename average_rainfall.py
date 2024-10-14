def main():
    total_inches = 0  # Tracks total inches of rainfall
    total_months = 0  # Tracks total months

    # Ask for the number of years
    number_of_years = int(input('Enter the number of years: '))

    # Loop through each year and each month to collect rainfall data
    for current_year in range(1, number_of_years + 1):
        for month in range(1, 13):
            inches_of_rain = float(input(f'Type in the number of inches of rainfall for year {current_year}, month {month}: '))
            total_inches += inches_of_rain
            total_months += 1  # Increment the month counter

    # Calculate the average rainfall
    average_rainfall = total_inches / total_months if total_months > 0 else 0

    # Display the average rainfall
    print(f'The average rainfall over {total_months} months is {average_rainfall:.2f} inches.')

if __name__ == "__main__":
    main()
