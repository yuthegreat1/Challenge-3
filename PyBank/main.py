import csv 
import numpy as np
file = 'Resources/budget_data.csv'
#from 08-Ins_ReadCSV
with open(file) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    i = 0
    total = 0
    store = []
    #intialize the variables
    for row in csvreader:
        total += int(row[1])
        i += 1
        store.append([row[0], int(row[1])])
        #make the values into integers and create a list to store them

previous = store[0][1]
#create a value that is considered the lowest
increase = [0, store[0][1]]
decrease = [0, store[0][1]]
#initilize vairbles
change = []
for i in range(len(store)):
    change.append(store[i][1] - previous)
    #find the change in the profit
    if store[i][1] > increase[1]:
        increase[0] = store[i][0]
        increase[1] = store[i][1]
    if store[i][1] < decrease[1]:
        decrease[0] = store[i][0]
        decrease[1] = store[i][1]
    #if they are greater or lower replace the
    previous = store[i][1]
avg_change = np.mean(change[1:])
#print analysis
print("Financial Analysis\n")
print("----------------------------\n")
print("Total Months:" + str(len(store))+"\n")
print("Total: $"+str(total)+"\n")
print("Greatest Increase in Profits:"+str(increase)+"\n")
print("Greatest Decrease in Profits:"+str(decrease)+"\n")
with open('analysis.txt', 'w') as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write("Total Months:" + str(len(store))+"\n")
    f.write("Total: $"+str(total)+"\n")
    f.write("Greatest Increase in Profits:"+str(increase)+"\n")
    f.write("Greatest Decrease in Profits:"+str(decrease)+"\n")