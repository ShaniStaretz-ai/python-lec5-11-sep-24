# print("ex1")
# for i in range(7, 39, 2):
#     print(i, end=" ")
# print()
#
# print("ex2")
# for i in range(50, 200+10, 10):
#     print(i, end=" ")
# print()
#
# print("ex3")
# number: int = int(input("please enter the end number:\n"));
# for i in range(1, number+1, 1):
#     print(i, end=" ")
# print()

print("ex4")  ###0.0,0.5,1.0
number2: int = int(input("please enter the end number:\n"));
# for i in range(0, number2,1):
#     print(float(i), end=" ")
#     i += 0.5;
#     print(float(i), end=" ")

for i in range(0, number2 * 2, 1):
    print(float(i / 2), end=" ")

print("end")


# ex3: do-while
sum_g: int = 0
avg_g = 0
while True:
    grade1 = int(input("please enter the grade1:\n"));
    if 0 > grade1 or grade1 > 100:
        print("invalid grade")
        break;
    grade2 = int(input("please enter the grade2:\n"));
    if 0 > grade2 or grade2 > 100:
        print("invalid grade")
        break;
    grade3 = int(input("please enter the grade3:\n"));
    if 0 > grade3 or grade3 > 100:
        print("invalid grade")
        break;
    sum_g = grade1 + grade2 + grade3
    avg_g = sum_g / 3
    if avg_g > 87 or grade1 == grade2 == grade3:
        break;
