
# set max_in as -1
# set num_int as 1
# start a loop
    # tak in input and put it in num_int
    # checking if the num_int is lower then zero
        # exit the loop
    # check if the max_int = -1 
        # then set max_in as num_int (max_int = num_int)
    # check if the num_int is bigger then max_int
        # set num_int as max_int
# write out the max_int 


max_int = -1
num_int = 1
while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    # Fill in the missing code
    if num_int < 0:
        break
    if max_int == -1:
        max_int = num_int
    if num_int > max_int:
        max_int = num_int
print("The maximum is", max_int)    # Do not change this line
