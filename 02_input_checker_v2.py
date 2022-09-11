# checks user choice is 'integer', 'text' or 'image'
def user_choice():

    # List of valid responses
    text_ok = ["text", "t", "txt"]
    integer_ok = ["interger", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic"]

    valid = False 
    while not valid:

        # ask user for choice and change response to lowercase
        response = input("File type (interger / text / image): ").lower()

        # CHecks for valid response and returns text, integer or image
        if response in text_ok:
            return "text"

        elif response in integer_ok:
            return "integer"

        else:
            # if response is not valid, output an error
            print(" PLease choose a valid file type!")
            print()


# Main routine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("You chose", data_type)

    print()