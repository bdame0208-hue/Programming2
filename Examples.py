secret_number=300
initial_guess=2
guess=True
counter=0
power=2
while guess:
    print(initial_guess)
    if initial_guess == secret_number:
        print("correct")
        guess=False
    elif guess>secret_number:
        initial_guess=initial_guess-10**power
        power-=1
        counter+=1
    else:
        initial_guess=initial_guess+10**power
        counter+=1
print("try : ",counter)