# The data we need to retrieve.
# 1. the total number of votes cast
# 2. A complete list of candidates who recieved votes
# 3. the percentage of votes each candidate won
# 4. the total number of votes each candidate won
# 5. the winner of the election based on popular vote

# add dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # read and print the header row
    headers = next(file_reader)
    print(headers)
   
   
   
   
   
   
    # write three counties to the file analysis.txt
    #txt_file.write("Counties in the Election\n---------------------\nArapahoe\nDenver\nJefferson")

