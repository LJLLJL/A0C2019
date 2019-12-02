def read_input(file):
    f = open(file, 'r')
    out = f.readlines()
    f.close()
    return out


def add_fuel(mass):
    # calculate the required fuel for a given mass
    fuel = int(int(mass)/3) - 2
    return fuel


def main():
    input = read_input("aoc1_input.txt")
    fuel_sum = 0
    fuel_sum_simple = 0
    for i in input:                         # loop through the list of masses to get the required fuel
        fuel_temp = add_fuel(i)
        fuel_sum = fuel_sum + fuel_temp
        fuel_sum_simple = fuel_sum_simple + fuel_temp
        while add_fuel(fuel_temp) > 0:      #let's check if the mass of the added fuel requires further fuel.
            fuel_temp = add_fuel(fuel_temp) # If yes, calculate it and add to the sum of fuel
            fuel_sum = fuel_sum + fuel_temp

    print("1st problem, fuel sum: ", fuel_sum_simple, ". 2nd problem, fuel sum: ", fuel_sum)


if __name__ == "__main__":
    main()

