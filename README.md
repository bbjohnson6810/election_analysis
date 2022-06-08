# election_analysis

## 1. Project Overview

Here, I used Python to analyze Colorado Board of Elections data from an audit of a recent local congressional election.
The following results were requested from the data:

1. The total number of votes cast
2. A complete list of candidates who received votes
3. The total number of votes received by each candidate
4. The percentage of votes won by each candidate
5. The winner of the election based on popular vote

## 2. Resources
 - Data source: election_results.csv
 - Code: PyPoll.py
 - Software: Python v3.8.8, Visual Studio Code 1.67.2

## 3. Results Overview

Raw results can be found in the file ```analysis/election_analysis.txt``` 

The analysis shows that:
- 369,711 total votes were cast in the election
- There were three candidates, each with the following percentage (and number) of votes:
	- Charles Casper Stockham: 23.0% (85,213)
	- Diana DeGette: 73.8% (272,892)
	- Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was Diana DeGette, with 73.8% of the vote 

## 4. Methods Overview

In general terms, I counted votes by iterating through the dataset with a for loop. 
Counting the total rows in the dataset yielded the total number of votes, 
and counting the number of rows with each candidate's name yielded the vote count for each candidate. 
I divided each candidate's vote count by the total vote count to calculate vote percentages, 
then identified the winner of the election as the candidate with the highest number and percentage of votes.
Refer to the code in ```PyPol.py``` for details.