# request the time taken to complete each task in minutes
# write an equation to calculate the total time in minutes for all 3 acitivities 
# put in order the flow of how you want computer to read descending order of values 
# use if-elif-else along with comparason and logical operators to set out the range and their coresponding print values 

Total_time_swim = int(input("Enter the time in minutes taken to complete swimming: "))
Total_time_cycle = int(input("Enter the time in minutes taken to complete cycling: "))
Total_time_run= int(input("Enter the time in minutes taken to complete running: "))

total_time_thri = Total_time_swim+ Total_time_cycle + Total_time_run
print( "Total Triothalon Time in minutes: " , total_time_thri)

if total_time_thri >= 111 :
    print("No Award")
    
elif total_time_thri >=106 and total_time_thri <= 110: 
    print("Pronvinical Scroll")
    
elif total_time_thri >=101 and total_time_thri <= 105:
    print("Pronvinical Half Colours")
    
elif total_time_thri >=0 and total_time_thri <= 100:
    print("Pronvinical Colours")
