import os
import csv
csvpath = os.path.join('..','Resources', 'budget_data.csv')
month = []
profit = []
with open(csvpath, newline ='') as csvfile:
    bankSet = csv.reader(csvfile, delimiter = ',')
    #skip header
    next(bankSet,None)
    for row in bankSet:
        #pull out list of months
        month.append(row[0])
        #count the num of unique month-year values
        numMonths = len(set(month))
        #pull out list of profits
        profit.append(float(row[1]))
        #calculate the total profits
        totProf = sum(profit)
        #find the highest profit
        maxProf = max(profit)
       #find the month with the highest profit
        maxMonth= month[profit.index(maxProf)]
        #find the lowest profit
        minProf = min(profit)
        #find the month with the lowest profit
        minMonth = month[profit.index(minProf)]
#calculate the change in profit between months
i = 0
profChange =[]
while  i <= len(profit)-2:
    profChange.append(profit[i+1]-profit[i])
    i=i+1
#calculate avg change of profit between months
avgChange = sum(profChange)/len(profChange)
#print results
print("Finanicial Analysis \n")
print("---------------------- \n")
print("Total Months: " + str(numMonths) + "\n")
print("Total: " + str(totProf) + "\n")
print("Average Change: " + str(avgChange) + "\n")
print("Greatest Increase in Profits: " + maxMonth + " ($" + str(maxProf)+ ")" + "\n")
print("Greatest Decrease in Profits: " + minMonth + " ($" + str(minProf)+ ")" + "\n")
output_file = os.path.join("bank_final.txt")
with open(output_file, "w") as f:
    f.write("Finanicial Analysis \n")
    f.write("---------------------- \n")
    f.write("Total Months: " + str(numMonths) + '\n')
    f.write("Total: " + str(totProf) + "\n")
    f.write("Average Change: " + str(avgChange) + "\n")
    f.write("Greatest Increase in Profits: " + maxMonth + " ($" + str(maxProf)+ ")" + "\n")
    f.write("Greatest Decrease in Profits: " + minMonth + " ($" + str(minProf)+ ")" + "\n")
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    