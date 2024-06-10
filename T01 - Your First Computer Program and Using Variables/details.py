# use input function to ask user for name
# store input result as variable called "name"
# use input function to ask user for age
# store input result as variable called "age"
# use input function to ask user for house number
# store input result as variable called "house number"
# use input function to ask user for street name
# store input result as variable called "street name"
# use string input to colate name, age, house number and street name in that order and store as variable called "sentence"
# print sentence

name = input("What is your Name?")
age = int(input("What is your Age?"))
house_number = input("What is your House Number?")
street_name = input("What is your Street Name?")

sentence = f"My name is {name} I am {age} years old and i live at {house_number} {street_name}"

print(sentence)