# election_analysis

## 1. Overview of Election Audit

Here, I used Python to analyze Colorado Board of Elections data from an audit of a recent local congressional election.
The purpose of this analysis was to quantify vote tallies for each county in the precinct (by raw count and percentage)
and for each candidate to determine the winner of the vote.


## 2. Election Audit Results

Raw results can be found in the output file ```analysis/election_analysis.txt``` 

The analysis shows that:
- 369,711 total votes were cast in the election
- Of three counties in the district:
	- Arapahoe county constituted 6.7% of the vote (24,801 votes)
	- Jefferson county constituted 10.5% of the vote (38,855 votes)
	- Dever county constituted 82.8% of the vote (306,055 votes)

- Denver county had the largest number of votes

- The three candidates received the following vote totals:
	- Charles Casper Stockham: 23.0% (85,213)
	- Diana DeGette: 73.8% (272,892)
	- Raymon Anthony Doane: 3.1% (11,606)
	
- The winner of the election was Diana DeGette, with 73.8% of the vote 

## 3. Election Audit Summary

This Python script produces results for this specific election, but can be easily adapted for other elections with minor changes to the code.
The loops through libraries containing county or candidate names and vote tallies are coded to run independent of library size,
meaning they will run as-is for any number of counties or candidates. The only major changes necessary to the code for future analyses 
will be to change the input file name and/or file structure needed to read in the data and output results to a new file.
Note, however, that the raw data must contain a header with county names in the 2nd column and candidate names in the 3rd column
in order to function properly.