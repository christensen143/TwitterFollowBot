#!/usr/bin/python

from TwitterFollowBot import TwitterBot

# Set the while loop as active
active = True

# The while loop allows you to make corrections if you mistype the hashtag you want to follow
while active:

# Set the hashtag variable by getting input from the user
    hashtag = input("Please enter a hashtag you would like to follow: ")
# Tell the user what they entered and ask for confirmation
    confirm = input("You entered " + hashtag + ". Is this correct? [y or n] ")
    if confirm == 'n':
# If the user says no ask if they want to enter a different hashtag
        repeat = input("Would you like to enter a different hashtag? [y or n] ")
        if repeat == 'n':
# If the user answers yes the loop will continue. If they answer no the script will end
            print("This script will now end.")
            quit()
# If the user answers yes to the original confirmation mark the while loop inactive
    else:
        active = False

# Start the TwitterBot instance
my_bot = TwitterBot()

# Auto follow the number of accounts given in "count" that match the hashtag confirmed by the user 
my_bot.auto_follow(hashtag, count=800)
