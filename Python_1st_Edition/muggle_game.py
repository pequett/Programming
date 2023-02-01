secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess = 0

while guess == 0:
    guess = int(input())
    if guess != 777:
        guess = 0
        print("Ha ha! You're stuck in my loop!")
    else:
        print("Well done, muggle! You are free now.")
