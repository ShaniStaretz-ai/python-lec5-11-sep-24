#ex1
# x: int = int(input("please enter the positive number:\n"));
# #x:int =0/-1, giving True condition instead of 1 input() to enter the loop
# while x <= 0:
#     print("this number is not positive")
#     x: int = int(input("please enter the negative number:\n"));
# print("finish")

x: int = int(input("please enter the positive number:\n"));
#x:int =0/-1, giving True condition instead of 1 input() to enter the loop
counter:int=1
while x <= 0 and counter!=3:
    print("this number is not positive")
    x: int = int(input("please enter the negative number:\n"));
    counter+=1
print("finish")

