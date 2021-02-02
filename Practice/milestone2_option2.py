

def display_menu():
    menu = "\nMENU\n \
a - Add player\n \
d - Remove player\n \
u - Update player rating\n \
r - Output players above a rating\n \
o - Output roster\n \
q - Quit"
    
    user_input = ''
    while user_input != 'q': 
        print(menu)
        user_input = input('Choose an option: ')

        if user_input.islower() == 'a':
            pass
        elif user_input.islower() == 'd':
            pass
        elif user_input.islower() == 'u':
            pass
        elif user_input.islower() == 'r':
            pass              
        elif user_input.islower() == 'o':
            pass 
        elif user_input.islower() == 'q':
            break
        else:
            print('Invalid input. Please try again.')
            continue

    return





    return


#//////////////////////////////////////////////////////////////////////////////////////////////////////////
def get_player_info():

    list_jerseys = [] # This list will hold jersey numbers (keys for the player_ratings dictionary)
    player = 1 # used to iterate thru below loop asking for 5 players' info
    player_ratings = {} # This dict will hold players numbers (keys) and ratings (values)
    while True: 
        if len(list_jerseys) < 5: # iterate loop until user has entered 5 pairs of values
            try:
                player_num = int(input(f'Enter player {player}\'s number:\n')) 
                list_jerseys.append(player_num) # Add jersey number to list of numbers
            except ValueError: # If non-int entry, display error message and reprompt for palyer number
                print('Invalid input. Please try again.\n')
                continue

            while True: # We get here after user enters a valid player number
                try:
                    player_rating = int(input(f'Enter player {player}\'s rating:\n'))
                    player_ratings[player_num] = player_rating # Add player number/rating pair to dictionary
                    player += 1 # Iterate player variarable for the next loop
                
                except ValueError: # If player rating entry is invalid, display error message and reprompt
                    print('Invalid input. Please try again.\n')
                    continue
                break     
        else:
            break

    return player_ratings, list_jerseys
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
def output_roster(player_ratings, list_jerseys):
    
    list_jerseys.sort() # Sort jersey numbers (dictionary keys) in ascending order

    # For each jersey number, print the player's jersey number and rating
    for jersey_number in list_jerseys:
        print(f'Jersey number: {jersey_number}, Rating: {player_ratings[jersey_number]}')

    return
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
if __name__ == '__main__':
    display_menu()
    player_ratings, list_jerseys = get_player_info()
    output_roster(player_ratings, list_jerseys)


