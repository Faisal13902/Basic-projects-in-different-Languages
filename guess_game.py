goal = 7

guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess_input = int(input("Enter your guess: "))
    guess_count += 1
    if guess_input == goal:
        print("You win!")
        break
else: print("Sorry, you failed!")        
