# Functions go here
# checks input is more than a given value
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
    

 # finds # of bits for 24 bit colour
def image_bits():

     # ask user for image width and height
     image_width = num_check("Image Width?: ", 1)
     image_height = num_check("Image Height?: ", 1)

     # calc number of pixels (width x height)
     print()
     num_pixels = image_width * image_height

     # calc number of bits (pixels x 24)
     num_bits = num_pixels * 24

     # output answer with working
     print()
     print("# of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))
     print("# bits = {} x 24 = {}". format(num_pixels, num_bits))
     print()

     return ""

# Main routine goes here
image_bits
     
