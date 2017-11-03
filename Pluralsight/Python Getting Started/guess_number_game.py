import random

def get_random_number(min,max):
    num_to_guess = random.randint(min,max)
    return num_to_guess

min = 1
max = 20
number_to_guess = get_random_number(min,max)
output = "Guess numbers between {0} and {1}"
print(output.format(min,max))

found = False

while not found:
    print("Your input ?")
    user_input_num = int(input())
    if user_input_num == number_to_guess:
        print("Bingo!! You guessed it right")
        found = True
    else:
        if user_input_num > number_to_guess:
             print("Hint:Your number is too high")
        else:
             print("Hint:Your number is too low")


print("Game over!!")
