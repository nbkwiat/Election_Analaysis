# The data we need to retrieve.
# 1. the total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote
#---------------------------------------------------------
# add dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# initialize candidate list
candidate_options = []

# initialize candidate vote dictionary
candidate_votes = {}

# winning candidate trackers
winning_candidate = ""

winning_count = 0

winning_percentage = 0


#open the election results and read the file
with open(file_to_load) as election_data:

    # Read the header with the reader function
    file_reader = csv.reader(election_data)

    # read and print the header row
    headers = next(file_reader)


    # Print each row in the CSV file
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]

        # if statement to add candidate once
        if candidate_name not in candidate_options:

            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0

        #adds vote to candidate name
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:

    votes = candidate_votes[candidate_name]

    vote_percentage = round((float(votes) / float(total_votes) * 100), 1)

    # To do: print out each candidates name, vote count, and percentage
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        winning_count = votes

        winning_percentage = vote_percentage

        winning_candidate = candidate_name
    
#To do: print out the wining candidate percentage and total
winning_candidate_summary = (
    f"---------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------\n")

print(winning_candidate_summary)