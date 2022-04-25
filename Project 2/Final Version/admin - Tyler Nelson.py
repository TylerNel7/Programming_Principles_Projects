# Name:  Tyler Nelson

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of Programming Principles in Semester 1, 2020.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json

# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.

#Repeatedly prompt user until a integer is entered
def input_int(prompt):
    while True:
        user_input = input(prompt)    
        try:
            if int(user_input) >= 1:
                user_input = int(user_input)
                return user_input
            else:
                print('Enter number that is "1" or above')
                
        except ValueError:
            print('Please insert Numbers only')   
    

# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.

#Repeatedly prompt user for input other then whitespace
def input_something(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input == '':
            print('Invaild input. Please input something')
        else:
            return user_input


# This function opens "data.txt" in write mode and writes the data to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.

#Save data list into data.txt file
def save_data(data_list):
    f = open('data.txt', 'w')
    json.dump(data_list, f, indent=4)
    f.close()
   

# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.dat
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.

#Try to open the data.txt file in read more and set the data_list to the contents inside
try:
    f = open('data.txt', 'r')
    data_list = json.load(f)
    f.close()

#If any error occurs, set data_list to a empty list
except:
    data_list = []

# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.

#Display welcome message
print('\nWelcome to the Joke Catalogue Admin Program.')

#Start While true loop and provide options
while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ')
        
    if choice == 'a':
        # Add a new joke.
        # See Point 3 of the "Requirements of admin.py" section of the assignment brief.

        #Add new joke to data_list with setup and punchline variables inside a dictionary and save
        setup = input_something('Enter setup of joke: ')
        punchline = input_something('Enter punchline of joke: ')
        joke = {'setup':setup, 'punchline':punchline, 'laughs':0, 'groans':0}
        data_list.append(joke)
        save_data(data_list)
        print('Joke added')
        

    elif choice == 'l':
        # List the current jokes.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.

        #List all jokes saved in the list. Unless list is empty, then display message
        if data_list == []:
            print("No jokes saved")
        else:
            print('Saved jokes: ')
            for index_num, joke in enumerate(data_list, 1):
                print(index_num, ':', joke['setup'])
                

    elif choice == 's':
        # Search the current jokes.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.

        #Search for a joke based on user inputed saerch term (In setup and punchline values). Unless list is empty, then display message
        if data_list == []:
            print('No jokes saved')
        else:
            search = input_something('Enter search term: ').lower()
            print('Jokes found: \n')
            for index, item in enumerate(data_list, 1):
                if search in item['setup'].lower() or search in item['punchline'].lower(): 
                    print('Joke', index, ':', '\n', 'Setup:    ', item['setup'], '\n', 'Punchline:', item['punchline'], '\n')
                    

    elif choice == 'v':
        # View a joke.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.

         #Display a joke based on the inputed joke number. Display appropriate messaged based on 'laughs' and 'groans' values. If list is empty display message.
        if data_list == []:
            print('No jokes saved')
        else:
            index_num = input_int('Input joke number: ')
            try:
                saved_joke = data_list[index_num - 1]
                print('\nSaved joke:', index_num)
                print(' Setup:    ', saved_joke['setup'], '\n', 'Punchline:', saved_joke['punchline'])
                if saved_joke['laughs'] == 0 and saved_joke['groans'] == 0:
                    print('\nThis joke has not been rated')
                else:
                    print(' Laughs: ', saved_joke['laughs'], '\n', 'Groans: ', saved_joke['groans'])
            #If input raises a index error, display message
            except IndexError:
                print('Invalid index number')


    elif choice == 'd':
        # Delete a joke.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.

         #Delete intended joke from the list. Unless list is empty, then display message
        if data_list == []:
            print('No jokes saved')
        else:
            delete_joke = input_int('Input joke number: ')
            try:
                delete_joke = delete_joke - 1
                del data_list[delete_joke]
                save_data(data_list)
                print('Joke deleted')
            #Run exception if input returns IndexError
            except IndexError:
                print('Invalid index number')

    elif choice == 'q':
        # Quit the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        print('Goodbye!')
        break

    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        print('\nInvalid choice')