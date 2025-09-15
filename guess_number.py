import random


def generate_secret_number(start: int = 1, end: int = 100) -> int:
    """Return a random integer within the given inclusive range."""
    return random.randint(start, end)


def prompt_for_guess(prompt: str = "Your guess: ", start: int = 1, end: int = 100) -> int:
    """Prompt the player for a numeric guess and validate input."""
    while True:
        guess_str = input(prompt)
        if not guess_str.strip().isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess_str)
        if guess < start or guess > end:
            print(f"Please enter a number between {start} and {end}.")
            continue
        return guess


def evaluate_guess(guess: int, secret: int) -> str:
    """Compare the guess to the secret number and return feedback."""
    if guess < secret:
        return "Too low"
    if guess > secret:
        return "Too high"
    return "Correct"


def main():
    print("Welcome to Guess the Number!")
    start_range = 1
    end_range = 100
    while True:
        secret = generate_secret_number(start_range, end_range)
        attempts = 0
        print(f"I'm thinking of a number between {start_range} and {end_range}.")
        while True:
            guess = prompt_for_guess(start=start_range, end=end_range)
            attempts += 1
            result = evaluate_guess(guess, secret)
            if result == "Correct":
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            else:
                print(result)
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for playing. Goodbye!")
            break


if __name__ == '__main__':
    main()
