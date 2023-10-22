import csv

#Read csv file and writes to lists
file_path = 'C:/Users/raols/OneDrive/Desktop/Bootcamp/python-challenge/PyPoll/Resources/election_data.csv'

#variables
cand_list = []
vote_tally = []
vote_perc = []
cand0 = 0
cand1 = 0
cand2 = 0
#opens file
with open(file_path) as election_file:
    e_data = csv.reader(election_file,delimiter = ',')
    csvheader=next(e_data)
    print(csvheader)
    e_data = list(e_data)
    
    #counts number of rows for month count and prints   
    row_count = sum(1 for row in e_data)
    print(row_count)
    
    #creates list of unique candidates
    for row in e_data:
        if row[2] not in cand_list:
            cand_list.append(row[2])
    print(cand_list)

#Tallies count for each candidate and stores in separate variable    
    for row in e_data:
        if row[2] == cand_list[0]:
            cand0 += 1
        if row[2] == cand_list[1]:
            cand1 += 1            
        if row[2] == cand_list[2]:
            cand2 += 1            
    vote_tally = [cand0,cand1,cand2]
    print(vote_tally) 
    vote_perc = [round(cand0/row_count*100,2),round(cand1/row_count*100,2),round(cand2/row_count*100,2)]
    print(vote_perc)

    #     Creates dictionary to hold results
    results = {cand_list[0]: vote_perc[0], cand_list[1]: vote_perc[1],cand_list[2]: vote_perc[2]}
    
    #assesses winner
    def test(results):
        return max(results, key = results.get)
    winner =test(results)
    print(winner)
    
lines = [f'There were {row_count} votes',f'Results were {cand_list[0]} got {vote_tally[0]} or {vote_perc[0]} percent',f'{cand_list[1]} got {vote_tally[1]} or {vote_perc[1]} percent', f'{cand_list[2]} got {vote_tally[2]} or {vote_perc[2]} percent.',f'The winner is {winner}']
with open('results.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')