from ConnectSong import *
from time import sleep

# create a function
def reportMenuOptions():
    userOption = 0  # flag variable

    while userOption not in ["1", "2", "3", "4", "5"]:
        print("**********************************************")
        print("Song Report Menu Options\n**********************************************\nEnter:\n1. To print list of all songs.\n2. To print songs of a particular genre .\n3. To print songs of a particular year.\n4. To exit from song report\n"
        )
        print("-----------------------------------------------")
        # re-assign a new value to the options variable
        userOption = input("\nEnter one of the options above: ")
        if userOption not in ["1", "2", "3", "4"]:
            print(f"{userOption} is not a valid choice")

    mainPrgm = True  # flag variable
    while mainPrgm:  #  == True
        try:
            if userOption == "1":
                cursor.execute("SELECT * FROM Music")  
                row = cursor.fetchall()  
                sleep(1) 
                for record in row:
                    print(record)
                break
            elif userOption == "2":
                genre = input("Enter the genre of the song to be printed : ").title()
                genreValue = "'" + genre + "'"
                cursor.execute(f"SELECT * FROM Music where Genre = {genreValue}")  
                row = cursor.fetchall() 
                sleep(1) 
                for record in row:
                    print(record)
                break
            elif userOption == "3":
                year = int(input("Enter the year of the song to be printed : "))
                cursor.execute(f"SELECT * FROM Music where Year = {year}")  
                row = cursor.fetchall() 
                sleep(1)  
                for record in row:
                    print(record)
                break
            # elif userOption == "4":
            #     rating = input("Enter the rating of the film to be printed : ").upper()
            #     ratingValue = "'" + rating + "'"
            #     cursor.execute(f"SELECT * FROM Music where rating = {ratingValue}")  
            #     row = cursor.fetchall()  
            #     sleep(1) 
            #     for record in row:
            #         print(record)
            #     break
            else:  # re-assign  the value of main program to False
                mainPrgm = False
                input("press enter to Exit: ")
        except ValueError:
            print("Invalid Choice , Enter 1 - 5")


if __name__ == "__main__":
   reportMenuOptions()

