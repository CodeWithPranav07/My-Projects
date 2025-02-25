# The Real Calculator

def calculator():
    while True:
        try:
            response = input("Enter an expression (q to quit): ")
            if response.lower() == 'q':
                print("Bye.")
                break
            result = eval(response)
            print("Result:", result)
        except Exception as e:
            print(f"Error: {e}")

calculator()