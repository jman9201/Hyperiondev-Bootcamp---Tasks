"""

Running a café, this script helps manage the stock and prices of items 
sold in the café

"""

# List of menu items
menu = ["Coffee", "Tea", "Cheese Sandwich", "Cake", "Ice Tea" ]

# Dictionary containing stock values for each item on the menu
stock ={
    "Coffee": 100,
    "Tea": 60,
    "Cheese Sandwich": 40,
    "Cake": 20,
    "Ice Tea": 60
}

# Dictionary containing prices for each item on the menu
price = {
    "Coffee": 2.5,
    "Tea": 2,
    "Cheese Sandwich": 4.5,
    "Cake": 3.5,
    "Ice Tea": 3
}

# Calculate total stock worth
total_stock_worth = 0
for item in menu:
    item_stock = stock[item]  # Get the stock quantity for the current item
    item_price = price[item]  # Get the price for the current item
    item_value = item_stock * item_price  # Calculate the total value of stock for the current item
    total_stock_worth += item_value  # Add the item value to the total stock worth

# Print the total stock worth
print("\n ----------------------------------")
print("\nTotal stock worth in the cafe: £", total_stock_worth)
print("\n ----------------------------------")