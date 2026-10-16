
import random


words = ["apple", "chair", "tiger", "house", "plant"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_guesses = 6
print("╔══════════════════════════════════╗")
print("║                                  ║")
print("║       🎮 HANGMAN GAME 🎮         ║")
print("║                                  ║")
print("╚══════════════════════════════════╝")

print("\n🎉 Welcome! Guess the hidden word.")
print("🔤 Guess one letter at a time.")
print("❤️ You have 6 incorrect guesses allowed.")

while wrong_guesses < max_guesses:

    # Display the word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\n🔎 Word:", display_word)
    print("❤️ Lives left:", max_guesses - wrong_guesses)

    # Check if the player wins
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You won!")
        print("🏆 The correct word was:", word)
        break

    # Get player's guess
    guess = input("✏️ Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one letter!")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("🔁 You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

else:
    print("\n💀 GAME OVER!")
    print("📖 The correct word was:", word)

print("\n╔══════════════════════════════════╗")
print("║      🌟 THANKS FOR PLAYING 🌟    ║")
print("╚══════════════════════════════════╝")
