import pandas as pd

quizlet_reader = pd.read_csv('quizlet.csv', header=0)	#read csv

randRow = quizlet_reader.sample(1)	#pull random row from csv
question = randRow.iat[0, 1]		#definition at random row
answer = randRow.iat[0, 0]			#term at random row

#pull 3 more random terms for incorrect choices
choice1 = quizlet_reader.sample(1).iat[0,0]	
choice2 = quizlet_reader.sample(1).iat[0,0]
choice3 = quizlet_reader.sample(1).iat[0,0]

#remove ':' from terms
answer = answer[:-2]
choice1 = choice1[:-2]
choice2 = choice2[:-2]
choice3 = choice3[:-2]