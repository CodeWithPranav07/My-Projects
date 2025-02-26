import random 

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input('Guess the number between 1 and 100: '))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")

        elif abs(guess - number_to_guess) > 50:
            print("Way too low!" if guess < number_to_guess else "Way too high!")

        elif abs(guess - number_to_guess) > 30:
            print("Too low!" if guess < number_to_guess else "Too high!")

        elif abs(guess - number_to_guess) > 15:
            print("Still low!" if guess < number_to_guess else "Still high!")

        elif abs(guess - number_to_guess) > 10:
            print("Close, but a bit low." if guess < number_to_guess else "Close, but a bit high.")

        elif abs(guess - number_to_guess) > 5:
            print("Very close! Slightly low." if guess < number_to_guess else "Very close! Slightly high.")

        elif abs(guess - number_to_guess) > 2:
            print("Too close! Just a little low." if guess < number_to_guess else "Too close! Just a little high.")

        elif guess < number_to_guess:
            print("Just a bit too low!")

        elif guess > number_to_guess:
            print("Just a bit too high!")

        else:
            print("Congratulations! You guessed the number.")
            break

    except ValueError:
        print("Please enter a valid number!")