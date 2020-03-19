import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')
budget_csv = "../Resources/budget_data.csv"

# Define the function and have it accept the 'budget_data' as its sole parameter
def print_FinancialAnalysis(Budget_data):
    # For readability, it can help to assign your values to variables with descriptive names
    Months = str(Budget_Data[0])
    ProfitLoses = float(Budget_data[1])

    # Total months can be found by countring rows
    total_months = len(Months)

    # The net total amount of "Profit/Losses" over the entire period
    # Can be found by addeding all of the values in row[2]
    net_profitslosses =  "${:,.2f}".format(sum(ProfitLoses))

    #def as_currency(net_profitslosses):
        #if net_profitslosses >= 0:
         #return '${:,.2f}'.format(net_profitslosses)
        #else:
         #return '-${:,.2f}'.format(-net_profitslosses)

    #The average_change of the changes in "Profit/Losses" over the entire period
    #Can be found by a nested function for average? or Net_ProfitLoses / total_months
    average_change = "${:,.2f}".format(net_profitslosses/total_months)

    #def as_currency(average_change):
        #if average_change >= 0:
         #return '${:,.2f}'.format(average_change)
        #else:
         #return '-${:,.2f}'.format(-average_change)

    #The greatest_increase_in_profits (date and amount) over the entire period
    #Find a formula or function that will identity the largest number in data set and identify it
    greatest_increase = "${:,.2f}".format(max(ProfitLoses))
    
    #def as_currency(greatest_increase):
        #if greatest_increase >= 0:
            #return '${:,.2f}'.format(greatest_increase)
        #else:
            #return '-${:,.2f}'.format(-greatest_increase)

    #The greatest decrease in losses (date and amount) over the entire period
    #Find a formula or function that will identity the smallest number in data set and identify it
    greatest_decrease = "${:,.2f}".format(min(ProfitLoses))

    #def as_currency(greatest_decrease):
        #if greatest_decrease >= 0:
            #return '${:,.2f}'.format(greatest_decrease)
        #else:
            #return '-${:,.2f}'.format(-greatest_decrease)

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    # ? Loop through the data
    for row in csvreader:

        #Print Data 
        print("Financial Analysis")
        print("Total Months:" + total_months)
        print("Total:" + net_profitslosses)
        print("Average Change:" + average_change)
        print(("Greatest Increast in Profits:" + greatest_increase)[0,1])
        print(("Greatest Decrease in Profits:" + greatest_decrease) [0,1])

# Specify the file to write to
budget_csv = os.path.join("..", "output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(budget_csv, 'a') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total', 'Average Change', 'Greatest Increase in Profits', 'Greatest Decrease in Profits'])

    # Write the second row
    csvwriter.writerows(['Total_Months', 'net_profitslosses', 'average_change', 'Greatest Increase', 'Greatest Decrease' ])