import os
import csv

# Path to csv file
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")

# Specify the output file path
output_file_path = "PyBank_Results.txt" 


# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csv_reader)

    # Creating empty lists to store data in columns
    months = []
    profit_loss_changes = []

    # Assign initial var. values
    month_count = 0
    total_profit_loss = 0
    previous_profit_loss = 0
    max_increase = 0
    max_increase_date = None
    max_decrease = 0
    max_decrease_date = None

    # Go through csv rows
    for row in csv_reader:
        # The total number of months included in the dataset
        month_count += 1

        # Go through csv columns and add months to list
        months.append(row[0])

        # Go through csv columns and add profit/losses to list
        profit_loss = int(row[1])
        total_profit_loss += profit_loss

        # Calculate the changes in profit/loss for each period
        if month_count > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)

            # The greatest increase in profits (date and amount) over the entire period
            if change > max_increase:
                max_increase = change
                max_increase_date = row[0]

            # The greatest decrease in profits (date and amount) over the entire period.
            if change < max_decrease:
                max_decrease = change
                max_decrease_date = row[0]

        # Update the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss

    # Calculate the average change in profit/loss
    average_change = sum(profit_loss_changes) / (month_count - 1)
    average_change = round(average_change, 2)

    # Add formatting to look like the example
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {month_count}")
    print("Net Total Amount of Profit/Losses: $", total_profit_loss)
    print(f"Average Change in Profit/Loss: ${average_change}")
    print(f"Greatest Increase in Profits: {max_increase_date} ${max_increase}")
    print(f"Greatest Decrease in Profits: {max_decrease_date} ${max_decrease}")

# Open a text file for writing
    with open(output_file_path, "w") as output_file:
        # Write results to the text file
        output_file.write("Financial Analysis\n")
        output_file.write("----------------------------\n")
        output_file.write(f"Total Months: {month_count}\n")
        output_file.write(f"Net Total Amount of Profit/Losses: ${total_profit_loss}\n")
        output_file.write(f"Average Change in Profit/Loss: ${average_change}\n")
        output_file.write(f"Greatest Increase in Profits: {max_increase_date} ${max_increase}\n")
        output_file.write(f"Greatest Decrease in Profits: {max_decrease_date} ${max_decrease}\n")
