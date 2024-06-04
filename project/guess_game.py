Number = 27

for Effort in range(3):
    numbers_said=int(input(f"please enter a n umber from 1 to 50: {Effort +1}/3 "))
    
    if numbers_said == Number:
        print("good job! You guessed it right ")
        break
    else:
        if Effort<2:
            print("Your guess was wrong! try again")
             
else :
    print("you lost! ")