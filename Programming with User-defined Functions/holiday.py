# Create a list of city flight options for user to select (Each city will have different flight costs)
# Prompt the user to select one of the city flight option
# prompt the user to enter the number of nights they will be staying at a hotel
# Prompt the user to enter the number of days which they will be hiring a car
# Create the following four functions: 
#   - hotel_cost(): Take num_nights as an argument, and return a total cost for the hotel stay
#   - plane_cost(): Take city_flight as an argument, and return a cost for the flight (Hint use if/else statements in the function to retrieve a price based on the chosen city)
#   - car_rental(): Take rental_days as an argument, and return the total cost of the car rental
#   - holiday_cost(): Take the above, and return the total cost for the holiday
# Print out all the details about the holiday in a readable way

# Function to calculate hotel cost
def hotel_cost(num_nights):
    return 100 * num_nights # £100 per night

# Function to calculate flight cost
def plane_cost(city_flight):
    city_costs = {
        "London (£100)": 100,
        "New York (£300)": 300,
        "Hong Kong (£500)": 500
    }
    return city_costs.get(city_flight, 0) # Return cost for selected city, default to 0 if city not found

city_options = ['London (£100)', 'New York (£300)', 'Hong Kong (£500)']

# Function to calculate car rental cost
def car_rental(rental_days):
    return 50 * rental_days # £50 per day

# Function to calculate total holiday cost
def holiday_cost(city_flight, num_nights, rental_days):
    total_cost = plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)
    return total_cost

# Welcome message to the user
print("Welcome to our holiday planner!")
for index, city in enumerate(city_options, 1):
    print(f"{index}. {city}")

# Prompt user to select a city flight option
while True:
    user_choice = int(input("\nPlease select a city flight options (1, 2, 3): "))
    if 1<= user_choice <= len(city_options):
       selected_city = city_options[user_choice - 1]
       break
    else:
       print("Invalid selection. Please select from the available options")


# Prompt user to enter number of nights staying at a hotel
while True:
    num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
    if num_nights >= 0:
        break
    else:
        print("Invalid input. Please enter the number of nights you will be staying at a hotel")

# Prompt user to enter number of days renting a car
while True:
    rental_days = int(input("Enter the number of days you will be renting a car: "))
    if rental_days >= 0:
        break
    else:
        print("Invalid input. Please enter the number of days you will be renting a car")

# Calculate total holiday cost
total_cost = holiday_cost(selected_city, num_nights, rental_days)


# Print details about the holiday
print("\n======================================================")
print("\nYour Holiday Details: ")
print(f"\nCity Flight: {selected_city}")
print(f"Hotel cost: £{hotel_cost(num_nights)}")
print(f"Car Rental Cost: £{car_rental(rental_days)}")
print(f"Total cost: £{total_cost}")
print("\n======================================================")
