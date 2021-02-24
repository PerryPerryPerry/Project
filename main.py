#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse data to get the highest amount of visitors from a region
#Name: <Perry>
#Group Name: <PIA>
#Class: <PN2004K>
#Date: <24/2/2021>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################

#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
  def __init__(self):
    #load excel data (CSV format) to dataframe - 'df'
    df = pd.read_csv('monthlyvisitors.csv')
    UserInput(df)
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch 
#########################################################################
def UserInput(df1):
  #Initialize variables
  FirstLine = 0
  SecondLine = 0

  print("Select a region:", "\n", "(1)Asia Pacific", "\n", "(2)South Asia Pacific", "\n", "(3)Europe","\n", "(4)Middle East", "\n", "(5)South East Asia", "\n","(6)North America", "\n", "(7)Australia", "\n", "(8)Africa")
  
  #Prompt User to select a region
  while True:
    RegionChosen = input("Select a region\n>")
    if RegionChosen == "1":
      CountriesChosen = df1[[' Hong Kong ',' China ', ' Japan ', ' Taiwan ', ' Korea, Republic Of ']]
      Region_name = "Asia Pacific"
      break
    
    elif RegionChosen == "2":
      CountriesChosen = df1[[' India ',' Sri Lanka ', ' Pakistan ']]
      Region_name = "South Asia Pacific"
      break
    
    elif RegionChosen == "3":
      CountriesChosen = df1[[' United Kingdom ', ' Germany ', ' France ', ' Italy ', ' Netherlands ',' Greece ', ' Belgium & Luxembourg ', ' Switzerland ', ' Austria ',' Scandinavia ', ' CIS & Eastern Europe ']]
      Region_name = "Europe"
      break

    elif RegionChosen == '4':
      CountriesChosen = df1[[' Saudi Arabia ', ' Kuwait ', ' UAE ']]
      Region_name = "Middle East"
      break

    elif RegionChosen == '5':
      CountriesChosen = df1[[' Brunei Darussalam ', ' Indonesia ',' Malaysia ',' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ']]
      Region_name = "South East Asia"
      break


    elif RegionChosen == '6':
      CountriesChosen= df1[[' USA ', ' Canada ']]
      Region_name = "North America"
      break

    elif RegionChosen == '7':
      CountriesChosen = df1[[' Australia ', ' New Zealand ']]
      Region_name = "Australia"
      break

    elif RegionChosen == '8':
     CountriesChosen = df1[[' Africa ']]
     Region_name = "Africa"
     break

    else:
      print('Error! Please select a valid region.')
  print(Region_name, "selected")
  print("Please choose a range of years starting from 2006 - 2016.")
  while True:
    #Prompt user for input
    Firstyear = input("Enter starting year(eg.2006):")
    #Error
    if Firstyear.isdigit() == False:
      print("Please enter a valid year")
    #No error
    else:
      Lastyear = input("Enter ending year(eg.2016):")
      #Error
      if Lastyear.isdigit() == False:
        print("Please enter a valid year")
      #No Error
      else:
        Firstyear = int(Firstyear)
        Lastyear = int(Lastyear)
      
        if Firstyear in range(2006, 2016):
          if Lastyear in range(2006, 2016):
            print("The sum of the total visitors, in descending order, between", Firstyear, "and", Lastyear, ":")
            break
          #Error
          else:
              print("ERROR! Please choose a valid Ending year.")
        #Error      
        else:
          print("ERROR! Please choose a valid starting year.")

  if str(Firstyear) == "2006":
          FirstLine = 338
  if str(Firstyear) == "2007":
          FirstLine = 350
  if str(Firstyear) == "2008":
          FirstLine = 362
  if str(Firstyear) == "2009":
          FirstLine = 374
  if str(Firstyear) == "2010":
          FirstLine = 386
  if str(Firstyear) == "2011":
          FirstLine = 398
  if str(Firstyear) == "2012":
          FirstLine = 410
  if str(Firstyear) == "2013":
          FirstLine = 422
  if str(Firstyear) == "2014":
          FirstLine = 434
  if str(Firstyear) == "2015":
          FirstLine = 446
  if str(Firstyear) == "2016":
          FirstLine = 458

  if str(Lastyear) == "2006":
          SecondLine = 349
  if str(Lastyear) == "2007":
          SecondLine = 361
  if str(Lastyear) == "2008":
          SecondLine = 373
  if str(Lastyear) == "2009":
          SecondLine = 385
  if str(Lastyear) == "2010":
          SecondLine = 397
  if str(Lastyear) == "2011":
          SecondLine = 409
  if str(Lastyear) == "2012":
          SecondLine = 421
  if str(Lastyear) == "2013":
          SecondLine = 435
  if str(Lastyear) == "2014":
          SecondLine = 447
  if str(Lastyear) == "2015":
          SecondLine = 457
  if str(Lastyear) == "2016":
          SecondLine = 469

  #Get the values from the csv file by row
  CountryYear = CountriesChosen.iloc[FirstLine:SecondLine]

  #Calculation
  FinalResult = CountryYear.sum(axis=0)
  TopChosen = FinalResult.sort_values(ascending = False)
  #Display the calculation
  print(TopChosen.head(3))
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
  #Project Title
  print('######################################')
  print('# Data Analysis App - PYTHON Project #')
  print('######################################')

  #perform data analysis on specific excel (CSV) file
  DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################