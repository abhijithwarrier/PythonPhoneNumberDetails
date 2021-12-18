# Programmer - python_scripts (Abhijith Warrier)

# PYTHON SCRIPT TO GET THE INFORMATION OF A PHONE NUMBER USING phonenumbers LIBRARY

# Python provides a module name phonenumbers for this task. This is Python version of Google's
# common library for parsing, formatting, storing and validating international phone numbers.
#
# The module can be installed using the command - pip install phonenumbers

# Importing necessary packages
import phonenumbers
import tkinter as tk
from tkinter import *
from phonenumbers import carrier, geocoder, timezone

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    inumLabel = Label(root, text="Phone No With Country Code : ", bg="slateblue4")
    inumLabel.grid(row=0, column=0, padx=10, pady=5)
    inumEntry = Entry(root, width=20, textvariable=numberInput, bg="slateblue3")
    inumEntry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

    countryCode = Label(root, text="COUNTRY CODE : ", bg="slateblue4")
    countryCode.grid(row=2, column=0, padx=10, pady=5)
    root.countryCode = Label(root, width=20, bg="slateblue3")
    root.countryCode.grid(row=2, column=1, padx=10, pady=5, columnspan=2)

    numberLabel = Label(root, text="NATIONAL NUMBER : ", bg="slateblue4")
    numberLabel.grid(row=3, column=0, padx=10, pady=5)
    root.numberLabel = Label(root, width=20, bg="slateblue3")
    root.numberLabel.grid(row=3, column=1, padx=10, pady=5, columnspan=2)

    providerLabel = Label(root, text="SERVICE PROVIDER : ", bg="slateblue4")
    providerLabel.grid(row=4, column=0, padx=10, pady=5)
    root.providerLabel = Label(root, width=20, bg="slateblue3")
    root.providerLabel.grid(row=4, column=1, padx=10, pady=5, columnspan=2)

    countryLabel = Label(root, text="COUNTRY : ", bg="slateblue4")
    countryLabel.grid(row=5, column=0, padx=10, pady=5)
    root.countryLabel = Label(root, width=20, bg="slateblue3")
    root.countryLabel.grid(row=5, column=1, padx=10, pady=5, columnspan=2)

    timezoneLabel = Label(root, text="TIMEZONE : ", bg="slateblue4")
    timezoneLabel.grid(row=6, column=0, padx=10, pady=5)
    root.timezoneLabel = Label(root, width=20, bg="slateblue3")
    root.timezoneLabel.grid(row=6, column=1, padx=10, pady=5, columnspan=2)

    getDetailsButton = Button(root, text="FETCH", command=getDetails)
    getDetailsButton.grid(row=1, column=1, padx=5, pady=5)
    clearButton = Button(root, text="CLEAR", command=clearEntries)
    clearButton.grid(row=1, column=2, padx=5, pady=5)

# Defining getDetails() function to find the details of the user-input number
def getDetails():
    # Fetching and storing the user-input phone number using the get() of tkinter variable
    phone_number = numberInput.get()
    # Creating a phonenumber object, from input using parse function of phonenumbers library
    phone_number = phonenumbers.parse(phone_number)
    # Fetching and storing the country code
    country_code = phone_number.country_code
    # Fetching and storing the national number
    national_number = phone_number.national_number
    # Fetching the carrier of phone number using name_for_number() of carrier of phonenumbers
    # Syntax - carrier.name_for_number(input_phone_number, language)
    phone_number_carrier = carrier.name_for_number(phone_number, 'en')
    # Fetching country of phone number using description_for_number() of geocoder of phonenumbers
    # Syntax - geocoder.description_for_number(input_phone_number, language)
    phone_number_country = geocoder.description_for_number(phone_number, 'en')
    # Fetching timezone of phone number using time_zones_for_number() of timezone of phonenumbers
    phone_number_timezone = timezone.time_zones_for_number(phone_number)

    # Clearing previous phone-number detail entries if there's any
    root.countryCode.config(text="")
    root.numberLabel.config(text="")
    root.providerLabel.config(text="")
    root.countryLabel.config(text="")
    root.timezoneLabel.config(text="")
    # Showing the new results in the tkinter window
    root.countryCode.config(text=str(country_code))
    root.numberLabel.config(text=str(national_number))
    root.providerLabel.config(text=str(phone_number_carrier))
    root.countryLabel.config(text=str(phone_number_country))
    root.timezoneLabel.config(text=str(phone_number_timezone))

# Defining clearEntries() to clear the values from the text entries of tkinter window
def clearEntries():
    numberInput.set('')
    root.countryCode.config(text="")
    root.numberLabel.config(text="")
    root.providerLabel.config(text="")
    root.countryLabel.config(text="")
    root.timezoneLabel.config(text="")

# Creating object of tk class
root = tk.Tk()
# Setting the title, background color,
# windowsize & disabling resizing property
root.title("PythonPhoneNumberDetails")
root.config(background="darkslateblue")
root.geometry("440x250")
root.resizable(False, False)
# Creating tkinter variable
numberInput = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
