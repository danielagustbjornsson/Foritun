# take the length of the sequence as a input and put the value in a int n

# check if the n = 1
    # set 1 into the int num_first
# check if n = 2
    # set 1 into the int num_first
    # set 2 into the int num_second
# check if n >= 3
    # set 1 into the int num_first
    # set 2 into the int num_second
    # set 3 into the int num_third

# start a for loop that ends when the value reaches the value of n using the conter i
    # check if i = 1
        # print num_first
    # check if i = 2
        # print num_second
    # check if i = 3
        # print num_third
    # check if i > 3
        # add num_first, num_second, num_third and put it into num_third_n
        # num_fist = num_second
        # num_second = num_third
        # num_third = num_third_n
        # print num_third
 
n = int(input("Enter the length of the sequence: ")) # Do not change this line

if n == 1:
    num_first = 1
if n == 2:
    num_first = 1
    num_second = 2
if n >= 3:
    num_first = 1
    num_second = 2
    num_third = 3

for i in range(1, (n + 1)):
    if i == 1:
        print(num_first)
    if i == 2:
        print(num_second)
    if i == 3:
        print(num_third)
    if i > 3:
        num_third_n = num_first + num_second + num_third
        num_first = num_second
        num_second = num_third
        num_third = num_third_n
        print(num_third)