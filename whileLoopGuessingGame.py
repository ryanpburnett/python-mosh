secret = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count += 1
    if guess == secret:
        print("a winner is you")
        break
else:
    print("Oops, you lost")