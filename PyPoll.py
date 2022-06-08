# retrieve data
# 1. total number of votes cast
# 2. complete list of candidates who received votes
# 3. percentage of votes each candidate won
# 4. total number of votes each candidate won
# 5. winner of the election based on popular vote

import csv
import os


# variable to load the input file
infile  = os.path.join("resources", "election_results.csv")

# output filename variable
outfile = os.path.join("analysis", "election_analysis.txt")

# open and read the file
with open(infile) as edat:
    
    # read the file object
    readfile = csv.reader(edat)

    # print the header row
    headers = next(readfile)
    print(headers)


