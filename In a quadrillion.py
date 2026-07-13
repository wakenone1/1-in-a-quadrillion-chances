import random
import time
user_input = int(input("Pick a number between 1 and 1000000000000000 : "))
i = 0
while True:
    choice = random.randint(1, 1000000000000001)
    
    i += 1
    print(choice)
    print(f"Times shuffled : {i}")
    time.sleep(1)
    if choice == user_input:
        print("You found your partner!!!")
        break
    else:
        print("Number skipped...")
