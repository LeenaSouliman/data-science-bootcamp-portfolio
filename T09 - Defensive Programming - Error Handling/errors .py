

print ("Welcome to the error program. \n") #compliation error; brackets are required 
#print ("\n") complition error; brackets required and also statment usually followed after sentence. complition error; indentation nor new line required
# syntax error ; missing paretheses as line dentation not required and does not follow the coding rule therefore line 8 to 14 inappropiate indentation 

# Variables declaring the user's age, casting the str to an int, and printing the result
age_str = "24"  #syntax error; double equal sign not required, brackets required and number only 
age = int(age_str)  
print("I'm" , age , "years old.") #syntax error; comma instead of the plus sign to concatenate string and integer

# Variables declaring additional years and printing the total years of age
years_from_now = int("3") #into an integer so that its recognised as a whole number
age=30
total_years = age + years_from_now #runtime error;age is not defined variable 
print ("The total number of years:" , total_years) # syntax error; missing brackets, replace '+' with ',' and 'answer_years' incorrect word used

# Variable to calculate the total amount of months from the total amount of years and printing the result
total = 27.5
total_months = total * 12 
print ("In 3 years and 6 months, I'll be " , total_months , " months old") #syntax error; braackets missing, runtime; total variable missed in error

#HINT, 330 months is the correct answer
