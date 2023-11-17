import os
import csv

# Path to csv file
election_data_csv_path = os.path.join("Resources", "election_data.csv")

# Output file path
output_file_path = os.path.join("Analysis","PyPoll_results.txt")

# Open and read csv
with open(election_data_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # header row
    header = next(csv_reader)

    # store values in empty lists
    votes = []
    candidates = []

    # set initial variables
    total_votes = 0
    candidate_votes = {}

    # loop through csv rows
    for row in csv_reader:
        # The total number of votes cast
        total_votes += 1

        # The complete list of candidates who received votes
        candidate_name = row[2]
        votes.append(candidate_name)

        # Count the votes for each candidate
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1

# Output the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and display the percentage of votes each candidate won
for candidate, votes_received in candidate_votes.items():
    percentage = (votes_received / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes_received})")

print("-------------------------")

# Find the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)
print(f"Winner: {winner}")
print("-------------------------")

# Open a text file for writing
with open(output_file_path, 'w') as output_file:
    # Write the results to the file
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    # Calculate and write the percentage of votes each candidate won
    for candidate, votes_received in candidate_votes.items():
        percentage = (votes_received / total_votes) * 100
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes_received})\n")

    output_file.write("-------------------------\n")

    # Find the winner based on popular vote and write to the file
    winner = max(candidate_votes, key=candidate_votes.get)
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
