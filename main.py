# Global username variable
username = "username"

# Global password variable
password = "password"

usernameAttempt = input("Please enter your username: ")
passwordAttempt = input("Please enter your password: ")
classCode = input("Enter the class code: ")

gradeFile = open(classCode, "w+")

# Step 1 function
def step1():
    
    # Fix this. I don't know what your conditions for this are but it doesn't look quite right and could be 
    # improved... But don't worry about it - just trust the process!
    while "no" or " " == end:
        # Prompt for user to enter grades
        print('Please enter your grades in the following format - FirstName-LastName-Grade,')
        grades = str(input('Please enter your grades using the above format. '))
        
        # NOTE/TODO: What happens if they don't enter their grades in the above format? I'd validate that here:
        # .....
        
        # Writing the entered grades into the file
        gradeFile.write(grades)
        gradeFile.write("\n")
        
        isDone = bool(input("Are you finished? "))
        
        if !isDone:
            step1()
        else:
            print("Thank you! Your grades have been recorded!")
            exit()
            
# Helper function to print the banner
def printWelcomeBannerHelper():
    # Open the file 
    welcomeFile = open('welcome.txt')
    
    # Iterating over the lines that the file returns
    for currentLine in lines:
        # Print that line
        print(currentLine)
 
    # Once iteration 
    welcomeFile.close()

# TODO: Clean this up
if usernameAttempt != username or passwordAttempt != password:
    print("You have entered an incorrect username or password. Please try again.")
    exit()
else:
    print("Welcome!")
    step1()
