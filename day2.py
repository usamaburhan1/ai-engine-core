#python -m venv venv (to create a virtual environment)
#venv\Scripts\activate (to activate the virtual environment)
import numpy as np
#using lists for data
sales_list = [4200,7800,3100]
print(sales_list*2)

#using Arrays
sales_array = np.array([4200,7800,3100])
print(sales_array*2)

import numpy as np
sales = np.array([4200,7800,3100,9200,5600])

#basic stats
print("Total:",np.sum(sales))
print("Average:",np.mean(sales))
print("Highest:",np.max(sales))
print("Lowest:",np.min(sales))
print("Std deviation:",np.std(sales))

print(sales > 5000)
print(sales[sales > 5000])

print(np.mean(sales))
print(sales[sales>5000])

# 5 salespeople, 3 months of sales data
sales_2d = np.array([
    [4200, 3800, 5100],  # Alex
    [7800, 8200, 7100],  # Maria
    [3100, 2900, 3400],  # James
    [9200, 9800, 8700],  # Sarah
    [5600, 5200, 6100]   # Tom
])
print(sales_2d)
print("Shape:", sales_2d.shape)

# Grab one person (row)
print(sales_2d[0])      # Alex's 3 months
print(sales_2d[3])      # Sarah's 3 months

# Grab one specific number
print(sales_2d[0][0])   # Alex, month 1
print(sales_2d[3][2])   # Sarah, month 3

# Grab one entire column (all people, one month)
print(sales_2d[:, 0])   # Everyone's month 1
print(sales_2d[:, 1])   # Everyone's month 2

print(sales_2d[1, :])   # ?
print(sales_2d[:, 2])   # ?
print(sales_2d[1, 2])   # ?

print(np.sum((sales_2d),axis=0) )# calculate down the rows → gives you one number per column (month)
print(np.mean((sales_2d),axis=0))
print(np.sum((sales_2d),axis=1 ))#calculate across columns → gives you one number per row (person)
print(np.mean((sales_2d),axis=1))

print(np.max((sales_2d) ))
print(np.argmax((sales_2d) ))

monthly_totals = np.sum(sales_2d, axis=0)
print("Monthly totals:", monthly_totals)
print("Best month:", np.argmax(monthly_totals))

person_totals = np.sum(sales_2d, axis = 1)
print("best person index:", np.argmax(person_totals))

# Give every salesperson a 10% bonus
bonus = sales_2d * 1.10
print(bonus)

# Each month has a different bonus rate
# Month 1: 10%, Month 2: 20%, Month 3: 15%
bonus_rates = np.array([1.10,1.20,1.15])
adjusted = sales_2d * bonus_rates
print(adjusted)

#Element-wise means: multiply each position with its matching position
print(sales_2d[1, 2])           # should be 7100
print(sales_2d[1, 2] * 1.15)    # should be 8165.0


adjusted = sales_2d * bonus_rates
print(adjusted[1, 2])           # should also be 8165.0
print(round(adjusted[1, 2], 2))  # 8165.0


sales_flat = np.array([4200, 7800, 3100, 9200, 5600, 4800])

print("Original shape:", sales_flat.shape)

reshaped = sales_flat.reshape(2, 3)
print("Reshaped:\n", reshaped)
print("New shape:", reshaped.shape)
auto_reshaped = sales_flat.reshape(-1, 2) #-1 means "figure out this dimension automatically"
print(auto_reshaped)
print(auto_reshaped.shape)

# Day 2 Final Exercise
import numpy as np

sales = np.array([
    [4200, 3800, 5100, 4600],
    [7800, 8200, 7100, 8900],
    [3100, 2900, 3400, 3200],
    [9200, 9800, 8700, 9100],
    [5600, 5200, 6100, 5800],
    [6200, 6800, 6500, 7100]
])

bonus_rates = np.array([1.10, 1.15, 1.20, 1.25])

print(np.mean(sales[0]))
print(np.mean(sales[1]))
print(np.mean(sales[2]))
print(np.mean(sales[3]))
print(np.mean(sales[4]))

#the correct way using axis
print(np.mean(sales, axis=1))

best_month = np.max(sales)
print("thebest month is",best_month)
#the correction
total_monthly = np.sum(sales, axis=0)
best_month1 = np.argmax(total_monthly)
print("thebest month is", best_month1)

alex = (np.sum(sales[0]))
maria = (np.sum(sales[1]))
james = (np.sum(sales[2]))
sarah =(np.sum(sales[3]))
tom = (np.sum(sales[4]))

worst_person = np.argmin([alex,maria,james,sarah,tom])
print("the worst performing sales person is",worst_person)
#correction
total_per_person = np.sum(sales, axis=1)
print("the worst performing sales person is",np.argmin(total_per_person))

final_bonus = bonus_rates*(sales)
print(final_bonus)

reshaped_sales = sales.reshape(3,8)
print(reshaped_sales)

# Average per person
print(np.mean(sales, axis=1))

# Best month
print("Best month index:", best_month1)

# Worst person
print("Worst person index:", np.argmin(total_per_person))
