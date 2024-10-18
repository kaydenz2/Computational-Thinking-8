import random

# Pick a word at random
word_list = ["loopy","heart","audio","laugh","trial,wordle,being,image.girls"]
hidden_word = random.choice(word_list)
print("Welcome to Wordle!")
# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "🟩"
    elif guess_word[0] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    #Second Letter
    if guess_word[1] == hidden_word[0]:
        output += "🟩"
    elif guess_word[1] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
   
    # Third Letter
    if guess_word[2] == hidden_word[0]:
        output += "🟩"
    elif guess_word[2] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    #4th letter
    if guess_word[3] == hidden_word[0]:
        output += "🟩"
    elif guess_word[3] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    #5th Letter
    if guess_word[4] == hidden_word[0]:
        output += "🟩"
    elif guess_word[4] in hidden_word:
        output += "🟨"
    else:
        output += "⬛"
    
    

    # Result
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You win")
        break

print(f"You used {i+1} guesses")

