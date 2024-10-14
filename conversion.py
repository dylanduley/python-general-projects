CONVERSION_FACTOR = 0.8

def main():
    # Input the cost of your building.
    cost_build = float(input('Enter the cost of your building: $'))

    # Display 80 percent of the building cost.
    show_percent_cost (cost_build)


def show_percent_cost (cost_build):
    # Calculate Percentage of Cost.
    percent_cost = cost_build * CONVERSION_FACTOR

    # Display Total.
    print('For $' , cost_build, 'you will need $' , percent_cost, 'of insurance.')

main()
