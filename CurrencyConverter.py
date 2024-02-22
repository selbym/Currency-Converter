# Function to convert USD to other currencies
def usd_to_other(amt):
    # Convert USD to Euro and print
    print(f"${amt} = €{amt * 0.92}")
    print()
    # Convert USD to Japanese Yen and print
    print(f"${amt} = {amt * 151.32}¥")
    print()
    # Convert USD to British Pound and print
    print(f"${amt} = £{amt * 0.81}")
    print()

# Function to convert Euro to other currencies
def eur_to_other(amt):
    # Convert Euro to USD and print
    print(f"€{amt} = ${amt * 1.08}")
    print()
    # Convert Euro to Japanese Yen and print
    print(f"€{amt} = {amt * 164.09}¥")
    print()
    # Convert Euro to British Pound and print
    print(f"€{amt} = £{amt * 0.87}")
    print()

# Function to convert Japanese Yen to other currencies
def jpy_to_other(amt):
    # Convert Japanese Yen to USD and print
    print(f"{amt}¥ = ${amt * 0.0066}")
    print()
    # Convert Japanese Yen to Euro and print
    print(f"{amt}¥ = €{amt * 0.0061}")
    print()
    # Convert Japanese Yen to British Pound and print
    print(f"{amt}¥ = £{amt * 0.0053}")
    print()

# Function to convert British Pound to other currencies
def gbp_to_other(amt):
    # Convert British Pound to USD and print
    print(f"£{amt} = ${amt * 1.24}")
    print()
    # Convert British Pound to Euro and print
    print(f"£{amt} = €{amt * 1.14}")
    print()
    # Convert British Pound to Japanese Yen and print
    print(f"£{amt} = {amt * 187.81}¥")
    print()

# Main function where the program execution begins
def main():
    # Display currency options for the user
    print("1 USD")
    print("2 EUR")
    print("3 JPY")
    print("4 GBP")

    # Input validation loop for currency choice
    while True:
        try:
            choice = int(input("Choose the currency (1, 2, 3, or 4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    # Take amount input from the user
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return  # Or loop back to ask for input again

    # Convert the amount to other currencies based on the user's choice
    if choice == 1:
        usd_to_other(amount)
    elif choice == 2:
        eur_to_other(amount)
    elif choice == 3:
        jpy_to_other(amount)
    elif choice == 4:
        gbp_to_other(amount)

# This ensures the main function is called only when the script is executed directly
if __name__ == "__main__":
    main()