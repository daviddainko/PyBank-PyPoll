import csv
import os

path = os.path.join("Resources", "budget_data.csv")


def analysis():
    with open(path, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        months = 0
        sum_profits = 0
        previous_val = 0
        current_val = 0
        average = 0
        max_val = 0
        min_val = 0
        next(data, None)
        for i in data:
            months += 1
            p_l = int(i[-1])
            sum_profits += p_l
            
            current_val = p_l
            if months > 1:
                change = current_val - previous_val
                average += change
                if change > max_val:
                    max_val = change
                    max_month = i[0]
                if change < min_val:
                    min_val = change
                    min_month = i[0]
            previous_val = current_val
        
        output = ''
        output += 'Financial Analysis \n-------------------------\n'
        output += 'Total Months: ' + str(months) + '\n'
        output += 'Average Change: $' + str((round(average/(months-1), 2))) + '\n'
        output += 'Greatest Increase in Profits: ' + max_month + ' ($' + str(max_val) + ')\n'
        output += 'Greatest Decrease in Profits: ' + min_month + ' ($' + str(min_month) + ')'
        
        print(output)        
        
        #print(months)
        #print(sum_profits)
        #print(round(average/(months-1), 2))
        #print(max_month, max_val)
        #print(min_month, min_val)

        text_file = open('PyBank.txt', 'w')
        text_file.write(output)
        text_file.close()

def main():
    analysis() 

main()
