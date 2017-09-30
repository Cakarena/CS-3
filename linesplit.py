textfile = open ('linesplit.txt', 'r')
total = 0
count = 0
for line in textfile:
		approvals = "Approvals_2016"
		approvals.replace("Approvals_2016"," ")##finds this stupid line and removes it
		while approvals == " ":
			continue
		for line in textfile:
			fields = line.split("|")
			field1 = fields[0]
			field2 = fields[1]
			field3 = fields[2]
			print(fields[2]) ##prints all the numbers in Approvals_2016 column

			numlist = list()
			value = float(field3)
			numlist.append(value)
			total = total + value
			count = count + 1
print("Complete Total of Approvals_2016 for all districts", total)

## Exercise 5, Find content for linesplit.txt here: https://docs.google.com/document/d/1yHJpag_E7fxLRq1Yx2aChZpT_AG-7_IN8bfuEiMJG1U/edit
##Below is an extracted dataset from NSW Department of Planning and Environment showing counts of building approvals
## and completions for previous years. 
##Please put this in a text file. 
##Write a program to read each record and output the total number of approvals in the Central district for year 2016. 
