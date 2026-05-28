import random

# Game assets provided by the user
hangman_art = {
    0: ("   ", "   ", "   "),
    1: (" o ", "   ", "   "),
    2: (" o ", " | ", "   "),
    3: (" o ", "/| ", "   "),
    4: (" o ", "/|\\", "   "),
    5: (" o ", "/|\\", "/  "),
    6: (" o ", "/|\\", "/ \\"),
}

words = (
    "aardvark", "alligator", "alpaca", "ant", "anteater", "antelope", "ape", "armadillo",
    "baboon", "badger", "bat", "bear", "beaver", "bee", "bison", "boar", "buffalo",
    "butterfly", "camel", "capybara", "caribou", "cat", "caterpillar", "cattle", "chamois",
    "cheetah", "chicken", "chimpanzee", "chinchilla", "chough", "clam", "cobra", "cockroach",
    "cod", "coyote", "crab", "crane", "crocodile", "crow", "curlew", "deer", "dinosaur",
    "dog", "dogfish", "dolphin", "donkey", "dormouse", "dotterel", "dove", "dragonfly",
    "duck", "dugong", "dunlin", "eagle", "echidna", "eel", "eland", "elephant", "elk",
    "emu", "falcon", "ferret", "finch", "fish", "flamingo", "fly", "fox", "frog", "gaur",
    "gazelle", "gerbil", "giraffe", "gnat", "gnu", "goat", "goldfinch", "goldfish", "goose",
    "gorilla", "goshawk", "grasshopper", "grouse", "guanaco", "gull", "hamster", "hare",
    "hawk", "hedgehog", "heron", "herring", "hippopotamus", "hornet", "horse", "human",
    "hummingbird", "hyena", "ibex", "ibis", "jackal", "jaguar", "jay", "jellyfish",
    "kangaroo", "kingfisher", "koala", "kookabura", "kouprey", "kudu", "lapwing", "lark",
    "lemur", "leopard", "lion", "llama", "lobster", "locust", "loris", "louse", "lyrebird",
    "magpie", "mallard", "manatee", "mandrill", "mantis", "marten", "meerkat", "mink",
    "mole", "mongoose", "monkey", "moose", "mosquito", "mouse", "mule", "narwhal", "newt",
    "nightingale", "octopus", "okapi", "opossum", "oryx", "ostrich", "otter", "owl", "ox",
    "oyster", "panda", "panther", "parrot", "partridge", "peafowl", "pelican", "penguin",
    "pheasant", "pig", "pigeon", "polar-bear", "pony", "porcupine", "porpoise", "quail",
    "quelea", "quetzal", "rabbit", "raccoon", "rail", "ram", "rat", "raven", "red-deer",
    "red-panda", "reindeer", "rhinoceros", "rook", "salamander", "salmon", "sand-dollar",
    "sandpiper", "sardine", "scorpion", "seahorse", "seal", "shark", "sheep", "shrew",
    "skunk", "snail", "snake", "sparrow", "spider", "spoonbill", "squid", "squirrel",
    "starling", "stingray", "stoat", "stork", "swallow", "swan", "tapir", "tarsier",
    "termite", "tiger", "toad", "trout", "turkey", "turtle", "viper", "vulture", "wallaby",
    "walrus", "wasp", "weasel", "whale", "wildcat", "wolf", "wolverine", "wombat",
    "woodcock", "woodpecker", "worm", "wren", "yak", "zebra"
)

def display_hangman(wrong_guesses):
    """Prints the current state of the hangman art."""
    print("-------")
    for line in hangman_art[wrong_guesses]:
        print(f"|  {line}")
    print("|")
    print("=======")

def play_hangman():
    # 1. Setup the game state
    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_losses = 6

    print("Welcome to Hangman!")
    print("I am thinking of an animal...")

    # 2. Main Game Loop
    while wrong_guesses < max_losses:
        print("\n" + "="*30 + "\n")
        
        # Display the visual gallows
        display_hangman(wrong_guesses)
        
        # Build and display the hidden word (e.g., _ _ a _ )
        word_display = []
        for letter in secret_word:
            if letter in guessed_letters or letter == "-":
                word_display.append(letter)
            else:
                word_display.append("_")
        
        current_progress = " ".join(word_display)
        print(f"Word: {current_progress}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Check if the player won
        if "_" not in word_display:
            print(f"\n🎉 Congratulations! You guessed the word: {secret_word}")
            break

        # 3. Get player input
        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please type a single alphabetical letter.")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
            continue

        # Add guess to our tracker
        guessed_letters.add(guess)

        # 4. Check if the guess is right or wrong
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            wrong_guesses += 1

    # 5. Game Over Check
    if wrong_guesses == max_losses:
        print("\n" + "="*30 + "\n")
        display_hangman(wrong_guesses)
        print("💀 Game Over! You ran out of guesses.")
        print(f"The word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    play_hangman()