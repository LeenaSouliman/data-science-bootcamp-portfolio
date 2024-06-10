#while the statement is true i.e the number entered is not -1 then continue to ask for a number
#if -1 is entered then average all the number entered before -1
         
total = 0 
num_count = 0

number = int(input("please insert a number, or -1 to end program : "))

while number != -1:
    total += number
    num_count += 1
    number = int(input("please insert a number, or -1 to end program  : "))
    
    if number == -1:
        print(total)
        break
    
if num_count == 0 :
    print("-1 ends the program, please try again with more numbers")
else:
    average = total / num_count
    print(f"total : {total}")
    print(f"average : {average}")