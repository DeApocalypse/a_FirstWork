def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3*number+1

print("Enter number:")

while True:
    try:
        number=int(input())
    except:
        print("You need to enter an Integer Number.")
    else:
        break

while number!=1:
    print(collatz(number))
    number=collatz(number)
