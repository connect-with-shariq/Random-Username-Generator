import random

# Predefined special characters and file names
SPECIAL_CHARS = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
ADJECTIVES_FILE = 'adjectives.txt'
NOUNS_FILE = 'nouns.txt'


def load_words(filename, default_words):
    """Load words from a file or use default list if file not found."""
    try:
        with open(filename, 'r') as f:
            return [line.strip().capitalize() for line in f]
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Using default list.")
        return default_words


# Load adjectives and nouns from files (or defaults)
adjectives = load_words(ADJECTIVES_FILE, ['Happy', 'Cool', 'Brave', 'Wild', 'Gentle', 'Rapid', 'Silent', 'Clever'])
nouns = load_words(NOUNS_FILE, ['Tiger', 'Dragon', 'Eagle', 'Wolf', 'Phoenix', 'Lion', 'Shark', 'Owl'])


def get_user_input():
    """Get user preferences for username generation."""
    # Number of usernames
    while True:
        try:
            num = int(input("How many usernames would you like to generate? "))
            if num < 1:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Include numbers?
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'

    # Include special characters?
    include_specials = input("Include special characters? (y/n): ").lower() == 'y'

    # Minimum length (optional)
    length = None
    while True:
        length_input = input("Minimum length? (press enter to skip): ").strip()
        if not length_input:
            break
        try:
            length = int(length_input)
            if length < 1:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    return num, include_numbers, include_specials, length


def generate_username(include_numbers, include_specials, min_length):
    """Generate a single username based on user preferences."""
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun

    # Add numbers
    if include_numbers:
        username += str(random.randint(0, 999))

    # Add special characters
    if include_specials:
        username += random.choice(SPECIAL_CHARS)

    # Adjust length if needed
    if min_length and len(username) < min_length:
        while len(username) < min_length and (include_numbers or include_specials):
            # Choose what to add based on user preferences
            if include_numbers and include_specials:
                choice = random.choice(['number', 'special'])
                if choice == 'number':
                    username += str(random.randint(0, 9))
                else:
                    username += random.choice(SPECIAL_CHARS)
            elif include_numbers:
                username += str(random.randint(0, 9))
            else:
                username += random.choice(SPECIAL_CHARS)

    return username


def save_usernames(usernames):
    """Save generated usernames to a file."""
    try:
        with open('usernames.txt', 'a') as f:
            for name in usernames:
                f.write(f"{name}\n")
        print(f"\nSaved {len(usernames)} usernames to 'usernames.txt'")
    except Exception as e:
        print(f"\nError saving usernames: {e}")


def main():
    print("=== Random Username Generator ===")
    num_usernames, include_numbers, include_specials, min_length = get_user_input()

    usernames = []
    for _ in range(num_usernames):
        username = generate_username(include_numbers, include_specials, min_length)
        usernames.append(username)

    # Display and save results
    print("\nGenerated Usernames:")
    for idx, name in enumerate(usernames, 1):
        print(f"{idx}. {name}")

    save_usernames(usernames)


if __name__ == "__main__":
    main()