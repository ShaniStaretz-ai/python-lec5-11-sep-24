# python-lec5-11-sep-24

1) continue loops:
    1. for loop:
       for i in range(start,end, jump):
        * end+jump for include the end
        * defaults: start=0, jump=1 can not write it: range(end)
        * range doesn't work with float, need to be creative.

          i.e: for i in range(20): .....
    2. while loop advanced:
        * using while, when we don't know when you stop.
        * you can add conditions to the while
    3. do-while loop: 
        ```
       while TRUE:
       
           .....
   
       if(some condition):
       break;
       ```
       i.e: https://www.freecodecamp.org/news/python-do-while-loop-example/

## Etra notes:

1) print (x,end=" ") - changes the last char from "\n" to " " to all next print, till you break it with empty print()
2) if there is no use with the iterator at all, you can use with _ instead of i

   i.e for _ in range(20): ....
3) can do condition of x==y==z