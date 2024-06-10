# ask user to select city destination- 3 options, data type string
# user to input number of nights - data type integer
# user to input number of days, they wish to rent car - data type integer
# set rate for hotel per night and car rentals 
# create functions: hotel_cost(num_nights), plane_cost(city_flight) this will inclde if statement each city diffferent amount, car_rental(rental_days) and holiday_cost including the the 3 parameteres
# invoke the functions by calling them in a total_holiday variable to give total 
# print all the choices/prices for user to see breakdown of cost

# define the functions for destination, flight, hotel and car rentals:
def options():
    print("We have 3 destitinations to choose from: \n")
    print("a = Singapore.")
    print("b = Ecuador.")
    print("c = Turkey. \n")

def hotel_cost (num_nights):
    total_hotel = num_nights * 50  # the hotel per night 
    print("\nYour total hotal cost is: $", total_hotel)
    return total_hotel

def plane_cost (city_flight):
    flight_dict = {"a": 500, "b":300 , "c": 200}  # dictionary with key:value of destination:cost
    value = flight_dict [city_flight]
    print("Cost of your flight is: $ ", value)
    return value

def car_rental (rental_days):
    total_car = rental_days * 10 # price of car rental 
    print("Your total car rental is: $", total_car)
    return total_car

def holiday_cost (hotel_cost, plane_cost, car_rental):
    total_holiday =  hotel_cost + plane_cost + car_rental 
    return total_holiday
    
print("Welcome to Holiday Calculator!\n")

options()

city_flight = input("Select a destination by entering either a, b or c: ")

while city_flight not in ["a", "b", "c"]:  #works as long as the condition is not met ensure ocrrect selection of destintion
    print("Please try again, incorrect entry ")
    city_flight = input("Select a destination by entering either a, b or c: ")
    
num_nights = int(input("Enter Number of nights at hotel: ")) 
rental_days = int(input("Enter Number of days hiring a car: "))

total_holiday = holiday_cost (hotel_cost(num_nights), plane_cost(city_flight), car_rental(rental_days))

print("Enjoy your holiday, your holiday total is: ", total_holiday) 