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
