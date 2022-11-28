#CTI-110
#P4HW1-Score List
#Anneliese Palacios
#11/19/22
#

#Getting number of scores from input
#Using nested loop to get scores from input to save in score_list
#Finding lowest score. printing, then removing it from list
#Printing the modified list after removing lowest score
#Finding the average grade and finding the letter grade
#Displaying the average and grade

score_num = int(input('How many scores do you want to enter? '))
score_list = []
numScore = 1
print()
for numScore in range(score_num):
    score = float(input(f'Enter score #{numScore+1}: '))
    while score < 0 or score >100:
        print()
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100')
        print(f'Enter score #{numScore+1} again:', end=' ')
        score = float(input())
    score_list.append(score)
print('\n')
print('----------Results----------')
print(f'Lowest Score  :  {min(score_list)}')
score_list.remove(min(score_list))
print(f'Modified List :  {score_list}')

avg_score = sum(score_list)/len(score_list)
if score <= 100:
    avg = 'A'
    if avg_score < 90:
        avg = 'B'
        if avg_score < 80:
            avg = 'C'
            if avg_score < 70:
                avg = 'D'
                if avg_score < 60:
                    avg = 'F'

print(f'Scores Average:  {avg_score:.2f}')
print(f'Grade         :  {avg}')
print('---------------------------')
