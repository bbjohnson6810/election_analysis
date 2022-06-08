import csv
import os


# variable to load the input file
infile  = os.path.join("resources", "election_results.csv")

# output filename variable
outfile = os.path.join("analysis", "election_analysis.txt")

# initialize the vote counter
total_votes = 0

# initialize list of candidates
candidate_options = []

# initialize dictionary of vote count per candidate
candidate_votes = {}

# initialize winning candidate and winning count tracker
winner = ""
winning_count = 0
winning_percent = 0


# open and read the file
with open(infile) as edat:
    
    # read the file object
    readfile = csv.reader(edat)

    # skip and print the header row
    headers = next(readfile) # next drops the first row, saved as 'headers'
    # print(headers)

    # print each row in the csv file
    for row in readfile:
        
        # add each vote to the total count
        total_votes += 1 

        # save the candidate name from each row
        candidate_name = row[2]

        
        if candidate_name not in candidate_options:
            
            # add the candidate name to the list of candidates
            candidate_options.append(candidate_name)

            # initialize each candidate's vote count
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1


# write results to output file
with open(outfile, "w") as txt_file:

    election_results = (
        f"\nElection Results\n\n"
        f"-------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"-------------------------\n\n")

    # print  final vote count to  terminal
    print(election_results, end="")

    # save final vote count to the text file.
    txt_file.write(election_results)

    # calculate the % of votes for each candidate
    for c in candidate_options:

        num_votes = candidate_votes[c]
        percent_votes = num_votes / total_votes * 100
        # print(f"{c} received {percent_votes:.1f}% of the total vote")
        
        # output candidate's results to the terminal
        candidate_results = f"{c}: {percent_votes:.1f}% ({num_votes:,})\n"
        print(candidate_results)

        # save candidate results to the output file
        txt_file.write(candidate_results)
        txt_file.write(f"\n")

        # decide the winner based on vote count and percentage
        if (num_votes > winning_count) and (percent_votes > winning_percent):
            winning_count = num_votes
            winning_percent = percent_votes
            winner = c

    winner_summary = (
        f"------------------------\n"
        f"Winner: {winner}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winning_percent:.1f}%\n"
        f"------------------------\n"
        )

    # output winner summary to terminal
    print(winner_summary)

    # save winner summary to text file
    txt_file.write(winner_summary)

