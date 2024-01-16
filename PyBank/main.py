import os
import csv

#relative path to the budget data csv file
budget_data_import = os.path.join("PyBank", "Resources", "budget_data.csv") 

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
    #using list comprehension
    profits_losses_changes = [(profits_losses[x+1] - profits_losses[x]) for x in range(len(profits_losses)-1)]
    
    #calculate the average monthly change as the total overall changes, divided by the number of changes analyzed
    avg_change = (sum(profits_losses_changes))/(int(len(profits_losses_changes)))
    
    #prepare to merge the monthly change and month lists by making them the same size,
        #removing first date from month as there is no change associated with the first day
    #list cloning source: https://stackoverflow.com/questions/2612802/how-do-i-clone-a-list-so-that-it-doesnt-change-unexpectedly-after-assignment
    months_change = list(months)
    months_change.pop(0)
    
    date_with_amount = list(zip(months_change, profits_losses_changes))
    #set variables for max & min as a counter to use in loop
    max = 0
    min = 0
    for row in date_with_amount:
       if int(row[1]) > max:
        max = int(row[1])
        max_index = date_with_amount.index(row)
       elif int(row[1]) < min:
        min = int(row[1])
        min_index = date_with_amount.index(row)
  
    #print to terminal
    print("Financial Analysis")
    print("----------------------------------")
    print(f"Total: ${net_total}")  
    print(f"Total Months: {str(len(months))}")
    print(f"Average Change: ${float(round(avg_change, 2))}")
    print(f"Greatest Increase in Profits: {date_with_amount[max_index]}") 
    print(f"Greatest Decrease in Profits: {date_with_amount[min_index]}")

    #next set up to export to new txt file
    #add \n to format as each piece of information on their own line (https://www.w3schools.com/python/ref_file_write.asp)
    with open('PyBank\Analysis\PyBankSummary.txt', 'w') as pb:
        pb.write(f"Financial Analysis: Total: ${net_total} \nTotal Months: {str(len(months))} \nAverage Change: ${float(round(avg_change, 2))} \nGreatest Increase in Profits: {date_with_amount[max_index]} \nGreatest Decrease in Profits: {date_with_amount[min_index]}")
   

  


    
    