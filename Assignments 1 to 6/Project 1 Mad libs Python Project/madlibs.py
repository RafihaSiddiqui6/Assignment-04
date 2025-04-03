# Madlibs python project
import random
places = ['womderland', 'candyland', 'disneyland' , 'zombieland' ,' Island']
adjectives = ['wonderful', 'magical', 'spooky', 'delicious', 'mysterious']
activities = ['exploring', 'dancing', 'fighting zombies', 'eating sweets', 'meeting new people']

# Getting user input
friend = input("Enter your friend's name: ")

# Choosing random words
place = random.choice(places)
adjective = random.choice(adjectives)
activity = random.choice(activities)

# Generating the story
story = f"""
One day, me and my friend {friend} decided to go on an adventure.
we traveled to {place}, a {adjective} place where we spent our time {activity}.
It was the most unforgettable day of our lives!
"""

# Printing the story
print("\n--- My Random Mad Libs Story ---")
print(story)