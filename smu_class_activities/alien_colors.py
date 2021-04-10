alien_colors = ['red', 'yellow', 'green', 'purple']
if 'red' in alien_colors:
    print("You've earned 5 points")
elif 'purple' in alien_colors:
    print("You lose 5 points")
elif 'green' in alien_colors:
    print("You've got a 2 point bonus")
# Player gains 5 points
for alien_color1 in alien_colors:
    if alien_color1 != 'yellow':
        print("The alien has leveled up")
    elif alien_color1 == 'red':
        print("Warning! The alien has lost power")
    else:
        print(f"You've earned double x2 bonus for {alien_color1}")
# The Alien has leveled up and 25 pts earned
