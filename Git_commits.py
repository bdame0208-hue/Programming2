score=int(input("Enter Score: "))
if score >90:
    print("good job")
else:
    print("Bad job")
if score ==100:
    print("perfect")
else:
    print("wrong")
if ~(score == 75):
    print("score is not average")
print(bin(25))
x=67
if x == 4 or x ==8:
    print(f"{x}is my favorite")
elif x>20 and x<100:
    print(f"{x}is large")
else:
    print("meh")
bool_1 = True
val_1 = 36
val_2 = 28
bool_2 =  bool_1 or (val_1 == val_2)
print(bool_2)
for i in range(2,101):
    is_prime = True
    for j in range(2,i):
        if i%j ==0:
            is_prime=False
    if is_prime:
        print(f"{i}is prime")