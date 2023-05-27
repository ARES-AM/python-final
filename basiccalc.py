import tkinter as tk
import random

# initialize the game
score = 0
time_left = 30

# create the main window
root = tk.Tk()
root.title("Guess the Number")

# create the score label
score_label = tk.Label(root, text="Score: " + str(score))
score_label.pack()

# create the time label
time_label = tk.Label(root, text="Time Left: " + str(time_left))
time_label.pack()

# create the number label
number_label = tk.Label(root, text="Guess a number between 1 and 10")
number_label.pack()

# create the entry box for the player's guess
guess_entry = tk.Entry(root)
guess_entry.pack()

# create the button to submit the guess
submit_button = tk.Button(root, text="Submit")
submit_button.pack()

# create a function to handle the player's guess
def check_guess():
    global score
    global time_left

    # get the player's guess
    guess = int(guess_entry.get())

    # generate a random number between 1 and 10
    number = random.randint(1, 10)

    # check if the player's guess is correct
    if guess == number:
        score += 1
        score_label.config(text="Score: " + str(score))
        number_label.config(text="Correct! Guess another number.")
    else:
        number_label.config(text="Sorry, the number was " + str(number) + ". Guess again.")

    # clear the guess entry box
    guess_entry.delete(0, tk.END)

    # decrement the time left
    time_left -= 1
    time_label.config(text="Time Left: " + str(time_left))

    # check if the game is over
    if time_left == 0:
        number_label.config(text="Game over! Your final score is " + str(score))
        submit_button.config(state="disabled")
        guess_entry.config(state="disabled")

# bind the submit button to the check_guess function
submit_button.config(command=check_guess)

# start the game
guess_entry.focus()
root.mainloop()
