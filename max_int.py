
num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
last_number = 0
while num_int >= 0:
    num_int = int(input("Input another number: "))
    if num_int > last_number:
        max_int = num_int
    

print("The maximum is", max_int)    # Do not change this line



