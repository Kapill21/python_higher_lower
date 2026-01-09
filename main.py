import art
import game_data
import random




def get_random_account(exclude=None):
    """Return a random account dict, optionally excluding one account."""
    account = random.choice(game_data.data)
    while exclude is not None and account == exclude:
        account = random.choice(game_data.data)
    return account


def format_account(account):
    """Return a readable string for the account."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def get_guess():
    """Prompt until the user enters A or B. Return 'a' or 'b'."""
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    while guess not in ("a", "b"):
        guess = input("Please type only 'A' or 'B': ").lower()
    return guess


def play_round():
    """Play one full game until the user guesses wrong."""
    score = 0

    account_a = get_random_account()
    account_b = get_random_account(exclude=account_a)

    game_over = False
    while not game_over:
        print(art.logo)
        print(f"Compare A: {format_account(account_a)}.")
        print(art.vs)
        print(f"Against B: {format_account(account_b)}.")

        guess = get_guess()

        a_followers = int(account_a["follower_count"])
        b_followers = int(account_b["follower_count"])

        correct = "a" if a_followers > b_followers else "b"

        if guess == correct:
            score += 1
            print(f"You're right! Current score: {score}\n")

            
            account_a = account_b
            account_b = get_random_account(exclude=account_a)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


def main():
    playing = True
    while playing:
        play_round()
        again = input("Play again? (y/n): ").lower()
        while again not in ("y", "n"):
            again = input("Please type 'y' or 'n': ").lower()
        playing = (again == "y")


if __name__ == "__main__":
    main()




