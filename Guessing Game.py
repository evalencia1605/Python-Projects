secret_word = "carajo"
guess = ""
num_guesses = 0
max_guess = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if num_guesses < max_guess:
        guess = input("Enter a guess: ")
        num_guesses = num_guesses + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lost!")
else:
    print("Winn!!!")


#Indentations matterrr!!!!!!


    

