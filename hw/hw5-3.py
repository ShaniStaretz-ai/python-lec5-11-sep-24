# START
# ex1:
print("ex1");
height: float = -1;
while 0.4 > height or height > 2.5:
    print(height, ": input wrong, try again");
    height = float(input("please enter the height:\n"));

# ex2:
print("ex2");
number1: int = int(input("please enter the first number:\n"));
number2: int = int(input("please enter the second number:\n"));
if number2 > number1:
    for i in range(number2, number1 - 1, -1):
        print(i, end=" ")
else:
    for i in range(number2, number1 + 1, 1):
        print(i, end=" ")
print()

# ex3:
print("ex3");
pie: float = 3.14;
counter_attempts: int = 1;
user_pie: float = -1;
while pie != user_pie and counter_attempts != 3:
    user_pie: float = float(input("please enter the value of pie:\n"));
    counter_attempts += 1;
if counter_attempts == 3:
    print("3.14 is pie")
else:
    print("you are correct")

# ex4
print("ex4");
while True:
    number1 = int(input("please enter the first number:\n"));

    number2 = int(input("please enter the second number:\n"));

    number3 = int(input("please enter the third number:\n"));
    avg_numbers = (number1 + number2 + number3) / 3;
    if avg_numbers == number2 and 0 <= number1 <= 10 <= number2 <= 60 <= number3 <= 100:
        break;

# challenge:
beer_Counter = 10;
while beer_Counter > 0:
    age: int = int(input("please enter your age:\n"));
    if age > 17:
        print("you got beer");
        beer_Counter -= 1;
print("no more beers left")
