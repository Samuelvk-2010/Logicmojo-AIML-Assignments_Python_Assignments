import random
print("Guess the number game !!!!")
a = int(input("Enter Start range.."))
b = int(input("Enter End range.."))
rand_num = random.randrange(a,b)
# print(rand_num)

x=-1
i=1
while x != rand_num:
    print(f"Attempt {i} Guess the number..")
    x= int(input("Enter a number between the given range.."))
    if (x==rand_num):
        break
    else:
        i=i+1
        val =  ">" if x>rand_num else "<"
        print(f"Entered number {x} is {val} compared to generated number Try again !!!")
        continue

print(f"Finally guessed the number {rand_num} on attempt {i}")
