'''An election is contested by five candidates. The candidates are numbered 1 to 5 and 
the voting is done by marking the candidate number on the ballot paper. 
Write a program to read the ballots and count the votes cast for each candidate using an array variable count. 
In case, a number read is outside the range 1 to 5, the ballot should be considered as a 'spoil ballot', and 
the program should also count the number of spoiled ballots.
'''

 #vlaues stored for, no. of votes of each candidate 
candidate_vote=[0,0,0,0,0]
spoilt_ballot=0

print('*** Are you ready to vote*** \nEach vote matters ,so vote wisely \nTheir are 5 candidates \n-----------------------------------------------------------------------------')

participants=int(input('Total number of participants: '))

print('To vote for your candidate')

for i in range(1,participants+1):
    
    print(f'Voter {i}: Enter the candidate number(1-5):')
    voting_no=int(input())
    
    print('Vote for Voter {i} stored')
    
    if 1<=voting_no<=5:
        candidate_vote[voting_no-1]+=1 #for matching the indexes of both candidate_vote and voting no
        
    else:
        spoilt_ballot+=1
        print('Oops you have spoilt a ballot ')
        
candidate_number=[1,2,3,4,5]       

for candidate_num,votes in zip(candidate_number,candidate_vote) :
    print(f'Candidate {candidate_num} recived {votes} votes')
    
print(f'Number of spoilt ballot is {spoilt_ballot}')    
