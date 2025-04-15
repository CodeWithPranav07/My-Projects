import random

original_numbers = [4, 7, 6, 3, 2, 9, 10, 1, 8, 5]

for _ in range(5):
    numbers = original_numbers[:]
    random.shuffle(numbers)

    evens = [n for n in numbers if n % 2 == 0]
    odds = [n for n in numbers if n % 2 != 0]

    if len(evens) >= 5 and len(odds) >= 5:
        first_half = evens[:3] + odds[:2]
        second_half = odds[2:5] + evens[3:5]

        random.shuffle(first_half)
        random.shuffle(second_half)

        print("First Half:", first_half, "| Second Half:", second_half)
        
    else:
        print("Not enough even or odd numbers to split correctly.")