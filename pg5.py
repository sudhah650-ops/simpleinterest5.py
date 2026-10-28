def calculate_simple_interest():
    try:
        principal = float(sys.argv[1])
        rate = float(sys.argv[2])
        time = float(sys.argv[3])
        
        interest = (principal * rate * time) / 100
        
        print(f"\nThe calculated simple interest is: {interest:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculate_simple_interest
