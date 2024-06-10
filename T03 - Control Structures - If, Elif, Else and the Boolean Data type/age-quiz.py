# Ask for users age - string
# store the output as int, tell python to save the output as a value names age 
# put the age condition in order 
# if age > greater than 100, output "Sorry youre dead"
# if age >= grater than or equal to 65, output "Enjoy your retirement"
# if age >= greater than or equal to 40, output "Youre over th Hill!"
# if age = to 21, output "Congrats on your 21st"
# if age < less then 13, output "You qualify for kiddie discount"
# any other age, output Age is but a number

age = int(input("Please enter your age: "))

if age > 100 :
    print("Sorry you are dead!")
elif age >= 65 :
    print("Enjoy your retirment!")
elif age >= 40 :
    print("You're Over the Hill!")
elif age == 21 :
    print("Congrats on your 21st!")
elif age < 13 :
    print("You qualify for a kiddies meal!")
else :
    print ("Age is but a number")
