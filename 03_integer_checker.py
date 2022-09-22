# checks input is a number more than a given value
def num_check(question, low):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than (or equal to) {}".format(low) 
        
        try:
        
            # ask user to enter a number
            response = int(input(question))
            
            # checks number is more than zero
            if response >= low:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    

# Main Routine goes here

keep_going = ""
while keep_going == "":
    print()
    # ask for integer (must be more than / equal to 0)
    var_integer = num_check("Enter a integer: ", 0)
    print()

    # ask for width and height of an image
    # Check if the number is more than / equal to 1
    image_width = num_check("Image Width?: ", 1)
    print()
    image_height = num_check("Image Height?: ", 1)

