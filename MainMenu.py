from time import sleep
from ReadSongs import read
from AddSongs import insertSongs
from UpdateSongs import update
from DeleteSongs import delete
from SongReport import reportMenuOptions

def menuOptions():       # function?  # subroutine?
    menuUI = \
    """
    Welcome to Music Database v1.00

    Please select an options:
        1. To Print 
        2. To Add 
        3. To Update 
        4. To Delete 
        5. Song Report
        5. To exit 

    """

    options = ["1", "2", "3", "4", "5", "6"]
    choice = 0
    while choice not in options:
        print(menuUI)
        choice = input("Select an option from the menu above: ")
        if choice not in options:
            print(choice, "is not a valid option, try again")
            sleep(1)
    return choice

mainProgram = True
while mainProgram:
    userChoice = menuOptions()  # Choice is stored in userChoice
    if userChoice == "1":
        read()
    elif userChoice == "2":
        insertSongs()
    elif userChoice == "3":
        update()
    elif userChoice == "4":
        delete()
    elif userChoice == "5":
        reportMenuOptions()
    else:
        mainProgram = False

input("Press Enter to Exit the Application. ")

# finished

