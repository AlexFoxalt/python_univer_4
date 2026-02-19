import random

def get_number(prompt="Enter a number: "):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def countdown(num):
    print(f"Countdown from {num} to 1:")
    for i in range(num, 0, -1):
        print(i, end=' ')
    print("\n")

def generate_random_number():
    print("Choose a range for the random number:")
    small = get_number("Enter the smaller number: ")
    large = get_number("Enter the larger number: ")
    while small > large:
        print("Small number cannot be larger than the large number. Try again.")
        small = get_number("Enter the smaller number: ")
        large = get_number("Enter the larger number: ")
    comp_num = random.randint(small, large)
    return comp_num

def guess_prompt():
    print("I am thinking of a number…")
    return get_number("Take a guess: ")

def check_guess(guess, comp_num):
    if guess < comp_num:
        print("Too low! Try again.")
        return False
    elif guess > comp_num:
        print("Too high! Try again.")
        return False
    else:
        print("Correct, you win!")
        return True

def guessing_game():
    comp_num = generate_random_number()
    guessed = False
    while not guessed:
        guess = guess_prompt()
        guessed = check_guess(guess, comp_num)

def addition_quiz():
    a = random.randint(5, 20)
    b = random.randint(5, 20)
    print(f"Add these two numbers: {a} + {b}")
    user_answer = get_number("Your answer: ")
    check_answer(user_answer, a + b)

def subtraction_quiz():
    a = random.randint(25, 50)
    b = random.randint(1, 25)
    print(f"Subtract these two numbers: {a} - {b}")
    user_answer = get_number("Your answer: ")
    check_answer(user_answer, a - b)

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!")
    else:
        print(f"Incorrect, the answer is {correct_answer}")

def main_menu():
    while True:
        print("Enter 1 or 2:")
        print("1 - Addition Quiz")
        print("2 - Subtraction Quiz")
        choice = input("Your choice: ").strip()
        if choice == "1":
            addition_quiz()
            break
        elif choice == "2":
            subtraction_quiz()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")

if __name__ == "__main__":
    num = get_number("Enter a number for countdown: ")
    countdown(num)
    guessing_game()
    main_menu()
