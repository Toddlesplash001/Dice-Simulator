import random
while True:
    a = random.randint(1, 6)
    print(a)
    b = input("Do you want to roll again? (Y/N):")
    if b.upper() == "Y":
        continue
    else:
        break
    
    

