# dm.py
# This script is a console application for a cab service called DropMe™.
# It calculates trip fares, applies promotions, and generates text file invoices.

import sys
import datetime
import random

# --- Data Storage ---
# We use a dictionary to store the price plan. The keys are the starting cities.
# The values are another dictionary where keys are the destination cities and values are the prices.
# This makes it easy to look up a price, for example: PRICE_PLAN['Alvin']['Jamz'] gives you 20.
PRICE_PLAN = {
    'alvin': {'alvin': 0, 'jamz': 20, 'razi': 40, 'mali': 40, 'zuhar': 20},
    'jamz': {'alvin': 20, 'jamz': 0, 'razi': 20, 'mali': 40, 'zuhar': 40},
    'razi': {'alvin': 40, 'jamz': 20, 'razi': 0, 'mali': 20, 'zuhar': 40},
    'mali': {'alvin': 40, 'jamz': 40, 'razi': 20, 'mali': 0, 'zuhar': 20},
    'zuhar': {'alvin': 20, 'jamz': 40, 'razi': 40, 'mali': 20, 'zuhar': 0}
}

# A list of valid city names for easy input validation. We store them in lowercase.
VALID_CITIES = ['alvin', 'jamz', 'razi', 'mali', 'zuhar']

# --- Helper Functions ---

def generate_invoice(start_city, end_city, base_amount, vehicle, promo_reduction, random_reduction, final_payment):
    """
    Creates and saves a .txt invoice file for a trip.
    The filename is based on the current date and time plus a random number.
    """
    try:
        # Get the current time for the invoice content and filename.
        now = datetime.datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        # Format the filename as per requirements: YYYY-MM-DD HH_MM_SS_xxxx.txt
        file_time_str = now.strftime("%Y-%m-%d %H_%M_%S")
        random_suffix = random.randint(1000, 9999)
        filename = f"{file_time_str}_{random_suffix}.txt"

        # Create the content that will be written to the file.
        # .capitalize() is used to make the city names look nice (e.g., 'alvin' -> 'Alvin').
        invoice_content = (
            f"Date: {date_str}\n"
            f"Time: {time_str}\n"
            f"Vehicle: {vehicle.capitalize()}\n"
            f"Start: {start_city.capitalize()}\n"
            f"End: {end_city.capitalize()}\n"
            f"Amount: {base_amount} KMD\n"
            f"Promo: {promo_reduction} KMD\n"
            f"Random Reduction: {random_reduction} KMD\n"
            f"Final payment: {final_payment} KMD"
        )

        # Write the content to the new text file.
        # 'with open' is used because it automatically handles closing the file.
        with open(filename, 'w') as f:
            f.write(invoice_content)
            
        print(f"\nInvoice successfully generated and saved as '{filename}'")

    except Exception as e:
        # If anything goes wrong during file creation, show an error.
        print(f"\nError: Could not generate or save the invoice file.")
        print(f"System error: {e}")


def display_price_plan():
    """
    Displays the full price plan for all vehicle types (Trishaw, Car, Van).
    """
    print("--- DropMe™ Official Price Plan (in KMD) ---")
    
    # Header for the table
    header = f"{'From/To':<10}" + "".join([f"{city.capitalize():>8}" for city in VALID_CITIES])
    
    for vehicle, multiplier in [('Trishaw', 1), ('Car', 2), ('Van', 3)]:
        print(f"\n--- {vehicle} Prices ---")
        print(header)
        print("-" * (10 + 8 * len(VALID_CITIES))) # A separator line
        
        # Loop through each starting city
        for start_city in VALID_CITIES:
            # Start the row with the city name
            row_str = f"{start_city.capitalize():<10}"
            # Add the price for each destination
            for end_city in VALID_CITIES:
                price = PRICE_PLAN[start_city][end_city] * multiplier
                row_str += f"{price:>8}"
            print(row_str)
    print("\n-------------------------------------------")


def display_help():
    """
    Displays a help message explaining how to use the program.
    """
    print("\n--- DropMe™ Command Help ---")
    print("This application helps you calculate trip fares and generate invoices.")
    print("\nUsage: python dm.py [arguments]")
    print("\n--- Commands ---")
    print("  dm <start_city> <end_city>               : Calculates fare for a Trishaw (default).")
    print("  dm <start_city> <end_city> /c            : Calculates fare for a Car.")
    print("  dm <start_city> <end_city> /v            : Calculates fare for a Van.")
    print("  dm <start_city> <end_city> /pro<number>  : Applies a promo discount (e.g., /pro5).")
    print("  dm <start_city> <end_city> /pro10 /v    : Combines options (10 KMD off for a Van).")
    print("  dm /price                                : Shows the full price plan for all vehicles.")
    print("  dm /?                                    : Shows this help message.")
    print("\n--- Available Cities ---")
    print("  Alvin, Jamz, Razi, Mali, Zuhar")
    print("\nExample: python dm.py alvin razi /c")


# --- Main Application Logic ---
def main():
    """
    The main function that runs the application.
    It parses command-line arguments and calls other functions.
    """
    # sys.argv is a list containing the command-line arguments.
    # sys.argv[0] is the script name itself ("dm.py"), so we ignore it.
    args = sys.argv[1:]

    # --- Argument Handling ---

    # Check if the user didn't provide any arguments.
    if not args:
        print("Error: No command provided. You must provide arguments.")
        display_help()
        return # Exit the function

    # Handle single-argument commands like /? or /price
    if len(args) == 1:
        command = args[0].lower() # Convert to lowercase for case-insensitivity
        if command == '/?':
            display_help()
            return
        elif command == '/price':
            display_price_plan()
            return
        else:
            print(f"Error: Unknown command '{args[0]}'. Use '/?' for help.")
            return

    # --- Trip Calculation Logic ---

    # The first two arguments should be the cities.
    start_city = args[0].lower()
    end_city = args[1].lower()

    # ** Input Validation **
    if start_city not in VALID_CITIES:
        print(f"Error: Invalid start city '{args[0]}'.")
        print("Please use one of the following:", ", ".join([c.capitalize() for c in VALID_CITIES]))
        return
        
    if end_city not in VALID_CITIES:
        print(f"Error: Invalid end city '{args[1]}'.")
        print("Please use one of the following:", ", ".join([c.capitalize() for c in VALID_CITIES]))
        return

    # --- Initialize Trip Variables ---
    vehicle = 'trishaw' # Default vehicle
    vehicle_multiplier = 1
    promo_reduction = 0
    random_reduction = 0
    has_user_promo = False
    
    # Look for optional arguments (/c, /v, /pro) in the rest of the list.
    option_args = args[2:]
    for opt in option_args:
        opt_lower = opt.lower()
        
        # Check for vehicle type
        if opt_lower == '/c':
            vehicle = 'car'
            vehicle_multiplier = 2
        elif opt_lower == '/v':
            vehicle = 'van'
            vehicle_multiplier = 3
            
        # Check for a promo code
        elif opt_lower.startswith('/pro'):
            has_user_promo = True
            try:
                # Extract the number from the promo code string (e.g., '/pro5' -> '5')
                promo_value_str = opt_lower.replace('/pro', '')
                if not promo_value_str.isdigit():
                    print(f"Error: Invalid promo code format '{opt}'. Must be like '/pro5'.")
                    return
                
                promo_reduction = int(promo_value_str)
                
                # Validate the promo amount is within the allowed range (1-15)
                if not 1 <= promo_reduction <= 15:
                    print(f"Error: Promo code amount must be between 1 and 15 KMD. You entered {promo_reduction}.")
                    return
                    
            except ValueError:
                print(f"Error: Invalid promo code format '{opt}'. Amount must be a whole number.")
                return
        else:
            # If the argument is not recognized
            print(f"Error: Unknown option '{opt}'. Use '/?' for help.")
            return

    # --- Fare Calculation ---
    
    # Get base price from the data structure
    base_price = PRICE_PLAN[start_city][end_city]
    
    # Apply vehicle multiplier
    total_amount = base_price * vehicle_multiplier
    
    # Apply random promotion ONLY if the user did not provide a promo code.
    if not has_user_promo:
        # This will randomly choose to apply a 5 KMD discount or not (50% chance).
        if random.choice([True, False]):
            random_reduction = 5
            
    # Calculate the final payment.
    final_payment = total_amount - promo_reduction - random_reduction
    
    # Ensure the final payment cannot be negative. If the discount is larger
    # than the fare, the fare is 0, not a negative number.
    if final_payment < 0:
        final_payment = 0

    # --- Display Results and Generate Invoice ---
    print("\n--- DropMe™ Trip Details ---")
    print(f"  Start City:       {start_city.capitalize()}")
    print(f"  End City:         {end_city.capitalize()}")
    print(f"  Vehicle Choice:   {vehicle.capitalize()}")
    print("----------------------------")
    print(f"  Base Fare:        {total_amount} KMD")
    if promo_reduction > 0:
        print(f"  Promo Discount:  - {promo_reduction} KMD")
    if random_reduction > 0:
        print(f"  Lucky Discount:  - {random_reduction} KMD")
    print("----------------------------")
    print(f"  Final Payment:    {final_payment} KMD")

    # Call the function to save the invoice to a text file.
    generate_invoice(
        start_city=start_city,
        end_city=end_city,
        base_amount=total_amount,
        vehicle=vehicle,
        promo_reduction=promo_reduction,
        random_reduction=random_reduction,
        final_payment=final_payment
    )


# This is standard Python practice. The code inside this 'if' block
# will only run when you execute the script directly.
if __name__ == "__main__":
    main()

