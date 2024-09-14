# ex1:
# x: int = int(input("please enter the positive number:\n"));
# #x:int =0/-1, giving True condition instead of 1 input() to enter the loop
# while x <= 0:
#     print("this number is not positive")
#     x: int = int(input("please enter the negative number:\n"));
# print("finish")
# ex2:
# x: int = int(input("please enter the positive number:\n"));
# # x:int =0/-1, giving True condition instead of 1 input() to enter the loop
# counter: int = 1
# while x <= 0 and counter != 3:
#     print("this number is not positive")
#     x: int = int(input("please enter the negative number:\n"));
#     counter += 1
# print("finish")

# ex3: do-while
sum_g: int = 0
avg_g = 0
while True:
    grade1 = int(input("please enter the grade1:\n"));
    grade2 = int(input("please enter the grade2:\n"));
    grade3 = int(input("please enter the grade3:\n"));
    avg_g = (grade1 + grade2 + grade3) / 3
    if avg_g > 87 or grade1 == grade2 == grade3:
        break;