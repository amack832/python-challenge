#import and set path to the CSV File
import os
import csv
from statistics import mean

csvpath=os.path.join('Resources','budget_data.csv')

with open(csvpath, newline = '' ) as csvfile:

    budget_data= csv.reader(csvfile, delimiter=',')

    csv_header = next(budget_data)
  
    months=[]
    profits_losses=[]
    date_profits = {}
    total = 0
    max_minvalues = {}
    #Running throught the data set
    for row in budget_data:
        #Used to find the total value
        currentValue = float(row[1])
        #Place the month's data into the month's series
        months.append(row[0])
        #The total amount of months
        total_months=(len(months))
        #Used to find the total value
        total = total + currentValue
        #Places all of the info from the csv into a dictionary so that each 
        #date can be assigned a value
        if row[0] !='Date':
            date_profits[row[0]]=int(row[1])
    #Uses the variables that are put together
    #in the dictionary. To separate the values, you place them in two separate
    #variables.
    p_l= tuple(date_profits.values())
    m = tuple(date_profits.keys())
    #Stores the values to find the average change into a series
    for r in range(1, total_months):
        profits_losses.append((int(p_l[r]) - int(p_l[r-1])))
    #Find the average change throughout all the changes. Had trouble using the 
    #length of the changes because it would not recognize the length.
    #So ended up just uses a stored mean function to find the average.
    average_change = mean(profits_losses)
    #Again stores the values of changes into another series to find the (max)greatest change
    #and the greatest loss (min).
    for r in range(1, total_months):
        max_minvalues[m[r]] = int(profits_losses[r-1])
    #Find the max and min values
    maxval = (max(zip(max_minvalues.values(), max_minvalues.keys())))
    minval = (min(zip(max_minvalues.values(), max_minvalues.keys())))

    #Printed Finacial Analysis
    print('Finacial Analysis')
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total}')
    print(f'Average Change: ${round(average_change, 2)}')
    print(f'Greatest Increase in Profits:{maxval}')
    print(f'Greatest Decrease in Profits:{minval}')
   
    
   
  
    
    
   




    
    
        


        
    