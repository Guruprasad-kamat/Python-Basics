
secret_word = "giraffe"
guess = ""
count = 0
limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if count < limit:
       guess = input("Enter ur guess: ")
       count = count+1
    else:
       out_of_guesses = True

if(out_of_guesses):
    print("You lost")
else:
    print("You Win!")