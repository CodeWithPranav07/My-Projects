
def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs / 2.20462

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    while True:
        print("\nWeight Converter")
        print("1. Convert Kilograms to Pounds")
        print("2. Convert Pounds to Kilograms")
        print("3. Exit")
        
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            kg = get_number("Enter weight in kilograms: ")
            print(f"{kg} kg is equal to {kg_to_lbs(kg):.2f} lbs")
        elif choice == "2":
            lbs = get_number("Enter weight in pounds: ")
            print(f"{lbs} lbs is equal to {lbs_to_kg(lbs):.2f} kg")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()