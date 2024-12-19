#beginning

import os

lebron_points = 0
jordan_points = 0

#middle
os.system('clear')
answer = input("do you like, A) scoring by your self, B) wining but relying on your team to win?")
if answer == "A":
    lebron_points += 1
elif answer == "B":
    jordan_points += 1

os.system('clear')
answer = input("would you rather A) be on the heat, B) or the bulls?")
if answer == "A":
    lebron_points += 1
elif answer == "B":
    jordan_points += 1

os.system('clear')
answer = input("Would you rather eat lunch A) by yourself, B) with a group?")
if answer == "A":
    lebron_points += 1
elif answer == "B":
    jordan_points += 1

os.system('clear')
answer = input("would you rather, A) play in the modern NBA, B) play in the 90s?")
if answer == "A":
    lebron_points += 1
elif answer == "B":
    jordan_points += 1

os.system('clear')
answer = input("would you rather, A) play 22 seasons, B) play 15 seasons?")
if answer == "A":
    lebron_points += 1
elif answer == "B":
    jordan_points += 1

#end
os.system('clear')
if jordan_points > lebron_points:
    print("you like MJ more!")

else:
    print("you like LeBron more!")