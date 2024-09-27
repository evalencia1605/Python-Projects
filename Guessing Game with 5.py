right_guess = "Karissa"
guess = ""
guess_count = 0
guess_max = 5
out_of_guesses = False

while right_guess != guess and not(out_of_guesses):
    if guess_count < guess_max:
        guess = input("Enter guess: ")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose!")
else:
    print("Win!!!")
