def calculate_simple_interest():
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the annual interest rate (in %): "))
        time = float(input("Enter the time period (in years): "))
        
        interest = (principal * rate * time) / 100
        
        print(f"\nThe calculated simple interest is: {interest:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculate_simple_interest
