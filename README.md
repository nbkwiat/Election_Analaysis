# Election_Analaysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.9, Visual Studio Code

## Summary
The analysis of the election shows that:
- There were "x" votes cas in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham recieved "23%" of the vote and "85,213" number of votes
    - Diana DeGette recieved "73.8%" of the vote and "272,892" number of votes 
    - Raymon Anthony Doane recieved "3.1%" of the vote and "11,606" number of votes   
- The winner of the elction was:
    - Diana DeGette, who recieved "73.8%" of the vote and "272,892" number of votes.

## Challenge Overview
The purpose of this challenge was to use the code I have already written to then analyze the number of votes per county and the highest voter turnout in each county.
## Challenge Summary
I took the code we had used to figure out total vote percentage and turnout to further break it down into the number of votes per county and the percentage of votes per county. Using this we can see that the county with the largest voter turnout was in fact Denver.

I did this by creating a dictionary and list that would hold the list of counties and the votes of each county. from there using loops and conditionals all I had to do was add a count to the tracked variable everytime a county would appear on the looping list.
![county_ list_example](https://user-images.githubusercontent.com/109539205/187251636-245aaab9-d5fb-419e-8751-177cb4fe162e.png)

once I got the total count for each county it was just a matter of calculating the percentage and printing it to the terminal and saving it to our text document. 
