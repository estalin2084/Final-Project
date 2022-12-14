# Name: Final Project.py
# Author: Estalin Peña
# Date Created: November 13, 2022
# Date Last Modified: December 12, 2022
# Purpose: A new travel agency, displaying the customers different cities to travel between Winnipeg other cities in Canada and USA.

hours = ["M", "A", "N"] #list to validate the hours of flight.

import random
import string

def chosenHours(): #Input checker for the hours of flight
    while True:
        try:
            chosen_hours = int(input("Please select your preferred hour: "))
        except:
            print("Please select a valid option! ")
        else: 
            if chosen_hours not in range(1,4):
                continue
            else:
                break
    return chosen_hours

#Dictionary to choose the kind of loyalty plan the user has
loyalty  = {
"1": {"Name": "Platinum",
"Percentage" : "20%",
"Value": 0.20}, 
"2": {"Name" : "Gold",
"Percentage" : "15%",
"Value": 0.15}, 
"3": {"Name" : "Silver",
 "Percentage" : "10%",
 "Value": 0.10}, 
"4": {"Name" : "Bronze", 
"Percentage": "5%",
"Value": 0.05}
}

#Class Shopping cart, use to calculate, total and discount
class shopping_cart():
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount
        self.total = 0

    def calculate_total(self, discount):
        self.discount = discount
        self.total = self.price * discount
        return self.total



    def get_total_price(self):
        return self.price * 1.13

#Function Loyalty tier, used to determine the kind of of loyalty program the client has.
def loyalty_tier(car):
   while True:
        discount = input("Do you have a loyalty plan [Yes/No]: ")
        print("")
        while discount.upper() != "YES" and discount.upper() != "Y" and discount.upper() != "NO" and discount.upper() != "N":
            discount = input("Do you have a loyalty plan [Yes/No]: ")
        if discount.upper() == "YES" or discount.upper() == "Y":
            discount = True  
            for x in loyalty.keys():
                print("{} - {} - {}".format(x, loyalty[x]["Name"], loyalty[x]["Percentage"]))
            print("")
            chosen_loyalty = input("Please indicate your loyalty plan: ")
            while chosen_loyalty not in loyalty:
                chosen_loyalty = input("Please choose a number between 1 and 4: ")
                continue
            selection = loyalty[chosen_loyalty]["Percentage"]
            print("")
            print("Your discount is " "{}" "{}".format("", selection))
            car.calculate_total(loyalty[chosen_loyalty]["Value"])
            break
        elif discount.upper() == "NO" or discount.upper() == "N":
                discount = False
                print("Sorry, this time you won't get any discounts! ")
                break

#List to present the user the way of payment
payment_list = ["Credit", "Debit", "PayPal", "ApplePay", "GooglePay"]

#Dictionary used to display the user the travel time from one city to another
flight_time = {
    
1:{"Destination" : "New York",
"Time": "5 h 15 min"},
2:{"Destination" : "Toronto",
"Time": "2 h 35 min"},
3:{"Destination" : "Vancouver",
"Time": "3 h 05 min"},
4:{"Destination" : "Montreal",
"Time": "2 h 25 min"},
5:{"Destination" : "Chicago",
"Time": "4 h 35 min"},
6:{"Destination" : "Boston",
"Time": "5 h 55 min"}

}
#Class Flight used to present the flight time, flight number, departute and arrival city.
class Flight(object):
    def __init__(self, flight_number, dept_city, arri_city):
        self.flight_number = flight_number
        self.dept_city = dept_city
        self.arri_city = arri_city
#Class Customer used to store the customer's information
class Customer(object):

    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.address = ''
        self.phoneNumber = ''
        self.passport = ''
        self.city = ''
        self.province = ''
        self.postalCode = ''
#Class City to present the City name, city code and price.
class City():

    def __init__(self, city_name, city_code, price):
        self.city_name = city_name
        self.city_code = city_code
        self.price = price
#variables created to instance the class City
new_york = City("New York", "NYC", 1000.00)
toronto = City("Toronto", "TOR", 400.00)
vancouver = City("Vancouver", "VAN", 800.00)
montreal = City("Montreal", "MON", 450.00)
chicago = City("Chicago", "CHI", 600.00)
boston = City("Boston", "BOS", 1200.00)

#Destination list to present the user the destionation cities
destination_list = [new_york, toronto, vancouver, montreal, chicago, boston]
#Hours available to travel
morning_hours = ["8:00 A.M.", "9:00 A.M.", "10:00 A.M."]
afternoon_hours = ["2:00 P.M.", "3:00 P.M.", "4:00 P.M."]
night_hours = ["8:00 P.M.", "9:00 P.M.", "10:00 P.M."]

print("{:>40}Welcome to EP Travel Agency! ".format(""))
print("")
print("")
#The only departure city
departure_city = "Winnipeg"


data = False  # variable to set the input data false to enter a while and verify its content.
while not data:

    c = Customer()

    c.first_name = input("Please enter customer's first name: ")  # this input takes the customer's name
    c.last_name = input("Please enter customer's last name: ") #This input takes the customer's last name
    c.address = input("Please enter customer's street number: ")  # this input takes the customer's street number
    c.city = input("Please enter customer's city: ")  # this input takes the customer's city
    c.province = input("Please enter customer's province: ")  # this input takes the customer's province
    c.postalCode = input("Please enter customer's postal code: ")  # this input takes the customer's postal code
    c.phoneNumber = input("Please enter customer's phone number: ")  # this input takes the customer's phone number
    c.passport = input("Please enter your passport number: ")

    for key in vars(c):  # this for iterates the while in the Class and evaluates that all the fields are filled.
        if vars(c)[key] == "":
            print("All fields are mandatory!")
            break
        else:
            data = True
print("")
print("Thank your for your information! ")
print("")
print("These are our destinations: ")
print("")
for x in range(len(destination_list)): #display the destination cities to the customer
    print("{} - {:>2s} - {:2>}".format(x + 1, destination_list[x].city_name, destination_list[x].price))
print("")
while True:#input checker for the destionation city
    try:
        chosen_city = int(input("Which city would you like to travel?:  "))
    except:
        print("Please select a valid option! ")
    else:
        if chosen_city not in range(1,7):
            continue
        else:
            break

dep_time = input("What is your preferred time to travel?: Select M for Morning, A for Afternoon, N for Night: ")
print("")
while dep_time.upper() not in hours:#Input checker for the time of the day
    dep_time = input("Only Select M for Morning, A for Afternoon, N for Night: ")
    
print("")
#Selection for the preferred time of the day to travel
if dep_time.upper() == "M":
    for item in range(len(morning_hours)):
        print("{} - {:>2s} ".format(item + 1, morning_hours[item]))
    print("")
    selection = morning_hours[chosenHours() - 1]
elif dep_time.upper() == "A":
    for item in range(len(afternoon_hours)):
        print("{} - {:>2s} ".format(item + 1, afternoon_hours[item]))
    print("")
    selection = afternoon_hours[chosenHours() - 1]
elif dep_time.upper() == "N":
    for item in range(len(night_hours)):
        print("{} - {:>2s} ".format(item + 1, night_hours[item]))
    print("")
    selection = night_hours[chosenHours() - 1]

print("")

cart = shopping_cart(0,0) #Instancing Shoping cart Class
cart.price = destination_list[chosen_city - 1].price
cart.tax = 1.13
loyalty_tier(cart) # instancing function Loyalty tier
cart.total

#Instancing variables from the Class Customer to print the customer's information
name = c.first_name
last = c.last_name
passport = c.passport
phone = c.phoneNumber


print("")
print("Your flight is from {} to {} at {}".format(departure_city, destination_list[chosen_city - 1].city_name, selection))
print("")
print("Your discount for your Loyalty Plan is: {} CAD".format(cart.total))
print("")
print("The price of your flight is {:.2f} CAD - Taxes included".format(cart.get_total_price() - cart.total))
print("")
print("How would you like to pay? ")
print("")
#Displays the list of payment options
for x in range(len(payment_list)):
    print("{} {}".format(x + 1, payment_list[x]))
print("")

while True:#Input checker for the payment
    try:

        received_payment = int(input("Please choose your payment method: "))
    except:
        print("Please select a number between 1 and 5")
    else:
        if received_payment not in range(1, 5):
            continue
        else:
            break

pay = payment_list[received_payment -1] #variable to store the payment received
ticket_id =  '-'.join(random.choices(string.digits, k=8)) #Ticket generator
flight_n = '-'.join(random.choices(string.digits, k=4)) #Flight number generator
print("")
print("Your payment was received via {}".format(pay))
print("")
print("Thank you for flying with us, this is your flight information: ")
print("-" * 80)
print("Traveler's Information: {} {} \nPhone: {} \nPassport: {}".format(name,last,phone, passport))
print("Your flight number is: {}".format(flight_n))
print("Eticket code: {}\nDeparture City - {} - Gate B\nArriving City - {} - City Code - {} \nDeparture Time: {}\nArriving Gate: A".format(ticket_id, departure_city, destination_list[chosen_city - 1].city_name, destination_list[chosen_city - 1].city_code, selection))
print ("Your estimated flight time is: {} ".format(flight_time[chosen_city]["Time"]))

openfile =open(r"C:\Users\Estalin Pena\Desktop\Programming-_Tasks\Final-Project\TravelInfo.txt", "w")

openfile.write("")
openfile.write("\nYour payment was received via {}".format(pay))
openfile.write("")
openfile.write("\nThank you for flying with us, this is your flight information: ")
openfile.write("-" * 80)
openfile.write("\nTraveler's Information: {} {} \nPhone: {} \nPassport: {}".format(name,last,phone, passport))
openfile.write("\nYour flight number is: {}".format(flight_n))
openfile.write("\nEticket code: {}\nDeparture City - {} - Gate B\nArriving City - {} - City Code - {} \nDeparture Time: {}\nArriving Gate: A".format(ticket_id, departure_city, destination_list[chosen_city - 1].city_name, destination_list[chosen_city - 1].city_code, selection))
openfile.write ("Your estimated flight time is: {} ".format(flight_time[chosen_city]["Time"]))
openfile.close()



