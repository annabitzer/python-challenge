import os
import csv

#relative path to the budget data csv file
budget_data_import = os.path.join ("Resources", "budget_data.csv") 

# Your task is to create a Python script that analyzes the records to calculate each of the following values:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in profits (date and amount) over the entire period

#store data from csv in lists
months = []
profits_losses = []
profits_losses_changes = []

with open(budget_data_import) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    #first, skip header row to start for loop through the dataset
    next(csvreader)

    #store everything in lists
    for row in csvreader:
        #add each month to list
        months.append(row[0])
        #add each profit or loss to list, as integer so numbers can be summed later 
        profits_losses.append(int(row[1]))

    #find net total profit/loss
    net_total = (sum(profits_losses))

    #make a list with the net change of each month. the list will have one less object than profits_losses, since it is change between months.
    #sources used: https://stackoverflow.com/questions/2400840/python-finding-differences-between-elements-of-a-list
    #come back and see if list comprehension methods could be used here?
    for x in range(len(profits_losses) - 1):
        #daily change is day minus previous month
        change = (profits_losses[x + 1]) - (profits_losses[x])
        #add daily change to list
        profits_losses_changes.append(change)  

    #calculate the average monthly change as the total overall changes, divided by the number of changes analyzed
    avg_change = (sum(profits_losses_changes))/(int(len(profits_losses_changes)))
    print(avg_change)

    #prepare to merge the monthly change and month lists by making them the same size, removing first date from month
    #as there is no change associated with the first day
    #list cloning source: https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment
    months_change = list(months)
    months_change.pop(0)
    

    #check work (clean up later to print nicely to terminal)
    print(net_total)  
    print(str(len(months)))
    