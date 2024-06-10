# use the for loop to set range 1-10 
# if i in the range is less than or equal to 5 then print "*" * index
# include a variable that tracks the decreasing number of indeces and therefore the stars. num_star = 10 - i
# else the indeces are greater than 5 then print "*" * num_star

for i in range(1, 10):
    
    if i <= 5:
        print("*" * i)
    else: 
        num_star = 10 - i
        print ("*" * num_star )
        
        