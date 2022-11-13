# Name: Final Project.py
# Author: Estalin Peña
# Date Created: November 13, 2022
# Date Last Modified: December, 2022
# Purpose: A new travel agency, displaying the customers different cities to travel around the world.

print("Welcome to EP Travel Agency! ")
print("")
print("")

customer_Data = {
    "FirstName" : "",
    "LastName" : "",
    "StreetNumber" : "",
    "StreetName" :"",
    "Unit": "",
    "City" : "",
    "Province" : "",
    "PostalCode" : "",
    "PhoneNumber" : ""
}

destination_city = {
     "1" : {
        "City" : "New York",
        "Price" : 500.00, },
    "2" : {
        "City" : "Toronto",
        "Price" : 400.00,  },
    "3" : {
        "City" : "Vancouver",
        "Price" : 1000.00, },
    "4" : {
        "City" : "Montreal",
        "Price" : 450.00,  },
    "5" : {
        "City" : "Chicago",
        "Price" : 600.00,  },
    "6" : {
        "City" : "Boston",
        "Price" : 750.00, }
}

departure_city = "Winnipeg"



data = False #variable to set the input data false to enter a while and verify its content.
while not data:
    
    customer_Data["FirstName"] = input("Please enter customer's first name: ").strip().capitalize() #this input takes the customer's name
    customer_Data["LastName"] = input("Please enter customer's last name: ").strip().capitalize()
    customer_Data["StreetNumber"] = input("Please enter customer's street number: ").strip().split(" ") #this input takes the customer's street number
    customer_Data["StreetName"] = input("Please enter customer's street name: ").strip().split(" ")
    customer_Data["Unit"] = input("Please enter customer's unit: ").strip().split(" ")
    customer_Data["City"] = input("Please enter customer's city: ").strip().capitalize() #this input takes the customer's city
    customer_Data["Province"] = input("Please enter customer's province: ").strip().capitalize() #this input takes the customer's province
    customer_Data["PostalCode"] = input("Please enter customer's postal code: ").strip() #this input takes the customer's postal code
    customer_Data["PhoneNumber"] = input("Please enter customer's phone number: ").strip() #this input takes the customer's phone number
     
    for key in customer_Data: #this for iterates the while dictionary and evaluates that all the fields are filled.
        if customer_Data[key] == "":
            print("All fields are mandatory!")
            break
        else:
            data = True
print("")
print("Thank your for your information! ")
print("")
chosen_city = input("Which city would you like to travel?:  ")

