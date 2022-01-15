from audioop import maxpp
import csv
import os 
##########################################################################
# 1. Reading of csv and storing data 

# set path name with os to ensure compatibility with different engines
filepath = os.path.join("Resources","budget_data.csv")

Whole_file = []
months = []
totals = []
#Opening and reading each row of the csv file 
with open(filepath) as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:

        #(storing headers) creating a variable of the entire file to ensure we have all the data and can create seperate lists without the header to work on
        Whole_file.append(row)

        #conditional to just inclue the profits/losses in a list (remove header as we want to perform calculations on it and require integers)
        if row[1] != "Profit/Losses":
            totals.append(int(row[1]))
        
        #append list of months - this includes header - which will be removed later
        months.append(row[0])



##########################################################################
# 2. Total months and Total profits/losses calculation


#remove header so we just have the list of months 
months.pop(0)

#calculating the number of months after header is removed 
number_of_months=len(months)

#total just by calculating the sum of profits/losses
total = sum(totals)

############################################################################
# 3. Calculating the monthly change then average change in profits/losses 

# list of changes variable set
change = []

#loop through length of totals - starting from second as we need to assess two months at once
for x in range(1,len(totals)):
    #change calculated by the current month in the range subtracted by the previous months profit/losses
    #it is then add to the list via append
    change.append(totals[x]-totals[x-1])


# average change calculated by summation of changes divided by the number of changes calculated
Average_change= sum(change)/len(change)



############################################################################
# 4. Calculating the minimum and maximum monthly change of profit/losses

#minimum monthly change via min function 
min = min(change)
# have to add an increment to the index as the change occured at the next month
minindex = change.index(min)+1
#month found by using previous index
mindate = months[minindex]

#same rationale applied for max calc
max = max(change)
maxindex = change.index(max)+1
maxdate = months[maxindex]


############################################################################
# 5. Output in terminal and txt file  

print("Financial Analysis")
print("-----------------------")
print(f'Total Months: {number_of_months}')
print(f'Total: ${total}')
print(f'Average Change: ${round(Average_change,2)}')
print(f'Greatest Increase in Profits: {maxdate}  (${max})')
print(f'Greatest Decrease in Profits: {mindate}  (${min})')


#setting path file 
filepathanalysis = os.path.join("analysis","PyBank_analysis.txt")

#opening file and writing txt
with open(filepathanalysis, "a") as f:
    print("Financial Analysis", file=f)
    print("-----------------------", file=f)
    print(f'Total Months: {number_of_months}', file=f)
    print(f'Total: ${total}', file=f)
    print(f'Average Change: ${round(Average_change,2)}', file=f)
    print(f'Greatest Increase in Profits: {maxdate}  (${max})', file=f)
    print(f'Greatest Decrease in Profits: {mindate}  (${min})', file=f)
