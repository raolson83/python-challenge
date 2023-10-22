#Read csv file and writes to lists
budget_path = 'C:/Users/raols/OneDrive/Desktop/Bootcamp/python-challenge/PyBank/Resources/budget_data.csv'

#opens file
with open(budget_path) as budget_file:
    budget_data = csv.reader(budget_file,delimiter = ',')
    csvheader=next(budget_data)
#sets initial values for month and profit    
    first_month = next(budget_data)
    prev_profit = int(first_month[1])
    budget_data = list(budget_data)
    profit_sum = prev_profit
#counts number of rows for month count, and adds 1 for first month    
    row_count = sum(1 for row in budget_data)+1
    
#for loop for all processes    
    for row in budget_data[0:]:
        curr_profit = int(row[1])
        curr_month = row[0]
 #calculates sum
        profit_sum = profit_sum + curr_profit
        
# Calculate difference
        diff = curr_profit - prev_profit

# append to list
        diff_months.append(curr_month)
        diff_list.append(diff)

# compare greatest increase
        if diff > greatest_increase_amount:
            greatest_increase_amount = diff
            greatest_increase_month = curr_month

# compare greatest decrease
        if diff < greatest_decrease_amount:
            greatest_decrease_amount = diff
            greatest_decrease_month = curr_month

# Reset prev_profit using this month's number
        prev_profit = curr_profit

#prints number of months
print(row_count)

#prints total
print(profit_sum)
        
#prints the difference between each row and previous        
print(diff_list)

#prints greatest increase and greatest decrease with month
print(greatest_increase_amount, greatest_increase_month)
print(f'Greatest Decrease: {greatest_decrease_amount} during {greatest_decrease_month} month')

#print average change
totalavgchange = sum(diff_list)/len(diff_list)
print(totalavgchange)


lines = [f'There are {row_count} rows',f'total profit is {profit_sum}',f'The total difference is {totalavgchange}',f'The greatest increase amount and month is {greatest_increase_amount} in {greatest_increase_month}',f'The greatest decrease amount and month is {greatest_decrease_amount} in {greatest_decrease_month}']
with open('results.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')