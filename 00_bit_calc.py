# Functions go here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):
    
    # Make string with five characters
    ends = decoration * 5 

    #add decoration to start and ent of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# checks user choice is 'integer', 'text' or 'image'
def user_choice():

    # List of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic", "p"]

    valid = False 
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # Checks for valid response and returns text, integer or image
        
        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        elif response in image_ok:
            return "image"

        elif response == "i":
            want_integer = input("Press <enter> for an integer or any key for image ")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else:
            # if response is not valid, output an error
            print(" PLease choose a valid file type!")
            print()


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

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display instructions if user has not used the program before

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    # Aks the user for the file type
    data_type = user_choice()
    print("You chose", data_type)

    # For integers, ask for the integer (must be more than / equal to 0)
    if data_type =="integer":
        var_integer = num_check("Enter an integer: ", 0)

    # For images, ask for width and height
    # (must be integers more than / equal to 1)
    elif data_type == "image":
        image_width = num_check("Image Width?: ", 1)
        print()
        image_height = num_check("Image Height?: ", 1)



    # For text, ask for a string
   