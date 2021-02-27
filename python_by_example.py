""""#001
first_name = input("Please enter your first name: ")
print(f"Hello {first_name}!".title())

#002
first_name = input("Please enter your first name: ")
surname = input("Please enter your surname: ")
print(f"Hello {first_name} {surname}!".title())

#003
print("-What do you call a bear with no teeth? \n-A gummy bear!")

#004
num1 = int(input("Please enter the first number to add: "))
num2 = int(input("Please enter the second number to add: "))
addition_num = num1 + num2
print(f"The sum of your numbers is {addition_num}")

#005
num1 = int(input("Please enter the first number to add: "))
num2 = int(input("Please enter the second number to add: "))
num3 = int(input("Please enter the third number to multiply: "))
outcome = (num1 + num2) * num3
print(f"The outcome is {outcome:,}")

#006
started = input("How many slices has the whole pizza? ")
eaten = input("How many slices have you eaten? ")
left = int(started) - int(eaten)
print(f"{left} slices of the pizza left")

#007
name = input("Please enter your name: ")
age = input("How old are you? ")
new_age = int(age) + 1
print(f"{name.title()} next year you will be {new_age} years old!")

#008
bill = input("Please enter the total amount of the bill: ")
diners = input("Please enter the number of diners: ")
each_diner = int(bill) / int(diners)
print(f"Each diner owes {each_diner.__round__(2)}£ for the meal.")

#009
days = input("Please enter the number of days: ")
hours = int(days) * 24
minutes = hours * 60
seconds = minutes * 60
print(f"{days} days have:\n {hours:,} hours,\n {minutes:,} minutes and \n {seconds:,} seconds!")

#010
weight_in_kilos = input("Please enter your weight in kilos: ")
weight_in_pounds = int(weight_in_kilos) * 2.204
print(f"Your weight is {weight_in_pounds.__round__(2)} pounds!")

#011
big_number = float(input("Please enter a number above 100: "))
small_number = float(input("Please enter a number below 10: "))
divided_number = float(big_number) // float(small_number)
print(f"Number {small_number} goes into number {big_number:,}, {divided_number:,} times!")

#012
num1 = input("Please enter the first number: ")
num2 = input("Please enter the second number: ")
if num1 > num2:
    print(f"You entered numbers {num2} and {num1}")
else:
    print(f"You entered numbers {num1} and {num2}")

#013
num = int(input("Please enter a number lower than 20: "))
if num < 20:
    print("Thank you!")
else:
    print("Too high!")

#014
num = int(input("Please enter a number between 10 and 20: "))
if 10 < num < 20:
    print("Thank you!")
else:
    print("Incorrect answer!")

#015
colour = input("Please enter your favourite colour: ")
if colour.lower() == "red":
    print("I like red too!")
else:
    print(f"I don't like {colour}, i prefer red.")

#016
rain = input("Is it raining today? Enter (y) for yes or (n) for no: ")
if rain.lower() == "y":
    windy = input("Is it windy today? ")
    if windy.lower() == "y":
        print("It is too windy for an umbrella!")
    else:
        print("Take an umbrella!")
else:
    print("Enjoy your day!")

#017
age = int(input("Please enter your age: "))
if age >= 18:
    print("You can vote!")
elif age == 17:
    print("You can learn to drive!")
elif age == 16:
    print("You can buy a lottery ticket!")
else:
    print("You can go Trickor-Treating")

#018
num = int(input("Please enter a number: "))
if num <10:
    print("Too low!")
elif 10<= num <= 20:
    print("Correct!")
else:
    print("Too high!")

#019
num = input("Please enter the number 1, 2 or 3: ")
if num == "1":
    print("Thank you!")
elif num == "2":
    print("Well done!")
elif num == "3":
    print("Correct!")
else:
    print("Error message!")

#020
name = input("Please enter your name: ")
length = len(name)
print(f"Hello {name.title()}, your name has {length} letters.")

#021
name = input("Please enter your name: ")
surname = input("Now enter your surname: ")
length = len(name) + len(surname)
print(f"Hello {name.title()} {surname.title()}, your whole name has {length} letters.")

#022
name = input("Please enter your name: ")
surname = input("Now enter your surname: ")
print(f"Hello {name.title()} {surname.title()}")

#023
rhyme = input("Please enter the first line of the rhyme: ")
length = len(rhyme)
print(f"Your rhyme has {length} letters.")
start = int(input("Please enter a number as a starting point: "))
finish = int(input("Please enter a number as a finish point: "))
print(rhyme[start:finish])

#024
upper = input("Enter a word to be converted in upper case: ")
print(upper.upper())

#025
name = input("Please enter your first name: ")
if len(name) < 5:
    surname = input("Please enter your surname: ")
    print(f"{name.upper()}{surname.upper()}")
else:
    print(name.lower())

#026
pig_word = input("Please enter a word to be translated in pig language: ")
if pig_word[0].lower() in "bcdfghjklmnpqrstvwxzy":
    new_word = pig_word[1:]
    new_word = new_word + pig_word[0]
    new_word = new_word + "ay"
    print(new_word.lower())
else:
    new_word = pig_word + "way"
    print(new_word.lower())

#027
num = float(input("Please enter a number with decimal points and i will double it: "))
new_num = num * 2
print(new_num)

#028
num = float(input("Please enter a number with decimal points and i will double it: "))
new_num = num * 2
print(round(new_num, 2))

#029
import math
num = float(input("Please enter an integer greater than 500: "))
new_num = math.sqrt(num)
print(round(new_num, 2))

#030
import math
print(round(math.pi, 5))

#031
import math
radius = float(input("Please enter the radius of a circle and i will print the area: "))
area = math.pi * (radius ** 2)
print(round(area, 2))

#032
import math
radius = float(input("Please enter the radius of the cylinder: "))
depth = float(input("Please enter the depth of the cylinder: "))
area = math.pi * radius
total_vol = depth * area
print(f"Total volume: {round(total_vol, 3)}")

#033
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
whole_div = num1 // num2
remainder = num1 % num2
print(f"{num1} divided by {num2} is {int(whole_div)} with {round(remainder, 2)} remaining.")

#034
choice = input('''
1) Square
2) Triangle

Please enter a number:
''')
if choice == "1":
    length = float(input("Please enter the length of a side: "))
    square = length ** 2
    print(f"The area of the square is {round(square, 2)}")
elif choice == "2":
    base = float(input("Please enter the base of the triangle: "))
    height = float(input("Now enter the height: "))
    triangle = (base * height)/2
    print(f"The area of the triangle is {round(triangle, 2)}")
else:
    print("Please enter a valid number...")

#035
name = input("Please enter your name: ")
for i in range(0,3):
    print(name.title())

#036
name = input("Please enter your name: ")
num = int(input("Please enter the number of times to repeat your name: "))
for i in range(num):
    print(name.title())

#037
name = input("Please enter your name: ")
for i in name:
    print(i)

#038
name = input("Please enter your name: ")
num = int(input("Please enter the number of times to repeat your name: "))
for i in range(num):
    for y in name:
        print(y)

#039
num = int(input("Please enter a number between 1 and 12: "))
for i in range(1,13):
    answer = i * num
    print(f"{i} x {num} = {answer}")

#040
num = int(input("Please enter a number below 50: "))
start_num = 50
for i in range(start_num,(num-1), -1):
    print(i)

#041
name = input("Please enter your name: ")
num = int(input("Please enter a number: "))
if num < 10:
    for i in range(num):
        print(name.title())
else:
    for i in range(3):
        print("Too high")

#042
total = 0
for i in range(5):
    user_num = int(input("Please enter a number: "))
    user_included = input("Do you want this number included? Enter (y) or (n): ")
    if user_included == "y":
        total += user_num
print(total)

#043
up_or_down = input("Which direction to count? Enter (u) for up or (d) for down: ")
if up_or_down == "u":
    top_num = int(input("Please enter the top number: "))
    for i in range(1, (top_num+1)):
        print(i)
else:
    down_num = int(input("Please enter a number below 20: "))
    for i in range(20,(down_num-1),-1):
        print(i)

#044
invitations = int(input("Please enter the number of people to invite to your party: "))
if invitations < 10:
    for i in range(invitations):
        name = input("Please enter the name of the guest: ")
        print(f"{name.title()} has been invited!")
else:
    print("Too many people!")

#045
total = 0
while total < 50:
    num = int(input("Enter a number: "))
    total += num
    print(f"The total is {total}")

#046
num = int(input("Please enter a number: "))
while num < 5:
    num = int(input("Enter a number again: "))
print(f"Your last number you entered was {num}")

#047
num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))
total = num1 + num2
answer = input(f"The result is {total}. Do you want to add another number? Enter y or n: ")
while answer == "y":
    num3 = int(input("Please enter another number: "))
    total += num3
    answer = input(f"The result is {total}. Do you want to add another number? Enter y or n: ")
print(f"The total result is {total}.")

#048
count = 0
another_name = "y"
while another_name == "y":
    name = input("Please enter the name of the person to invite to your party: ")
    count += 1
    another_name = input(
        f"{name.title()} has now been invited Count:{count}. Do you want to invite another person? Enter y or n: ")
print(f"Total number of people coming to the party: {count}")

#049
compnum = 50
guess = int(input("Please enter your guess-number: "))
attempts = 1
while guess != compnum:
    if guess > 50:
        guess = int(input("Too high, please enter again: "))
        attempts += 1
    else:
        guess = int(input("Too low, please enter again: "))
        attempts += 1
print(f"Well done, you took {attempts} attempts.")

#050
num = int(input("Please enter a number: "))
while not 10 < num < 20:
    if num > 20:
        num = int(input("Too high, try again: "))
    elif num < 10:
        num = int(input("Too low, try again: "))
print("Thank you!")

#051
num = 10
while num > 0:
    print(f"There are {num} green bottles hanging on the wall.")
    print(f"{num} green bottles hanging on the wall.")
    print("and if 1 green bottle accidentally fall,")
    num -= 1
    answer = int(input("How many green bottles will be hanging on the wall? "))
    if answer == num:
        print(f"There are {num} green bottles hanging on the wall.")
    else:
        while answer != num:
            answer = int(input("No, try again: "))
print("There are no more green bottles hanging on the wall.")

#052
import random
print(random.randint(1,100))

#053
import random
fruits = ["apple", "lemon", "tomato", "cucumber", "orange"]
select = random.choice(fruits)
print(select)

#054
import random
h_or_t = ["h", "t"]
h_or_t_pc = random.choice(h_or_t)
h_or_t_user = input("Please choose head or tails (h/t): ")
if h_or_t_pc == h_or_t_user:
    print("You win!")
else:
    print("Bad luck..")
if h_or_t_pc == "h":
    print("The computer chose heads.")
else:
    print("The computer chose tails.")

#055
import random
num = random.randint(1,5)
user_num = int(input("Please enter a number between 1 and 5: "))
if num == user_num:
    print("Well done!")
elif user_num > num:
    user_num = int(input("Too high, try again: "))
    if user_num == num:
        print("Correct!")
    else:
        print("You lose..")
else:
    user_num = int(input("Too low, try again: "))
    if user_num == num:
        print("Correct!")
    else:
        print("You lose..")
if num != user_num:
    print(f"Computer chose {num}")

#056
import random
num = random.randint(1,10)
num_user = int(input("Please enter a number between 1 and 10: "))
while num != num_user:
    num_user = int(input("Wrong! Please enter again: "))
print("Well done!")

#057
import random
num = random.randint(1,10)
num_user = int(input("Please enter a number between 1 and 10: "))
while num != num_user:
    if num_user > num:
        num_user = int(input("Go down, please: "))
    else:
        num_user = int(input("Go up, please: "))
print("Well done!")

#058
import random
right_answers = 0
for i in range(1,6):
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    correct = num1 + num2
    answer = int(input(f"What is the result of adding numbers {num1} and {num2}: "))
    if answer == correct:
        right_answers += 1
if right_answers == 5:
    print(f"Well done! You scored 5 out of 5!")
else:
    print(f"So sorry, you scored only {right_answers} out of 5.")

#059
import random
colours = ["green", "blue", "black", "red", "yellow"]
colour_pc = random.choice(colours)
colour_user = input("Select a colour from green, blue, black, red and yellow: ")
while colour_pc != colour_user.lower():
    if colour_pc == "green":
        colour_user = input(f"I bet you are feeling GREEN from envy. Try again: ")
    elif colour_pc == "blue":
        colour_user = input(f"Don't feel BLUE. Try again: ")
    elif colour_pc == "black":
        colour_user = input(f"You can't stop thinking BLACK friday, right? Try again: ")
    elif colour_pc == "red":
        colour_user = input(f"You certainly feel RED from passion. Try again: ")
    elif colour_pc == "yellow":
        colour_user = input(f"We are all in a YELLOW submarine. Try again: ")
print("Well done!")

#060
import turtle
turtle.shape("turtle")
for i in range(0,4):
    turtle.forward(300)
    turtle.right(90)
turtle.exitonclick()

#061
import turtle
turtle.shape("turtle")
for i in range(0,3):
    turtle.forward(250)
    turtle.left(120)
turtle.exitonclick()

#062
import turtle
turtle.shape("turtle")
for i in range(0,360):
    turtle.forward(1)
    turtle.left(1)
turtle.exitonclick()

#063
import turtle
#turtle.shape("turtle")
turtle.color("black", "red")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.forward(150)
turtle.pendown()
turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.forward(150)
turtle.pendown()
turtle.color("black", "green")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

turtle.exitonclick()

#064
import turtle
turtle.shape("turtle")
for i in range(0,5):
    turtle.forward(100)
    turtle.left(145)
turtle.exitonclick()

#065
import turtle

turtle.shape("turtle")
turtle.left(90)
turtle.forward(150)

turtle.right(90)
turtle.penup()
turtle.forward(60)
turtle.pendown()

turtle.forward(100)
turtle.right(90)
turtle.forward(75)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(100)

turtle.penup()
turtle.forward(60)
turtle.pendown()

turtle.forward(100)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(100)

turtle.hideturtle()

turtle.exitonclick()

#066
import turtle
import random
turtle.shape("turtle")
colours = ["red", "black", "green", "orange", "blue", "cyan"]
turtle.pensize(3)

for i in range(0,8):
    random_color = random.choice(colours)
    turtle.color(random_color)
    turtle.forward(100)
    turtle.left(45)

turtle.hideturtle()
turtle.exitonclick()

#067
import turtle
for x in range(0,10):
    for i in range(0,8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

turtle.hideturtle()
turtle.exitonclick()

#068
import turtle
import random

lines_range = range(5,50)
lines = random.choice(lines_range)


for i in range(0,lines):
    pensize_range = range(1, 6)
    pensize = turtle.pensize(random.choice(pensize_range))
    forward_range = range(20, 120)
    forward = random.choice(forward_range)
    angle_range = range(1, 180)
    angle = random.choice(angle_range)
    turtle.pensize(pensize)
    turtle.forward(forward)
    turtle.left(angle)

turtle.exitonclick()

#069
countries = ("Sweden", "UK", "USA", "Italy", "France")
print(countries)
choice = input("Please pick a country to display its index: ")
if choice in countries:
    print(f"{choice} is in index {countries.index(choice)}")

#070
countries = ("Sweden", "UK", "USA", "Italy", "France")
choice = int(input("Please enter the index of the country to display: "))
print(countries[choice])

#071
sports = ["hockey", "baseball"]
user = input("What is your favourite sport? ")
sports.append(user)
sports.sort()
print(sports)

#072
school_subjects = ["math", "geography", "language", "arts", "history", "socials"]
print(school_subjects)
user = input("Please enter a subject you dislike from the list above: ")
school_subjects.remove(user)
print(f"{user} has been removed.")
print(school_subjects)
again = input("Do you want to remove another subject (y) (n)? ")
while again == "y":
    user = input("Please enter another subject you dislike: ")
    school_subjects.remove(user)
    print(f"{user} has been removed.")
    print(school_subjects)
    again = input("Do you want to remove another subject (y) (n)? ")
print(f"The final list of subjects is {school_subjects}")

#073
favorite_foods = {}
for i in range(4):
    food = input(f"Please enter your favorite food number {i+1}: ")
    favorite_foods[i+1] = food
print(favorite_foods)
remove = int(input("Which one would you like to get rid of? Enter the number: "))
del favorite_foods[remove]
print(f"favorite foods left: {sorted(favorite_foods.values())}")

#074
colours = ["black", "white", "green", "red", "blue", "yellow", "grey", "pink", "purple", "brown"]
start_num = int(input("Please enter a number between 0 and 4: "))
end_num = int(input("Please enter a number between 5 and 9: "))
print(f"This is a print of colours {start_num+1} to {end_num}")
print(colours[start_num:end_num])

#075
numbers = [111, 222, 333, 444]
for i in numbers:
    print(i)
user_num = int(input("Please enter a 3 digit number: "))
if user_num in numbers:
    print(f"Your number is in position {numbers.index(user_num)+1} in the list.")
else:
    print("That is not in the list.")

#076
list_of_invitations = []
for i in range(3):
    invitations = input("Please enter the name of a friend to invite to your party: ")
    list_of_invitations.append(invitations)
another = input("Would you like to add another name? Enter (y) or (n): ")
while another == "y":
    invitations = input("Please enter the name of a friend to invite to your party: ")
    list_of_invitations.append(invitations)
    another = input("Would you like to add another name? Enter (y) or (n): ")
print(f"You have invited {len(list_of_invitations)} people to your party.")

#077
list_of_invitations = []
for i in range(3):
    invitations = input("Please enter the name of a friend to invite to your party: ")
    list_of_invitations.append(invitations)
print(f"This is your list of invitations: {list_of_invitations}")
person = input("Please enter one name of the list above: ")
print(f"{person.title()} is in position {list_of_invitations.index(person)+1}")
delete = input("Do you still want that person to come to your party, (y) or (n)? ")
if delete == "y":
    print("All right!")
    print(f"This is your final list of invitations: {list_of_invitations}")
else:
    list_of_invitations.remove(person)
    print(f"{person.title()} has been deleted. This is your final list of invitations: {list_of_invitations}")

#078
tv_programmes = ["Lost", "The Sopranos", "Downton Abbey", "24"]
print("List of my favorites tv shows: ")
for i in tv_programmes:
    print(i)
another_show = input("Please enter your favorite show: ")
index = int(input("Please enter the index to insert it: "))
tv_programmes.insert(index, another_show.title())
print(tv_programmes)

#079
nums = []
for i in range(3):
    number = input("Please enter a number: ")
    nums.append(number)
    print(nums)
last_num = input("Do you still want the last number of your list(y/n)? ")
if last_num == "y":
    print(f"All right, your list is {nums}")
else:
    nums.remove(nums[2])
    print(f"All right, your list is {nums}")

#080
name = input("What is your name? ")
print(f"Your name has {len(name)} letters.")
surname = input("What is your surname? ")
print(f"Your surname has {len(surname)} letters.")
print(f"Your full name is {name.title()} {surname.title()}")
full_name = f"{name} {surname}"
print(f"Your full name has {len(full_name)} letters.")

#081
fav_subject = input("Please enter your favorite school subject: ")
for i in fav_subject:
    print(i, end="-")

#082
poem = "Two roads diverged in a yellow wood and sorry I could not travel both"
len_poem = len(poem)
start_point = int(input(f"Please enter the starting index point, between 0 and {len_poem}: "))
ending_point = int(input(f"Please enter the ending index point, between 0 and {len_poem}: "))
print(poem[start_point:ending_point])

#083
word = input("Please enter a word in upper case: ")
while not word.isupper():
    word = input("Please enter a word in upper case: ")
print(f"Thank you for your word '{word}'")

#084
postcode = input("Please enter your postcode: ")
print(postcode[0:2].upper())

#085
name = input("Please enter your full name: ")
vowels = "aeiou"
vowels_num = 0
for i in name.lower():
    if i in vowels:
        vowels_num += 1
print(f"Your name has {vowels_num} vowels")

#086
password = input("Please enter your password: ")
confirmation = input("Please enter your password again: ")
if password == confirmation:
    print("Thank you!")
elif password.lower() == confirmation.lower():
    print("They must be in the same case")
else:
    print("Incorrect")

#087
word = input("Please enter a word: ")
spelling = []
for i in word:
    spelling.insert(0, i)
for i in spelling:
    print(i)

#088
from array import *

integers = array ('i', [])
for i in range(5):
    num = int(input("Please enter a number: "))
    integers.append(num)
integers = sorted(integers)
integers.reverse()
print(integers)

#089
from array import *
import random

integers = array ('i', [])
for i in range(5):
    num = random.randint(0, 1000)
    integers.append(num)
for i in integers:
    print(i)

#090
from array import *
integers = array ('i', [])
numbers_added = 0
while numbers_added < 5:
    user_num = int(input("Please enter a number: "))
    if 10 < user_num < 20:
        integers.append(user_num)
        numbers_added += 1
    else:
        print("Outside the range")
print("Thank you!")
for i in integers:
    print(i)

#091
from array import *
integers = array ('i', [1, 22, 22, 3, 50])
print(integers)
user_num = int(input("Enter on number of the list: "))
times = 0
for i in integers:
    if user_num == i:
        times += 1
print(f"The number you chose appears {times} time(s) in the list")

#092
from array import *
import random

user_nums = array('i', [])
for i in range(3):
    num = int(input("Please enter a number: "))
    user_nums.append(num)

random_nums = array('i', [])
for i in range(5):
    num = random.randint(1, 1000)
    random_nums.append(num)

user_nums.extend(random_nums)
user_nums = sorted(user_nums)
for i in user_nums:
    print(i)

#093
from array import *

user_nums = array('i', [])
for i in range(5):
    num = int(input("Please enter a number: "))
    user_nums.append(num)
user_nums = sorted(user_nums)
print(user_nums)
get_rid = int(input("Please enter a number to remove from the list: "))
user_nums.remove(get_rid)
user_nums2 = array('i', [])
user_nums2.append(get_rid)
print(user_nums)
print(user_nums2)

#094
from array import *

nums = array('i', [10, 20, 30, 40, 50])
print(nums)
user_num = int(input("Please choose one of the numbers above: "))
while user_num not in nums:
    user_num = int(input("This number is invalid, please try again: "))
print(f"The number you chose is in position {nums.index(user_num)}")

#095
from array import *

nums = array('f', [10.26, 20.55, 30.54, 40.12, 50.85])
user_num = float(input("Please enter a number between 2 and 5: "))
while not 2 <= user_num <= 5:
    user_num = float(input("Please enter an integer between 2 and 5: "))
for i in nums:
    print((i / user_num).__round__(2))

#096
list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list)

#097
list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list)
user_row = int(input("Please select the row: "))
user_col = int(input("Please select the column: "))
selected = list[user_row][user_col]
print(selected)

#098
list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list)
user = int(input("Please enter a row to display: "))
print(list[user])
value = int(input("Enter a new value to that row: "))
list[user].append(value)
print(list)

#099
list = [[2, 5, 8], [3, 7, 4], [1, 6, 9], [4, 2, 0]]
print(list)
user_row = int(input("Please enter a row to display: "))
print(list[user_row])
user_col = int(input("Please enter a column to display: "))
print(list[user_row][user_col])
change = input("Do you want to change that value (y/n)? ")
if change == "y":
    new_value = int(input("Please enter a new value: "))
    list[user_row][user_col] = new_value
    print(list)
else:
    print("Thank you, the program will now exit...")

#100
sales = {"John": {"N": 3026, "S": 8463, "E": 8441, "W": 2694},
         "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
         "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
         "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
         }
print(sales)

#101
from pprint import pprint
sales = {"John": {"N": 3026, "S": 8463, "E": 8441, "W": 2694},
         "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
         "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
         "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}
         }
pprint(sales)
user_name = input("Please choose a name to display: ")
user_region = input(f"Please choose a region of {user_name} to display: ")
print(f"The sales of {user_name.title()} in '{user_region.title()}' is "
      f"{sales[user_name.title()][user_region.title()]:,}")
user_name = input("Please choose a name: ")
user_region = input(f"Please choose a region of {user_name} to change: ")
new_value = int(input("Please enter the new value: "))
sales[user_name.title()][user_region.title()] = new_value
print(f"{user_name.title()}'s new sales are {sales[user_name.title()]}")

#102
list = {}
for i in range(4):
    name = input(f"Please enter a name ({i+1} of 4): ")
    age = input(f"Please enter {name}'s age: ")
    shoe_size = int(input(f"Please enter {name}'s shoe size: "))
    list[name.title()] = {"Age": age, "Shoe size": shoe_size}
print(list)
choose = input("Please pick a person to display the details: ")
print(list[choose.title()])

#103
list = {}
for i in range(4):
    name = input(f"Please enter a name ({i+1} of 4): ")
    age = int(input(f"Please enter {name}'s age: "))
    shoe_size = int(input(f"Please enter {name}'s shoe size: "))
    list[name.title()] = {"Age": age, "Shoe size": shoe_size}
print(list)
for name in list:
    print(f"{(name).title()}'s age is {list[name]['Age']}")

#104
list = {}
for i in range(4):
    name = input(f"Please enter a name ({i+1} of 4): ")
    age = int(input(f"Please enter {name}'s age: "))
    shoe_size = int(input(f"Please enter {name}'s shoe size: "))
    list[name.title()] = {"Age": age, "Shoe size": shoe_size}
print(list)
remove = input("Please enter a name you want to remove: ")
del list[remove.title()]
print(list)
print(f"{remove.title()} has been removed")

#105
file = open("Numbers.txt", "w")
file.write("1, ")
file.write("2, ")
file.write("3, ")
file.write("4, ")
file.write("5 ")
file.close()

#106
file = open("Names.txt", "w")
file.write("Anne\n")
file.write("Liz\n")
file.write("Sonia\n")
file.write("Adelaize\n")
file.write("Mairy\n")
file.close()

#107
file = open("Names.txt", "r")
print(file.read())
file.close()

#108
file = open("Names.txt", "r")
print(file.read())
file.close()
user = input("Please add a name to the file above: ")
file = open("Names.txt", "a")
file.write(f"{user.title()}, ")
file.close()
file = open("Names.txt", "r")
print(file.read())
file.close()

#109
user = input('''
1) Create a new file
2) Display the file
3) Add a new item to the file
Please select 1, 2 or 3: 
''')
if user == "1":
    subject = input("Please enter a school subject: ")
    file = open("Subject.txt", "w")
    file.write(f"{subject.title()}, ")
    file.close()
elif user == "2":
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
elif user == "3":
    file = open("Subject.txt", "a")
    subject = input("Please enter a school subject: ")
    file.write(f"{subject.title()}, ")
    file.close()
    file = open("Subject.txt", "r")
    print(file.read())
    file.close()
else:
    print("You should only select 1, 2 or 3, please try again...")

#110
file = open("Names.txt", "r")
print(file.read())
file.close()

file = open("Names.txt", "r")
user = input("Please select one of the names above: ")
user = user + "\n"
for i in file:
    if i != user:
        file = open("Names2.txt", "a")
        newvalue = i
        file.write(newvalue)
        file.close()
file.close()

#111
#import csv
file = open("Books.csv", "w")
new_record = '''To Kill A Mockingbird, Harper Lee, 1960\n\
A Brief History of Time, Stephen Hawking, 1988\n\
The Great Gatsby, F. Scott, Fitzgerald 1922\n\
The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n\
Pride and Prejudice, Jane Austen, 1813\n\
'''

file.write(str(new_record))
file.close()

#112
import csv
user_book = input("Please add another book to the file: ")
user_author = input("Please add the author: ")
user_year = input("Please add the year the book was written: ")
new_record = f"{user_book}, {user_author}, {user_year}"
file = open("Books.csv", "a")
file.write(str(new_record))
file.close()
file = open("Books.csv", "r")
print(f"\n{file.read()}")
file.close()

#113
import csv
file = open("Books.csv", "a")
user_input = int(input("How namy records would you like to add? "))

for i in range(user_input):
    user_book = input("Please add another book to the file: ")
    user_author = input("Please add the author: ")
    user_year = input("Please add the year the book was written: ")
    new_record = f"{user_book}, {user_author}, {user_year}\n"
    file.write(str(new_record))
file.close()

file = open("Books.csv", "r")
print(file.read())
file.close()

file = open("Books.csv", "r")
author = input("Type your favourite author: ")
counter = 0
for row in file:
    if author in row:
        print(row)
        counter += 1
if counter == 0:
    print("No books from that author on the list")

#114
import csv
file = open("Books.csv", "r")
print(file.read())
file.close()

start_year = int(input("Enter a starting year of your book search: "))
end_year = int(input("Enter an ending year of your book search: "))

file = list(csv.reader(open("Books.csv")))
books = []
for row in file:
    books.append(row)

x = 0
for row in books:
    if start_year <= int(books[x][2]) <= end_year:
        print(books[x])
    x += 1

#114 2nd way
import csv
file = open("Books.csv", "r")
print(file.read())
file.close()

file = open("Books.csv", "r")
start_year = int(input("Enter a starting year of your book search: "))
end_year = int(input("Enter an ending year of your book search: "))
user_range = range(start_year, end_year+1)

years = []
for i in user_range:
    years.append(i)

string_years = [str(int) for int in years]
#print(string_years)

for row in file:
    for year in string_years:
        if year in row:
            print(row)
file.close()

#115
import csv
file = open("Books.csv", "r")
x = 1
for row in file:
    print(f"Row {x} : {row}")
    x += 1

#116
import csv
file = list(csv.reader(open("Books.csv")))
books = []
x= -1
for row in file:
    books.append(row)
    x += 1
print(books)
delete = int(input(f"Which row you want deleted? Enter a number between 0 and {x}: "))
del books[delete]
print(books)
row_change_num = int(input(f"Which row you want changed? Enter a number between 0 and {x-1}: "))
element_change_num = int(input(f"Which row you want changed? Enter a number between 0 and 2: "))
element_change = input("Please enter the new value: ")
books[row_change_num][element_change_num] = element_change
print(books)

file = open("Books.csv", "w")
for row in books:
    file.write(f"{str(row)}\n")
file.close()

#117
import csv
from random import sample
name = input("What is your name? ")
file = open("Math_game.csv", "a")
file.write(f"\n{name.title()}\n")
file.close()
question1 = "How much is 5.5 x 2: "
answer1 = 11
question2 = "How much is 5.5 x 4: "
answer2 = 22
question3 = "How much is 5.5 x 6: "
answer3 = 33
question4 = "How much is 5.5 x 8: "
answer4 = 44
random_questions = question1, question2, question3, question4
asked = sample(random_questions, 2)
print(asked)
points = 0
x = 0

for i in asked:
    quest1 = int(input(asked[x]))

    if question1 in asked[x]:
        if quest1 == 11:
            print("That's right, bravo!")
            points += 50
            file = open("Math_game.csv", "a")
            file.write(f"Question: {str(question1)}\n")
            file.write(f"Your answer was: {str(quest1)}\n")
            file.close()
        else:
            print("I don't think so, try again..")
            file = open("Math_game.csv", "a")
            file.write(f"{str(question1)}\n")
            file.write(f"Your answer was: {str(quest1)}\n")
            file.close()
    if question2 in asked[x]:
        if quest1 == 22:
            print("That's right, bravo!")
            points += 50
            file = open("Math_game.csv", "a")
            file.write(f"Question: {str(question2)}\n")
            file.write(f"Your answer was: {str(quest1)}\n")
            file.close()
        else:
            print("I don't think so, try again..")
            file = open("Math_game.csv", "a")
            file.write(f"Question: {str(question2)}\n")
            file.write(f"Your answer was: {str(quest1)}\n")
            file.close()
    if question3 in asked[x]:
        if quest1 == 33:
            print("That's right, bravo!")
            points += 50
            file = open("Math_game.csv", "a")
            file.write(f"Question: {str(question3)}\n")
            file.write(f"Your answer was: {str(quest1)}\n")
            file.close()
        else:
            print("I don't think so, try again..")
            file = open("Math_game.csv", "a")
            file.write(f"Question: {str(question3)}\n")
            file.write(f"Your answer was: {str(quest1)}\n")
            file.close()
    if question4 in asked[x]:
        if quest1 == 44:
            print("That's right, bravo!")
            points += 50
            file = open("Math_game.csv", "a")
            file.write(f"Question: {str(question4)}\n")
            file.write(f"Your answer was: {str(quest1)}\n")
            file.close()
        else:
            print("I don't think so, try again..")
            file = open("Math_game.csv", "a")
            file.write(f"Question: {str(question4)}\n")
            file.write(f"Your answer was: {str(quest1)}\n")
            file.close()
    x += 1
print(f"Total points: {points}")
file = open("Math_game.csv", "a")
file.write(f"Total points: {points}\n")
file.close()

# 117 2nd way
# I have to notice that the solution in the book did not answer the challenge itself.
# Maybe the wording was not proper, maybe something else.
# Anyways the challenges themselves are great, i enjoyed them all.

from random import sample

name = input("What is your name? ")
file = open("Math_game.csv", "a")
file.write(f"\n{name.title()}\n")
file.close()

question1 = "How much is 5.5 x 2: "
question2 = "How much is 5.5 x 4: "
question3 = "How much is 5.5 x 6: "
question4 = "How much is 5.5 x 8: "
question5 = "How much is 5.5 x 10: "

random_questions = [question1, question2, question3, question4, question5]
random_answers = [11, 22, 33, 44, 55]
asked = sample(random_questions, 2)
#print(asked)
points = 0
x = 0
y = 0
right_answers = 0

for i in asked:
    for y in range(len(random_questions)):

        if i in random_questions[y]:
            answer = int(input(i))

            if answer == random_answers[y]:
                print("That's right, bravo!")
                points += 50
                file = open("Math_game.csv", "a")
                file.write(f"Question: {str(random_questions[y])}\n")
                file.write(f"Your answer was: {str(answer)}\n")
                file.close()
                right_answers += 1
                y += 1
                #print(f"y = {y}") helps in understanding what's not working properly in the loop
            else:
                print("I don't think so, try again..")
                file = open("Math_game.csv", "a")
                file.write(f"{str(random_questions[y])}\n")
                file.write(f"Your answer was: {str(answer)}\n")
                file.close()
                y += 1
                #print(f"y = {y}") helps in understanding what's not working properly in the loop
        else:
            y += 1
            #print(f"y = {y}") helps in understanding what's not working properly in the loop
    x += 1
    #print(f"x = {x}") helps in understanding what's not working properly in the loop
print(f"Total points: {points}")
file = open("Math_game.csv", "a")
file.write(f"Total points: {points}\n")
file.write(f"Right answers: {right_answers} / {x} or {((right_answers/x)*100).__round__(2)} %\n\n")
file.close()
print(f"Right answers: {right_answers} / {x} or {((right_answers/x)*100).__round__(2)} %\n")
# print(y)
# print(x)

#118
def enter_num():
    num = int(input("Please enter a number: "))
    return num

def main():
    num = enter_num()
    numbers = (list(i for i in range(1, num+1)))
    print(numbers)
    print(num)

main()

#118 2nd way
def enter_num():
    num = int(input("Please enter a number: "))
    return num

def count(num):
    n = 1
    while n <= num:
        print(n)
        n += 1

def main():
    num = enter_num()
    count(num)

main()

#119
from random import randint

def random_num():
    low_num = int(input("Please enter the low number: "))
    high_num = int(input("Please enter the high number: "))
    comp_num = randint(low_num, high_num)
    #print(comp_num)
    return comp_num

def guess_num():
    user_num = int(input("I am thinking of a number, can you guess? "))
    return user_num

def check_results(comp_num, user_num):
    while comp_num != user_num:
        if user_num > comp_num:
            print("Go DOWN please.")
            user_num = int(input("Enter again: "))
        else:
            print("Go UP please.")
            user_num = int(input("Enter again: "))
    print("Correct, you win!")

def main():
    comp_num = random_num()
    user_num = guess_num()
    check_results(comp_num, user_num)

main()

#120
import random

print("1) Addition")
print("2) Subtraction")
choice = input("Enter 1 or 2: ")

def add_nums():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    actual_answer = num1 + num2
    answer = int(input(f"How much is {num1} + {num2} ? "))
    return actual_answer, answer


def subtract_nums():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    actual_answer = num1 - num2
    answer = int(input(f"How much is {num1} - {num2} ? "))
    return actual_answer, answer


def check_answers(actual_answer, answer):
    if answer == actual_answer:
        print("Bravo, you found it!")
    else:
        print(f"Incorrect, the answer is {actual_answer}")


def main():
    global choice
    if choice == "1":
        actual_answer, answer = add_nums()
        check_answers(actual_answer, answer)
    elif choice == "2":
        actual_answer, answer = subtract_nums()
        check_answers(actual_answer, answer)
    else:
        choice = input("Enter a valid choice: ")
        main()


main()

#121
name_list = ["Chris", "c", "Trox"]

def add_name():
    name = input("Please add a new person to the list: ")
    name_list.append(name)
    return name


def change_name():
    name = input("Which name would you like to change? : ")
    new_name = input("Please enter the new name : ")
    x = 0
    for i in name_list:
        if name in name_list[x]:
            name_list[x] = new_name
            x += 1
        else:
            x += 1
    return name, new_name


def delete_name():
    name = input("Which name would you like to delete? : ")
    name_list.remove(name)
    return name


def view_names():
    print(name_list)
    return name_list


def main():
    again = "y"
    while again == "y":
        print("1) Add name")
        print("2) Change name")
        print("3) Delete name")
        print("4) View the list of names")
        print("5) Exit")
        user = input("Please choose one of the above: ")
        if user == "1":
            add_name()
        elif user == "2":
            change_name()
        elif user == "3":
            delete_name()
        elif user == "4":
            view_names()
        elif user == "5":
            print("The program will now exit...")
            again = "n"
        else:
            print("Choice out of range...")


main()

#122


def add_to_file():
    name = input("Please enter your name: ")
    salary = int(input("Please enter your salary: "))
    file = open("Salaries.csv", "a")
    file.write(f"\nName: {name.title()}, Salary: {salary:,}\n")
    file.close()


def view_records():
    file = open("Salaries.csv", "r")
    print(file.read())
    file.close()


def main():
    again = "y"
    while again == "y":
        print("1) Add to file")
        print("2) View all records")
        print("3) Quit program")
        user = input("Enter the number of your selection: ")

        if user == "1":
            add_to_file()
        elif user == "2":
            view_records()
        elif user == "3":
            print("The program will now exit...")
            again = "n"
        else:
            print("\nChoice out of range!")


main()

#123

def add_to_file():
    name = input("Please enter your name: ")
    salary = int(input("Please enter your salary: "))
    file = open("Salaries.csv", "a")
    file.write(f"\nName: {name.title()}, Salary: {salary:,}\n")
    file.close()
    return name, salary


def view_records():
    file = open("Salaries.csv", "r")
    print(file.read())
    file.close()


def delete_records():
    salaries = []
    file = open("Salaries.csv", "r")
    for row in file:
        salaries.append(row)
    #print(salaries)
    file.close()
    num = 0
    for i in salaries:
        print(num, i)
        num += 1
    user = int(input("Enter the row number to delete: "))
    del salaries[user]
    print(salaries)
    file = open("Salaries.csv", "w")
    for i in salaries:
        file.write(i)
    file.close()


def main():
    again = "y"
    while again == "y":
        print("1) Add to file")
        print("2) View all records")
        print("3) Delete record")
        print("4) Quit program")
        user = input("Enter the number of your selection: ")

        if user == "1":
            add_to_file()
        elif user == "2":
            view_records()
        elif user == "3":
            delete_records()
        elif user == "4":
            print("The program will now exit...")
            again = "n"
        else:
            print("Choice out of range!\n")


main()

#124
from tkinter import *


def click():
    name = entry_box1.get()
    message = str(f"Hello {name}!")
    entry_box2["bg"] = "yellow"
    entry_box2["fg"] = "green"
    entry_box2["text"] = message


window = Tk()
window.title("Welcome screen")
window.geometry("800x400")

label = Label(text = "Enter your name: ")
label.place(x = 200, y = 170, width = 100, height = 25)

entry_box1 = Entry(text = 0)
entry_box1.place(x = 300, y = 170, width = 160, height = 25)

button1 = Button(text = "OK", command = click)
button1.place(x = 480, y = 170, width = 60, height = 25)

entry_box2 = Message(text = "")
entry_box2.place(x = 260, y = 210, width = 250, height = 45)
entry_box2["bg"] = "white"
entry_box2["fg"] = "black"

window.mainloop()

#125
from tkinter import *
from random import randint

# I just thought 2 dice is better than one!!..
def dice():
    number1 = randint(1, 6)
    number2 = randint(1, 6)
    box1["text"] = number1, number2
    box1["bg"] = "green"
    box1["fg"] = "red"


window = Tk()
window.title = ("Lucky Dice")
window.geometry("200x200")

button1 = Button(text = "Lucky Dice", command = dice)
button1.place(x=50, y=50, width=100, height=50)

box1 = Message(text="")
box1.place(x=50, y=100, width=100, height=50)
box1.config(font=("Franklin Gothic Book", 30))

window.mainloop()

#126
from tkinter import *


def add():
    number = int(entry1.get())
    entry1.delete(0, END)
    global sum
    sum += number
    label2["text"] = (f"{sum:,}")


def reset():
    global sum
    sum = 0
    entry1.delete(0, END)
    label2.config(text="0")


sum = 0
window = Tk()
window.title("Simple Adder")
window.geometry("400x400")

laber1 = Label(text = "Enter a number")
laber1.place(x=100, y=50, width=100, height=25)

entry1 = Entry(text=0)
entry1.place(x=200, y=50, width=100, height=25)

button1 = Button(text="Adder", command=add)
button1.place(x=100, y=100, width=200, height=50)

button2 = Button(text="Reset", command=reset)
button2.place(x=100, y=240, width=200, height=50)

label2 = Label(text="")
label2.place(x=100, y=170, width=200, height=50)
label2.config(font=("Franklin Gothic Book", 26))

window.mainloop()

#127
from tkinter import *


def add():
    name = entry1.get()
    name_list.insert(END, name)
    name_list.focus()
    entry1.delete(0, END)


def clear():
    name_list.delete(0, END)


window = Tk()
window.title("Name List")
window.geometry("400x400")

label1 = Label(text="Enter a name in the list:")
label1.config(font=12)
label1.place(x=0, y=40, width=200, height=25)

entry1 = Entry(text=0)
entry1.place(x=190, y=40, width=160, height=25)

button1 = Button(text="Add", command = add)
button1.place(x=355, y=40, width=35, height=25)

button2 = Button(text="Clear", command=clear)
button2.place(x=170, y=330, width=60, height=25)

name_list = Listbox()
name_list.place(x=100, y=100, width=200, height=200)

window.mainloop()

#128
from tkinter import *


def convert_miles():
    miles = entry2.get()
    miles = float(miles)
    kilometers = miles * 1.6093
    label3["text"] = f"{miles} miles are {round(kilometers, 2)} kilometers"
    label3["fg"] = "green"
    label3.config(font=22)
    entry2.delete(0, END)


def convert_km():
    kilometers = entry3.get()
    kilometers = float(kilometers)
    miles = 0.6214 * kilometers
    label3["text"] = f"{kilometers} kilometers are {round(miles, 2)} miles"
    label3["fg"] = "red"
    label3.config(font=22)
    entry3.delete(0, END)


window = Tk()
window.geometry("400x400")
window.title("mile-kilometer converter")

label1 = Label(text="Mile - Kilometer Converter")
label1.place(x=100, y=50, width=200, height=30)
label1.config(font=15)

label2 = Label(text="Enter Miles")
label2.place(x=95, y=100, width=200, height=30)
label2.config(font=15)

label3 = Label(text="")
label3.place(x=40, y=180, width=300, height=30)

label4 = Label(text="Enter Kilometers")
label4.place(x=95, y=230, width=200, height=30)
label4.config(font=15)

label5 = Label(text="")
label5.place(x=95, y=320, width=200, height=30)

entry2 = Entry(text=0)
entry2.place(x=120, y=140, width=150, height=30)

entry3 = Entry(text=0)
entry3.place(x=120, y=270, width=150, height=30)

button1 = Button(text="Convert", command = convert_miles)
button1.place(x=280, y=140, width=100, height=30)
button1.config(font=25)

button2 = Button(text="Convert", command = convert_km)
button2.place(x=280, y=270, width=100, height=30)
button2.config(font=25)

window.mainloop()

#129
from tkinter import *


def check_num():
    data = entry1.get()
    if data.isdigit():
        list1.insert(END, data)
        entry1.delete(0, END)
    else:
        entry1.delete(0, END)


def clear():
    list1.delete(0, END)


window = Tk()
window.geometry("400x400")
window.title("Number checker")

label1 = Label(text="Enter a number: ")
label1.place(x=20, y=60, width=150, height=30)
label1.config(font=22)

entry1 = Entry(text=0)
entry1.place(x=160, y=60, width=150, height=30)

button1 = Button(text="Check it", command=check_num)
button1.place(x=325, y=60, width=60, height=30)

button2 = Button(text="Clear\n List", command=clear)
button2.place(x=330, y=130, width=60, height=60)

list1 = Listbox()
list1.place(x=80, y=130, width=240, height=200)

window.mainloop()

#130
from tkinter import *
import csv


def check_num():
    data = entry1.get()
    if data.isdigit():
        list1.insert(END, data)
        entry1.delete(0, END)
    else:
        entry1.delete(0, END)


def clear():
    list1.delete(0, END)


def save_to_csv():
    file = open("Isdigit.csv", "a")
    tmp_list = list1.get(0, END)
    item = 0
    for x in tmp_list:
        new_record = tmp_list[item]
        file.write(f"\n{str(new_record)}")
        item += 1
    file.close()


window = Tk()
window.geometry("400x400")
window.title("Number checker")

label1 = Label(text="Enter a number: ")
label1.place(x=20, y=60, width=150, height=30)
label1.config(font=22)

entry1 = Entry(text=0)
entry1.place(x=160, y=60, width=150, height=30)

button1 = Button(text="Check it", command=check_num)
button1.place(x=325, y=60, width=60, height=30)

button2 = Button(text="Clear\n List", command=clear)
button2.place(x=330, y=130, width=60, height=60)

button3 = Button(text="Save to\n.csv file", command=save_to_csv)
button3.place(x=330, y=270, width=60, height=60)

list1 = Listbox()
list1.place(x=80, y=130, width=240, height=200)

window.mainloop()

#131
from tkinter import *

# I choose to let the user pick a name for the file, so the variable csv_name must be global
def create_csv():
    global csv_name
    csv_name = entry1.get()
    entry1.delete(0, END)
    file = open(f"{csv_name}.csv", "a")
    file.close()
    return csv_name


def enter_person():
    file = open(f"{csv_name}.csv", "a")
    name = entry2.get()
    age = entry3.get()
    entry2.delete(0, END)
    entry3.delete(0, END)
    file.write(f"\nName: {name}, Age: {age}")
    file.close()


window = Tk()
window.geometry("420x250")
window.title("Create csv file")

label1 = Label(text="Enter the name of\n the new cvs file:")
label1.place(x=10, y=50, width=200, height=30)
label1.config(font=18)

label2 = Label(text="Enter person's name: ")
label2.place(x=5, y=100, width=200, height=30)
label2.config(font=10)

label3 = Label(text="Enter person's age: ")
label3.place(x=5, y=150, width=200, height=30)
label3.config(font=10)

entry1 = Entry(text="")
entry1.place(x=185, y=50, width=150, height=30)

entry2 = Entry(text="")
entry2.place(x=185, y=100, width=150, height=30)

entry3 = Entry(text="")
entry3.place(x=185, y=150, width=150, height=30)

button1 = Button(text="Create \ncsv", command=create_csv)
button1.place(x=345, y=40, width=50, height=50)

button2 = Button(text="Add to \nfile", command=enter_person)
button2.place(x=345, y=115, width=50, height=50)

window.mainloop()

#132
from tkinter import *

# I choose to let the user pick a name for the file, so the variable csv_name must be global
def create_csv():
    global csv_name
    csv_name = entry1.get()
    entry1.delete(0, END)
    file = open(f"{csv_name}.csv", "a")
    file.close()
    return csv_name


def enter_person():
    file = open(f"{csv_name}.csv", "a")
    name = entry2.get()
    age = entry3.get()
    entry2.delete(0, END)
    entry3.delete(0, END)
    file.write(f"\nName: {name}, Age: {age}")
    file.close()


def view_list():
    file = open(f"{csv_name}.csv", "r")
    for item in file:
        list1.insert(END, item)
    file.close()


window = Tk()
window.geometry("420x450")
window.title("Create csv file")

label1 = Label(text="Enter the name of\n the cvs file:")
label1.place(x=10, y=50, width=200, height=30)
label1.config(font=18)

label2 = Label(text="Enter person's name: ")
label2.place(x=5, y=100, width=200, height=30)
label2.config(font=10)

label3 = Label(text="Enter person's age: ")
label3.place(x=5, y=150, width=200, height=30)
label3.config(font=10)

entry1 = Entry(text="")
entry1.place(x=185, y=50, width=150, height=30)

entry2 = Entry(text="")
entry2.place(x=185, y=100, width=150, height=30)

entry3 = Entry(text="")
entry3.place(x=185, y=150, width=150, height=30)

button1 = Button(text="Create / \nOpen csv", command=create_csv)
button1.place(x=345, y=40, width=60, height=50)

button2 = Button(text="Add to \nfile", command=enter_person)
button2.place(x=345, y=115, width=60, height=50)

button3 = Button(text="View \nFull List", command=view_list)
button3.place(x=345, y=200, width=60, height=50)

list1 = Listbox()
list1.place(x=80, y=200, width=260, height=200)

window.mainloop()

#133
from tkinter import *

def press_me():
    name = entry1.get()
    phrase = "Hello " + name
    label2["text"] = phrase

window = Tk()
window.geometry("900x600")
window.wm_iconbitmap("a_verical_lines.ico")
window.config(bg="black")

logo = PhotoImage(file="a_GIFGun_Logo.gif")
logoimage = Label(image=logo)
logoimage.place(x=100, y=50, width=700, height=216)

label1 = Label(text="Enter your name", font='Helvetica 12', foreground="white", bg="black", bd=4)
label1.place(x=250, y=350, width=150, height=30)

label2 = Label(text="", bg="white", justify=CENTER, font=12)
label2.place(x=400, y=400, width=200, height=30)

entry1 = Entry(text="", bg="white", justify=CENTER, font=12)
entry1.place(x=400, y=350, width=200, height=30)

button1 = Button(text="Press me", command = press_me)
button1.place(x=250, y=400, width=140, height=30)

window.mainloop()

#134
from tkinter import *
from random import randint


def random_nums():
    photo1 = PhotoImage(file="")
    photobox = Label(window, image=photo1, bg="gold")
    photobox.image = photo1
    photobox.place(x=125, y=290, width=50, height=50)
    num1 = randint(10, 50)
    label2["text"] = num1
    num2 = randint(10, 50)
    label3["text"] = num2
    return num1, num2


def check_it():
    num1 = int(label2["text"])
    num2 = int(label3["text"])
    total = num1 + num2
    answer = int(entry1.get())
    if answer == total:
        photo1 = PhotoImage(file="a_right2.gif")
        photobox = Label(window, image=photo1)
        photobox.image = photo1
        photobox.place(x=125, y=290, width=50, height=50)
    else:
        photo1 = PhotoImage(file="a_wrong2.gif")
        photobox = Label(window, image=photo1)
        photobox.image = photo1
        photobox.place(x=125, y=290, width=50, height=50)


def next():
    random_nums()
    entry1.delete(0, END)


def exit():
    quit()


window = Tk()
window.geometry("510x500")
window.title("Add the numbers")
window.config(bg="gold")

label1 = Label(text="Add the two numbers below", font="Helvetica 14 bold", bg="cyan", borderwidth=6, relief="raised")
label1.place(x=100, y=40, width=300, height=70)

label2 = Label(text="", font="Helvetica 33 bold", bg="cyan", borderwidth=6, relief="raised")
label2.place(x=160, y=130, width=75, height=75)

label3 = Label(text="", font="Helvetica 33 bold", bg="cyan", borderwidth=6, relief="raised")
label3.place(x=265, y=130, width=75, height=75)

label4 = Label(text="Your Answer", font="Helvetica 14 bold", bg="cyan", borderwidth=6, relief="raised")
label4.place(x=150, y=230, width=200, height=40)

entry1 = Entry(text="", font="Helvetica 20 bold", justify=CENTER, bd=3)
entry1.place(x=200, y=290, width=100, height=50)

button1 = Button(text="Check it", font="Helvetica 14", justify=CENTER, bd=4, command=check_it)
button1.place(x=320, y=290, width=90, height=50)

button2 = Button(text="Next", font="Helvetica 14", justify=CENTER, bd=4, command=next)
button2.place(x=320, y=350, width=90, height=50)

button3 = Button(text="Exit", font="Helvetica 14", justify=CENTER, bd=4, command=exit)
button3.place(x=105, y=350, width=80, height=50)

random_nums()

window.mainloop()

#135
from tkinter import *


def click_me():
    window.config(bg=variable.get())


window = Tk()
window.geometry("400x400")
window.title("BackGroynd Colour Changer")
window.config(bg="white")

variable = StringVar()
variable.set("white")
colours = ["white", "blue", "green", "red", "cyan", "purple1"]

dropmenu1 = OptionMenu(window, variable, *colours)
dropmenu1.config(font='Helvetica 10 bold')
dropmenu1.place(x=140, y=30, width=80, height=30)

button1 = Button(text="Click Me", command=click_me)
button1.place(x=240, y=30, width=70, height=28)

window.mainloop()

#136
from tkinter import *


def add():
    person = f"{entry1.get()}, {variable.get()}"
    listbox.insert(END, person)
    entry1.delete(0, END)
    variable.set("Pick one")


window = Tk()
window.geometry("470x400")
window.config(bg="cyan2")

label1 = Label(text="Enter your name", font=12, bg="pale green", borderwidth=4, relief="raised")
label1.place(x=60, y=50, width=130, height=35)

label2 = Label(text="Choose Gender", font=12, bg="pale green", borderwidth=4, relief="raised")
label2.place(x=230, y=50, width=130, height=35)

entry1 = Entry(text="", justify=CENTER, font=12)
entry1.place(x=60, y=100, width=130, height=30)

variable = StringVar()
variable.set("Pick one")
entry2 = OptionMenu(window, variable, "male", "female")
entry2.config(font=12)
entry2.place(x=245, y=100, width=100, height=30)

listbox = Listbox()
listbox.config(font=12, bd=5)
listbox.place(x=80, y=160, width=320, height=200)

button1 = Button(text="Add", font='Helvetica 17 bold', bd=6, command=add)
button1.place(x=375, y=50, width=90, height=80)

window.mainloop()

#137
from tkinter import *


def add():
    person = f"{entry1.get()}, {variable.get()}"
    listbox.insert(END, person)
    entry1.delete(0, END)
    variable.set("Pick one")
    file = open("names_137_pbe.txt", "a")
    file.write(person + "\n")
    file.close()


def txt_file():
    listbox.delete(0, END)
    file = open("names_137_pbe.txt", "r")
    for item in file:
        listbox.insert(END, item)
    file.close()


window = Tk()
window.geometry("470x400")
window.config(bg="cyan2")

label1 = Label(text="Enter your name", font=12, bg="pale green", borderwidth=4, relief="raised")
label1.place(x=60, y=50, width=130, height=35)

label2 = Label(text="Choose Gender", font=12, bg="pale green", borderwidth=4, relief="raised")
label2.place(x=230, y=50, width=130, height=35)

entry1 = Entry(text="", justify=CENTER, font=12)
entry1.place(x=60, y=100, width=130, height=30)

variable = StringVar()
variable.set("Pick one")
entry2 = OptionMenu(window, variable, "male", "female")
entry2.config(font=12)
entry2.place(x=245, y=100, width=100, height=30)

listbox = Listbox()
listbox.config(font=12, bd=5)
listbox.place(x=80, y=160, width=320, height=200)

button1 = Button(text="Add", font='Helvetica 17 bold', bd=6, command=add)
button1.place(x=375, y=50, width=90, height=80)

button2 = Button(text="View\n txt file", font='Helvetica 10 bold', bd=6, command=txt_file)
button2.place(x=405, y=160, width=60, height=60)

window.mainloop()

#138
from tkinter import *


def click():
    photo = PhotoImage(file=f"{variable.get()}.gif")
    photobox = Label(window, image=photo)
    photobox.image = photo
    photobox.place(x=100, y=120, width=400, height=400)


window = Tk()
window.geometry("600x600")
window.title("Pick a picture")
window.config(bg="yellow")

label1 = Label(text="Pick one", justify=CENTER, bg="white", font="Helvetica 12 bold", bd=4, relief="raised")
label1.place(x=250, y=20, width=100, height=35)

variable = IntVar()
variable.set(1)
option = range(1, 6)
entry1 = OptionMenu(window, variable, *option)
entry1.place(x=250, y=60, width=100, height=35)
entry1.config(justify=CENTER, bg="white", font="Helvetica 12 bold")

button1 = Button(text="OK", font="Helvetica 12 bold", bg="white", bd=4, relief="raised", command=click)
button1.place(x=360, y=60, width=60, height=33)

photo = PhotoImage(file="1.gif")
photobox = Label(window, image=photo)
photobox.image = photo
photobox.place(x=100, y=120, width=400, height=400)

window.mainloop()

#139
import sqlite3

with sqlite3.connect("PhoneBook.db") as db:
    cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS PhoneBook(
            id integer PRIMARY KEY,
            First_name text NOT NULL,
            Surname text NOT NULL,
            Phone_Number integer)
            ''')

cursor.execute('''INSERT INTO PhoneBook(id, First_name, Surname, Phone_Number) VALUES
                ("1", "Simon", "Howels", "01223 125458"),
                ("2", "Karen", "Phillips", "01954 254569"),
                ("3", "Darren", "Smith", "01583 524596"),
                ("4", "Anne", "Jones", "01323 452156"),
                ("5", "Mark", "Smith", "01223 854897")
                ''')
db.commit()
db.close()

#140
import sqlite3


def main():
    print("\nMain Menu\n")
    print("1) View phone book")
    print("2) Add to phone book")
    print("3) Search for surname")
    print("4) Delete person from phone book")
    print("5) Quit\n")
    selection = input("Enter your selection: ")

    if selection == "1":
        with sqlite3.connect("PhoneBook.db") as db:
            cursor = db.cursor()

        data = cursor.execute("SELECT * FROM PhoneBook")
        print("The PhoneBook database:")
        for i in data:
            print(i)
        db.close()
        main()

    elif selection == "2":
        with sqlite3.connect("PhoneBook.db") as db:
            cursor = db.cursor()

        new_id = input("Enter a new id: ")
        new_first_name = input("Enter new first name: ")
        new_surname = input("Enter new surname: ")
        new_phone_number = input("Enter new phone number: ")

        cursor.execute("INSERT INTO PhoneBook(id, First_name, Surname, Phone_Number) VALUES (?,?,?,?)",
                       (new_id, new_first_name, new_surname, new_phone_number))
        db.commit()
        db.close()
        main()

    elif selection == "3":
        with sqlite3.connect("PhoneBook.db") as db:
            cursor = db.cursor()

        which_surname = input("Enter the surname: ").title()
        surname = cursor.execute("SELECT * FROM PhoneBook WHERE Surname = ?", [which_surname,])
        for i in surname.fetchall():
            print(i)
        main()

    elif selection == "4":
        with sqlite3.connect("PhoneBook.db") as db:
            cursor = db.cursor()

        delete_id = input("Enter the id to delete: ")
        cursor.execute("DELETE FROM PhoneBook WHERE id = ?", [delete_id,])
        db.commit()
        db.close()
        print(f"Id No {delete_id} has been deleted")
        main()

    elif selection == "5":
        exit()

    else:
        print("Selection out of range!")
        main()

main()

#141
import sqlite3

with sqlite3.connect("bookinfo.db") as db:
    cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS authors(
                Name text NOT NULL,
                Place_of_birth text NOT NULL)
                ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS books(
                id integer PRIMARY KEY,
                Title text NOT NULL,
                Author text NOT NULL,
                Date_Published integer)
                ''')

cursor.execute('''INSERT INTO authors(Name, Place_of_birth) VALUES
                ("Agatha Christie", "Torquay"),
                ("Cecelia Ahern", "Dublin"),
                ("J.K.Rowling", "Bristol"),
                ("Oscar Wilde", "Dublin")
                ''')

cursor.execute('''INSERT INTO books(id, Title, Author, Date_Published) VALUES
                ("1", "De Profundis", "Oscar Wilde", "1905"),
                ("2", "Harry Potter and the chambers of secrets", "J.K.Rowling", "1998"),
                ("3", "Harry Potter and the prisoner of Askaban", "J.K.Rowling", "1999"),
                ("4", "Lyrebird", "Cecelia Ahern", "2017"),
                ("5", "Murder on the Orient Express", "Agatha Christie", "1934"),
                ("6", "Perfect", "Cecelia Ahern", "2017"),
                ("7", "The murble collector", "Cecelia Ahern", "2016"),
                ("8", "The murder on the links", "Agatha Christie", "1923"),
                ("9", "The picture of Dorian Grey", "Oscar Wilde", "1890"),
                ("10", "The secret adversary", "Agatha Christie", "1921"),
                ("11", "The seven dials mystery", "Agatha Christie", "1929"),
                ("12", "The year I met you", "Cecelia Ahern", "2014")
                ''')

db.commit()
db.close()

#142
import sqlite3

with sqlite3.connect("bookinfo.db") as db:
    cursor = db.cursor()

authors = cursor.execute("SELECT * FROM authors")
for i in authors:
    print(i)

place_of_birth = input("Enter place of birth: ").title()

author = cursor.execute('''SELECT books.Title, books.Author, books.Date_Published FROM books, authors 
WHERE authors.Name=books.Author AND Place_of_birth=?''', [place_of_birth])
for i in author:
    print(i)

#143
import sqlite3

year_selected = int(input("Enter a year: "))

with sqlite3.connect("bookinfo.db") as db:
    cursor = db.cursor()

books = cursor.execute('''SELECT Title, Author, Date_Published FROM books WHERE Date_Published>? 
                        ORDER BY Date_Published''', [year_selected])
for i in books:
    print(i)

#144
import sqlite3

author = input("Select an author: ")

with sqlite3.connect("bookinfo.db") as db:
    cursor = db.cursor()

author_books = cursor.execute('''SELECT * FROM books WHERE Author=?''', [author])


file = open("author_books.txt", "w")
for i in author_books:
    print(i)
    file.write(f"{str(i[0])} - {str(i[1])} - {str(i[2])} - {str(i[3])}\n")

file.close()

#145
from tkinter import *
import sqlite3


def add():
    with sqlite3.connect("test_scores.db") as db:
        cursor = db.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS test_scores(
    name text NOT NULL,
    score real NOT NULL)
    ''')
    cursor.execute('''INSERT INTO test_scores(name, score) VALUES(?,?)''', (entry1.get(), entry2.get()))
    db.commit()
    db.close()


def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)


window = Tk()
window.geometry("450x225")
window.title("TestScores")
window.config(bg="light cyan")

label1 = Label(text="Enter student's name: ", font=10, bg="light cyan")
label1.place(x=50, y=50, width=150, height=25)

entry1 = Entry(text="", font=10, justify=CENTER)
entry1.place(x=205, y=50, width=170, height=25)

label2 = Label(text="Enter student's grade: ", font=10, bg="light cyan")
label2.place(x=50, y=100, width=150, height=25)

entry2 = Entry(text="", font=10, justify=CENTER)
entry2.place(x=205, y=100, width=170, height=25)

button1 = Button(text="Add", command=add)
button1.place(x=205, y=150, width=70, height=25)

button2 = Button(text="Clear", command=clear)
button2.place(x=300, y=150, width=70, height=25)

window.mainloop()

# 146
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F",
            "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"," "]


def encode():
    new_phrase = []
    phrase = input("Please enter a phrase to encode: ")
    pusher = int(input("Please enter encoding key (only integers allowed): "))
    words = phrase.split()
    for word in words:
        for letter in word:
            if letter in alphabet:
                new_index = (pusher + alphabet.index(letter)) % 62
                new_phrase.append(alphabet[new_index])
            else:
                print(f"'{letter}' not allowed")
        new_phrase.append(" ")
    result = "".join(new_phrase)
    print(f"\nYour encoded phrase is: '{result[0:-1]}' and your key is: {pusher}\n")


def decode():
    new_phrase = []
    phrase = input("Please enter a phrase to decode: ")
    pusher = int(input("Please enter decoding key (only integers allowed): "))
    words = phrase.split()
    for word in words:
        for letter in word:
            if letter in alphabet:
                new_index = (-pusher + alphabet.index(letter)) % 62
                new_phrase.append(alphabet[new_index])
            else:
                print(f"'{letter}' not allowed")
        new_phrase.append(" ")
    result = "".join(new_phrase)
    print(f"\nYour decoded phrase is: '{result[0:-1]}' \n")


def main():
    switch = "on"
    while switch == "on":
        print("1) Make o code")
        print("2) Decode a message")
        print("3) Quit")
        selection = input("\nEnter your selection: ")
        if selection == "1":
            encode()
        elif selection == "2":
            decode()
        elif selection == "3":
            switch = "off"
        else:
            print("\nSelection out of range!\n")


main()

# 147
import random

available_colours = ["red", "blue", "green", "yellow", "white", "brown"]
pc_colours = random.choices(available_colours, k=4)
# print(pc_colours)
user_colours = []


def main():
    colour1 = input("Enter your 1st colour: ")
    user_colours.append(colour1)
    colour2 = input("Enter your 2nd colour: ")
    user_colours.append(colour2)
    colour3 = input("Enter your 3rd colour: ")
    user_colours.append(colour3)
    colour4 = input("Enter your 4th colour: ")
    user_colours.append(colour4)
    finish = "no"
    x = 1
    while finish == "no":
        print(f"\nRound: {x}\n")
        if user_colours[0] == pc_colours[0] and user_colours[1] == pc_colours[1] and user_colours[2] == pc_colours[2] \
                and user_colours[3] == pc_colours[3]:
            finish = "yes"
        if user_colours[0] == pc_colours[0]:
            print(f"Correct colour 1 '{user_colours[0]}' in the correct place")
        elif user_colours[0] in pc_colours:
            colour1 = input(f"Correct colour 1 '{user_colours[0]}' in the wrong place, try again: ")
            user_colours[0] = colour1
        elif user_colours[0] not in pc_colours:
            colour1 = input(f"Colour 1 '{user_colours[0]}' not selected by the computer, try again: ")
            user_colours[0] = colour1
        if user_colours[1] == pc_colours[1]:
            print(f"Correct colour 2 '{user_colours[1]}' in the correct place")
        elif user_colours[1] in pc_colours:
            colour2 = input(f"Correct colour 2 '{user_colours[1]}' in the wrong place, try again: ")
            user_colours[1] = colour2
        elif user_colours[1] not in pc_colours:
            colour2 = input(f"Colour 2 '{user_colours[1]}' not selected by the computer, try again: ")
            user_colours[1] = colour2
        if user_colours[2] == pc_colours[2]:
            print(f"Correct colour 3 '{user_colours[2]}' in the correct place")
        elif user_colours[2] in pc_colours:
            colour3 = input(f"Correct colour 3 '{user_colours[2]}' in the wrong place, try again: ")
            user_colours[2] = colour3
        elif user_colours[2] not in pc_colours:
            colour3 = input(f"Colour 3 '{user_colours[2]}' not selected by the computer, try again: ")
            user_colours[2] = colour3
        if user_colours[3] == pc_colours[3]:
            print(f"Correct colour 4 '{user_colours[3]}' in the correct place")
        elif user_colours[3] in pc_colours:
            colour4 = input(f"Correct colour 4 '{user_colours[3]}' in the wrong place, try again: ")
            user_colours[3] = colour4
        elif user_colours[3] not in pc_colours:
            colour4 = input(f"Colour 4 '{user_colours[3]}' not selected by the computer, try again: ")
            user_colours[3] = colour4
        x += 1
    print("\nMission completed successfully! Bravo!")


main()

print(user_colours)

# 148
import csv

new_user = []
new_password = ""


def create_id():
    users_ids = []
    global new_user
    new_user = []
    enter_id = input("Enter new ID: ")
    file = open("passwords.csv", "r")
    reader = csv.reader(file)
    full_csv = list(reader)
    for i in full_csv:
        if not i:
            full_csv.remove(i)
    for i in full_csv:
        try:
            users_ids.append(i[0])
        except IndexError:
            pass
    while enter_id in users_ids:
        enter_id = input("ID already in use, enter different ID: ")
    new_user.append(enter_id)
    file.close()
    create_password()
    write_to_csv()
    main()


def create_password():
    points = 0
    password = input("Enter your password: ")

    len_list = len(password)
    upper = 0
    lower = 0
    numbers = 0
    special_char = 0

    for i in password:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        if i.isnumeric():
            numbers += 1
        if not i.isalnum():
            special_char += 1

    if len_list > 7:
        points += 1
    if upper > 0:
        points += 1
    if lower > 0:
        points += 1
    if numbers > 0:
        points += 1
    if special_char > 0:
        points += 1

    if points < 3:
        print("Weak password, please try again.")
        create_password()
    elif points == 3 or points == 4:
        response = input("This password could be improved. Do you want to try again? (y/n): \n")
        if response == "y":
            create_password()
        else:
            new_user.append(password)
    elif points == 5:
        print("You have selected a strong password!\n")
        new_user.append(password)


def write_to_csv():
    file = open("passwords.csv", "a")
    reader = csv.reader(file)
    file.write(f"\n{new_user[0]},")
    file.write(f"{new_user[1]}")
    file.close()


def change_password():
    user_id = input("Enter the user ID: ")
    file = open("passwords.csv", "r")
    reader = csv.reader(file)
    full_csv = list(reader)  # The way to create list from csv file
    #print(full_csv)
    for i in full_csv:
        try:
            if user_id in i[0]:
                check_new_password()
                i[1] = new_password
        except IndexError:
            pass
    #print(full_csv)
    file.close()
    for i in full_csv:
        if [] in full_csv:
            full_csv.remove([])
    file = open("passwords.csv", "w")
    for i in full_csv:
        file.write(f"{str(i[0])},{str(i[1])}\n")
    file.close()
    main()


def check_new_password():
    global new_password
    points = 0
    password = input("Enter the new password: ")

    len_list = len(password)
    upper = 0
    lower = 0
    numbers = 0
    special_char = 0

    for i in password:
        if i.isupper():
            upper += 1
        if i.islower():
            lower += 1
        if i.isnumeric():
            numbers += 1
        if not i.isalnum():
            special_char += 1

    if len_list > 7:
        points += 1
    if upper > 0:
        points += 1
    if lower > 0:
        points += 1
    if numbers > 0:
        points += 1
    if special_char > 0:
        points += 1

    if points < 3:
        print("Weak password, please try again.")
        create_password()
    elif points == 3 or points == 4:
        response = input("This password could be improved. Do you want to try again? (y/n): \n")
        if response == "y":
            check_new_password()
        else:
            new_password = password
    elif points == 5:
        print("You have selected a strong password!\n")
        new_password = password


def display_users_id():
    ids = []
    file = open("passwords.csv", "r")
    reader = csv.reader(file)
    full_csv = list(reader)
    for i in full_csv:
        if not i:
            full_csv.remove(i)
    for i in full_csv:
        try:
            ids.append(i[0])
        except IndexError:
            pass
    file.close()
    print(f"\nStored id's: {ids}\n")
    main()

def display_password():
    file = open("passwords.csv", "r")
    reader = csv.reader(file)
    full_csv = list(reader)
    for i in full_csv:
        if not i:
            full_csv.remove(i)
    #print(full_csv)
    user_id = input("Enter the user ID: ")
    x = 0
    for i in full_csv:
        if i[0] == user_id:
            print(f"The ID '{i[0]}' has password '{i[1]}'\n")
            x += 1
    if x == 0:
        print(f"There is no ID '{user_id}'\n")
    file.close()
    main()


def main():
    print("1) Create a new user ID")
    print("2) Change a password")
    print("3) Display all user ID's")
    print("4) Display password for specific ID")
    print("5) Quit")

    selection = input("\nEnter selection: ")

    if selection == "1":
        create_id()
    elif selection == "2":
        change_password()
    elif selection == "3":
        display_users_id()
    elif selection == "4":
        display_password()
    elif selection == "5":
        exit()
    else:
        print("\nSelection out of range!\n")
        main()


main()

# 149
from tkinter import *


def times_table():
    num = int(entry1.get())
    for i in range(1, 13):
        label_main.Listbox(END, f"{i} x {num} = {i * num}")


def clear():
    entry1.delete(0, END)
    label_main.delete(0,'end')


window = Tk()
window.geometry("540x450")
window.title("Times Table")

label1 = Label(text="Enter a number", font=12)
label1.place(x=30, y=40, width=150, height=25)

entry1 = Entry(text="", justify=CENTER, font=12)
entry1.place(x=170, y=40, width=150, height=25)

label_main = Listbox(bg="white", font=10)
label_main.place(x=170, y=75, width=150, height=300)

button1 = Button(text="View Times Table", font=10, command=times_table)
button1.place(x=330, y=38, width=150, height=28)

button2 = Button(text="Clear", font=10, command=clear)
button2.place(x=330, y=75, width=150, height=28)

window.mainloop()

# 150
from tkinter import *
import sqlite3
import os

with sqlite3.connect("paintings.db") as db:
    cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS artists_contact_details(
                artist_id integer NOT NULL PRIMARY KEY,
                name text NOT NULL,
                address text NOT NULL,
                town text,
                county text NOT NULL,
                postcode text NOT NULL)
                ''')

cursor.execute('''CREATE TABLE IF NOT EXISTS pieces_of_art(
                piece_id integer NOT NULL PRIMARY KEY,
                artist_id integer NOT NULL,
                title text NOT NULL,
                medium text NOT NULL,
                price integer NOT NULL)
                ''')

# cursor.execute('''INSERT INTO artists_contact_details VALUES
# ("1", "Martin Leighton", "5 Park Place", "Peterborough", "Cambridgeshire", "PE32 5LP"),
# ("2", "Eva Czarniecka", "77 Warner Close", "Chelmsford", "Essex", "CM22 5FT"),
# ("3", "Roxy Parkin", "90 Hindhead Road", NULL, "London", "SE12 6WM"),
# ("4", "Nigel Farnworth", "41 Whitby Road", "Huntly", "Aberdeenshire", "AB54 5PN"),
# ("5", "Teresa Tanner", "70 Guild Street", NULL, "London", "NW7 1SP")
#
# ''')

# cursor.execute('''INSERT INTO pieces_of_art VALUES
# ("1", "5", "Woman with black Labrador", "Oil", "220"),
# ("2", "5", "Bees & thistles", "Watercolour ", "85"),
# ("3", "2", "A stroll to Westminster", "Ink", "190"),
# ("4", "1", "African giant", "Oil", "800"),
# ("5", "3", "Water daemon", "Acrylic", "1700"),
# ("6", "4", "A seagull", "Watercolour", "35"),
# ("7", "1", "Three friends", "Oil", "1800"),
# ("8", "2", "Summer breeze 1", "Acrylic ", "1350"),
# ("9", "4", "Mr Hamster", "Watercolour", "35"),
# ("10", "1", "Pulpit Rock, Dorset", "Oil", "600"),
# ("11", "5", "Trawler Dungeness beach", "Oil", "195"),
# ("12", "2", "Dance in the snow", "Oil", "250"),
# ("13", "4", "St Tropez port", "Ink", "45"),
# ("14", "3", "Pirate assassin", "Acrylic", "420"),
# ("15", "1", "Morning walk", "Oil", "800"),
# ("16", "4", "A baby barn swallow", "Watercolour", "35"),
# ("17", "4", "The old working mills", "Ink", "395")
# ''')
#
# db.commit()

def search():
    if var_artist_medium.get() == "artist":
        search_by_artist()
    elif var_artist_medium.get() == "medium":
        search_by_medium()
    elif var_artist_medium.get() == "price >":
        search_by_price_greater_than()
    elif var_artist_medium.get() == "price <":
        search_by_price_less_than()

def search_by_artist():
    artists = cursor.execute('''SELECT pieces_of_art.piece_id, pieces_of_art.artist_id, pieces_of_art.title, 
    pieces_of_art.medium, pieces_of_art.price FROM pieces_of_art,artists_contact_details WHERE 
    artists_contact_details.name=? COLLATE NOCASE AND artists_contact_details.artist_id=pieces_of_art.artist_id''', [entry2.get()])
    for i in artists.fetchall():
        listbox1.insert(END, f"Piece id: {i[0]}, Piece title: '{i[2]}', Medium: {i[3]}, Price: {i[4]:,}$")


def search_by_medium():
    medium = cursor.execute('''SELECT artists_contact_details.name, pieces_of_art.title, pieces_of_art.medium, 
    pieces_of_art.price FROM pieces_of_art, artists_contact_details WHERE 
    pieces_of_art.artist_id=artists_contact_details.artist_id AND pieces_of_art.medium=? COLLATE NOCASE''', [entry2.get()])
    for i in medium.fetchall():
        listbox1.insert(END, f"Artist: {i[0]}, Piece title: '{i[1]}', Medium: {i[2]}, Price: {i[3]:,}$")


def search_by_price_greater_than():
    price_greater_than = cursor.execute('''SELECT artists_contact_details.name, pieces_of_art.title, pieces_of_art.medium, 
    pieces_of_art.price FROM pieces_of_art, artists_contact_details WHERE 
    pieces_of_art.artist_id=artists_contact_details.artist_id AND pieces_of_art.price>=? ORDER BY price''', [entry2.get()])
    for i in price_greater_than.fetchall():
        listbox1.insert(END, f"Artist: {i[0]}, Piece title: '{i[1]}', Medium: {i[2]}, Price: {i[3]:,}$")


def search_by_price_less_than():
    price_less_than = cursor.execute('''SELECT artists_contact_details.name, pieces_of_art.title, pieces_of_art.medium, 
    pieces_of_art.price FROM pieces_of_art, artists_contact_details WHERE 
    pieces_of_art.artist_id=artists_contact_details.artist_id AND pieces_of_art.price<=? ORDER BY price''', [entry2.get()])
    for i in price_less_than.fetchall():
        listbox1.insert(END, f"Artist: {i[0]}, Piece title: '{i[1]}', Medium: {i[2]}, Price: {i[3]:,}$")


def print_all_pieces():
    all = cursor.execute('''SELECT artists_contact_details.name, pieces_of_art.title, pieces_of_art.medium, 
    pieces_of_art.price, pieces_of_art.piece_id FROM pieces_of_art, artists_contact_details WHERE 
    pieces_of_art.artist_id=artists_contact_details.artist_id''')
    for i in all.fetchall():
        listbox1.insert(END, f"{i[4]} / Artist: {i[0]}, Piece title: '{i[1]}', Medium: {i[2]}, Price: {i[3]:,}$")


def print_all_artists():
    all = cursor.execute('''SELECT * FROM artists_contact_details''')
    for i in all.fetchall():
        listbox1.insert(END, f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}")


def add_piece_of_art():
    try:
        cursor.execute('''INSERT INTO pieces_of_art VALUES (?,?,?,?,?)''', (entry11.get(), entry12.get(), entry13.get(),
                                                                            entry14.get(), entry15.get()))
        db.commit()
        new_window.destroy()
    except sqlite3.IntegrityError as ie:
        label_error = Label(new_window, text=ie, bg="white", font=12)
        label_error.place(x=160, y=85, width=300, height=30)


def new_window_1():
    global new_window
    new_window = Toplevel(window)
    new_window.geometry("625x140")
    new_window.title("Insert new piece of art")
    new_window.config(bg="SeaGreen3")
    label11 = Label(new_window, text="Piece id", font='Helvetica 12', bg="orange", borderwidth=3, relief="raised")
    label11.place(x=5, y=5, width=75, height=30)
    label12 = Label(new_window, text="Artist id", font='Helvetica 12', bg="orange", borderwidth=3, relief="raised")
    label12.place(x=85, y=5, width=75, height=30)
    label13 = Label(new_window, text="Title", font='Helvetica 12', bg="orange", borderwidth=3, relief="raised")
    label13.place(x=165, y=5, width=220, height=30)
    label14 = Label(new_window, text="Medium", font='Helvetica 12', bg="orange", borderwidth=3, relief="raised")
    label14.place(x=390, y=5, width=150, height=30)
    label15 = Label(new_window, text="Price", font='Helvetica 12', bg="orange", borderwidth=3, relief="raised")
    label15.place(x=545, y=5, width=75, height=30)
    global entry11
    global entry12
    global entry13
    global entry14
    global entry15
    entry11 = Entry(new_window, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry11.place(x=5, y=40, width=75, height=30)
    entry12 = Entry(new_window, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry12.place(x=85, y=40, width=75, height=30)
    entry13 = Entry(new_window, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry13.place(x=165, y=40, width=220, height=30)
    entry14 = Entry(new_window, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry14.place(x=390, y=40, width=150, height=30)
    entry15 = Entry(new_window, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry15.place(x=545, y=40, width=75, height=30)
    button11 = Button(new_window, text="Enter", bd=6, font='Helvetica 12 bold', foreground="black", command=add_piece_of_art)
    button11.place(x=540, y=80, width=80, height=45)


def add_artist():
    try:
        cursor.execute('''INSERT INTO artists_contact_details VALUES (?,?,?,?,?,?)''', (entry21.get(), entry22.get(),
                                                                                        entry23.get(), entry24.get(),
                                                                                        entry25.get(), entry26.get()))
        db.commit()
        new_window2.destroy()
    except sqlite3.IntegrityError as ie:
        label_error = Label(new_window2, text=ie, bg="white", font=12)
        label_error.place(x=250, y=90, width=500, height=30)


def new_window_2():
    global new_window2
    new_window2 = Toplevel(window)
    new_window2.geometry("1025x140")
    new_window2.title("Insert new Artist")
    new_window2.config(bg="SeaGreen3")
    label21 = Label(new_window2, text="Artist id", font='Helvetica 12', bg="orange", borderwidth=3, relief="raised")
    label21.place(x=5, y=5, width=75, height=30)
    label22 = Label(new_window2, text="Name", font='Helvetica 12', bg="orange", borderwidth=3, relief="raised")
    label22.place(x=85, y=5, width=195, height=30)
    label23 = Label(new_window2, text="Address", font='Helvetica 12', bg="orange", borderwidth=3, relief="raised")
    label23.place(x=285, y=5, width=195, height=30)
    label24 = Label(new_window2, text="Town", font='Helvetica 12', bg="orange", borderwidth=3, relief="raised")
    label24.place(x=485, y=5, width=195, height=30)
    label25 = Label(new_window2, text="County", font='Helvetica 12', bg="orange", borderwidth=3, relief="raised")
    label25.place(x=680, y=5, width=195, height=30)
    label26 = Label(new_window2, text="Postcode", font='Helvetica 12', bg="orange", borderwidth=3, relief="raised")
    label26.place(x=880, y=5, width=140, height=30)
    global entry21
    global entry22
    global entry23
    global entry24
    global entry25
    global entry26
    entry21 = Entry(new_window2, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry21.place(x=5, y=40, width=75, height=30)
    entry22 = Entry(new_window2, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry22.place(x=85, y=40, width=195, height=30)
    entry23 = Entry(new_window2, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry23.place(x=285, y=40, width=195, height=30)
    entry24 = Entry(new_window2, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry24.place(x=485, y=40, width=195, height=30)
    entry25 = Entry(new_window2, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry25.place(x=680, y=40, width=195, height=30)
    entry26 = Entry(new_window2, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry26.place(x=880, y=40, width=140, height=30)
    button21 = Button(new_window2, text="Enter", bd=6, font='Helvetica 12 bold', foreground="black", command=add_artist)
    button21.place(x=910, y=80, width=80, height=45)


def delete_piece():
    try:
        sold = cursor.execute('''SELECT artists_contact_details.name, pieces_of_art.title, pieces_of_art.medium, 
            pieces_of_art.price, pieces_of_art.piece_id FROM pieces_of_art, artists_contact_details WHERE 
            pieces_of_art.piece_id=? AND pieces_of_art.artist_id=artists_contact_details.artist_id''', [entry31.get()])
        file = open("art_gallery_sold.txt", "a")
        for i in sold:
            file.write(f"\nSold: Id:{i[4]} / Artist: {i[0]}, Piece title: '{i[1]}', Medium: {i[2]}, Price: {i[3]:,}$")
        file.close()
        cursor.execute('''DELETE FROM pieces_of_art WHERE piece_id=?''', [entry31.get()])
        db.commit()
        new_window3.destroy()

    except sqlite3.IntegrityError as ie:
        label_error = Label(new_window3, text=ie, bg="white", font=12)
        label_error.place(x=20, y=45, width=240, height=30)


def new_window_3():
    global new_window3
    new_window3 = Toplevel(window)
    new_window3.geometry("295x100")
    new_window3.title("Delete a piece of art")
    new_window3.config(bg="IndianRed3")
    label21 = Label(new_window3, text="Enter piece id to remove", font='Helvetica 12 bold', bg="yellow", borderwidth=3, relief="raised")
    label21.place(x=5, y=5, width=220, height=30)
    global entry31
    entry31 = Entry(new_window3, text="", justify=CENTER, font='Helvetica 12', bd=2)
    entry31.place(x=230, y=5, width=60, height=30)
    button31 = Button(new_window3, text="Enter", bd=6, font='Helvetica 11 bold', foreground="black", command=delete_piece)
    button31.place(x=230, y=50, width=60, height=45)


def clear():
    entry2.delete(0, END)
    listbox1.delete(0, END)


def about():
    os.startfile("art_gallery_database.txt")


window = Tk()
window.geometry("1020x640")
window.title("Art Gallery Database")
image = "aSNGHeader_01.png"
filename = PhotoImage(file=image)
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label1 = Label(text="Art Gallery Database", font="Helvetica 30 bold", fg="black", justify=CENTER, bd=6, relief="raised", bg="SteelBlue1")
label1.place(x=285, y=50, width=450, height=50)

label2 = Label(text="Search the database by ", font='Helvetica 12 bold', fg="black", justify=CENTER, bd=6, relief="raised", bg="SteelBlue1")
label2.place(x=80, y=145, width=220, height=35)

var_artist_medium = StringVar()
var_artist_medium.set("artist")
artist_mediums = ("artist", "medium", "price >", "price <")
entry1 = OptionMenu(window, var_artist_medium, *artist_mediums)
entry1.config(justify=CENTER, font='Helvetica 12', bg="white")
entry1.place(x=315, y=145, width=100, height=33)

entry2 = Entry(text="", justify=CENTER, font='Helvetica 12')
entry2.place(x=430, y=145, width=200, height=33)

button1 = Button(text="Go", font='Helvetica 12 bold', bd=4, bg="grey66", command=search)
button1.place(x=645, y=140, width=80, height=45)

button2 = Button(text="Clear", font='Helvetica 12 bold', bd=4, bg="grey76", command=clear)
button2.place(x=738, y=140, width=80, height=45)

button3 = Button(text="If you want to PRINT the \nthe full list of art Pieces,\n press here",
                 font='Helvetica 10 bold', bd=5, bg="khaki", command=print_all_pieces)
button3.place(x=740, y=230, width=200, height=60)

button4 = Button(text="If you want to PRINT the \nthe full list of Artists contact \ndetails, press here",
                 font='Helvetica 10 bold', bd=3, bg="khaki", command=print_all_artists)
button4.place(x=740, y=300, width=200, height=60)

button5 = Button(text="If you want to ADD \na new Piece of art,\n press here", font='Helvetica 10 bold', bd=3, bg="SeaGreen3", command=new_window_1)
button5.place(x=740, y=370, width=200, height=60)

button6 = Button(text="If you want to ADD \na new Artist,\n press here", font='Helvetica 10 bold', bd=3, bg="SeaGreen3", command=new_window_2)
button6.place(x=740, y=440, width=200, height=60)

button7 = Button(text="If you want to REMOVE \na Piece of art,\n press here", font='Helvetica 10 bold', bd=3, bg="IndianRed3", command=new_window_3)
button7.place(x=740, y=510, width=200, height=60)

button8 = Button(text="About", bd=6, command=about)
button8.place(x=940, y=593, width=60, height=30)
button8.config(font='Helvetica 10 bold', foreground="black")

listbox1 = Listbox(bg="white", font='Helvetica 11', bd=2)
listbox1.place(x=80, y=230, width=640, height=342)

window.mainloop()
db.close()"""
