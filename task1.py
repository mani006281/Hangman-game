#  Import the random module to pick a random word from the list
import random

# step 1:list = ["python", "apple", "hangman", "school", "coding"]

#  Step 2: Randomly choose one word from the list
word_to_guess = random.choice(word_list)

#  Step 3: Create a list with underscores for each letter
guessed_word = ["_"] * len(word_to_guess)

#  Step 4: Setup other variables
guessed_letters = []
attempts_left = 6

print("🎯 Welcome to Hangman!")
print("You have 6 chances to guess the word.")
print(" ".join(guessed_word))  # Show word as underscores

#  Step 5: Repeat until the word is guessed or attempts run out
while attempts_left > 0 and "_" in guessed_word:
    guess = input("\nEnter a letter: ").lower()

    # Step 6: Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single alphabet letter.")
        continue
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Step 7: Check if the guessed letter is in the word
    if guess in word_to_guess:
        print("✅ Good job! Letter is in the word.")
        # Reveal all positions of the guessed letter
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed_word[i] = guess
    else:
        attempts_left -= 1
        print(f"❌ Incorrect! You have {attempts_left} attempts left.")

    # Step 8: Show the current state of the guessed word
    print("Current word: " + " ".join(guessed_word))

#  Step 9: Game conclusion
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("\n💀 Game Over! The word was:", word_to_guess)
