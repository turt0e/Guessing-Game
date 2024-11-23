import random

def guess():
    random_num = random.randint(1,100)

    attempts = 0
    correct_attempt = False

    print("This is a simple functional Guessing Game :)")
    print("From the numbers 1-100, what am I thinking?")

    while not correct_attempt:
        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if user_guess < random_num:
            print("Too low! Try again.")
        elif user_guess > random_num:
            print("Too high! Try again.")
        else:
            correct_guess = True
            print(f"Congratulations! You've guessed the correct number {random_num} in {attempts} tries.")
            break

if __name__ == "__main__":
    guess()
